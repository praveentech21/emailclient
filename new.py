import logging
from flask import Flask, jsonify
from flask_cors import CORS
import os
import base64
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from apscheduler.schedulers.background import BackgroundScheduler
import googleapiclient.errors

app = Flask(__name__)
CORS(app)

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

# Global variables to store fetched emails and the latest processed email ID
fetched_emails = []
latest_email_id = None

def authenticate():
    """Authenticate and obtain credentials to access Gmail API."""
    creds = None
    
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
        
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())
            except Exception as e:
                logging.error("Failed to refresh credentials: %s", e)
                return None

    return creds

def get_unseen_emails(service):     
    """Fetch unread emails from Gmail."""
    try:  
        messages = service.users().messages().list(userId='me', labelIds=['UNREAD']).execute()
        message_ids = messages.get('messages', [])
        return message_ids
    except googleapiclient.errors.HttpError as e:
        logging.error("Gmail API HTTP error occurred: %s", e)
        return None
    except Exception as e:
        logging.error("An error occurred while fetching unread emails: %s", e)
        return None

def get_email(service, message_id):
    """Fetch details of a specific email by message ID."""
    try:
        message = service.users().messages().get(userId='me', id=message_id['id']).execute()
        return message
    except googleapiclient.errors.HttpError as e:
        logging.error("Gmail API HTTP error occurred: %s", e)
        return None
    except Exception as e:
        logging.error("An error occurred while fetching email: %s", e)
        return None

def fetch_and_update_emails():
    """Fetch new unread emails and update the fetched_emails list."""
    global fetched_emails, latest_email_id
    try:
        creds = authenticate()
        if not creds:
            logging.error("Authentication failed. Cannot fetch emails.")
            return
        
        service = build('gmail', 'v1', credentials=creds)
        message_ids = get_unseen_emails(service)
        new_emails = []

        if message_ids:
            for message_id in message_ids:
                if latest_email_id is None or message_id['id'] > latest_email_id:
                    if message_id['id'] not in fetched_emails:  # Check if email ID has been processed before
                        message = get_email(service, message_id)
                        if message:
                            sender = next((header['value'] for header in message['payload']['headers'] if header['name'] == 'From'), '')
                            subject = next((header['value'] for header in message['payload']['headers'] if header['name'] == 'Subject'), '')
                            body = ''

                            if 'parts' in message['payload']:
                                for part in message['payload']['parts']:
                                    if part['mimeType'] == 'text/plain':
                                        body = base64.urlsafe_b64decode(part['body']['data']).decode('utf-8')
                                        break  

                            email_data = {
                                "sender": sender,
                                "subject": subject,
                                "body": body
                            }
                            new_emails.append(email_data)
                            fetched_emails.append(message_id['id'])  # Add email ID to processed list
                            latest_email_id = message_id['id']  # Update latest email ID
                        
                            logging.info("New Email ID: %s", message_id['id'])
                            return message_id
        
        # Update fetched_emails list with new emails
        fetched_emails += new_emails
    except Exception as e:
        logging.error("An error occurred during email fetching and update: %s", e)

# Schedule the task to run every 1 minute
scheduler = BackgroundScheduler()
scheduler.add_job(fetch_and_update_emails, 'interval', seconds=20)
scheduler.start()

@app.route('/fetch_emails', methods=['GET'])
def get_fetched_emails():
    """Endpoint to retrieve the fetched emails."""
    global fetched_emails
    return jsonify(fetched_emails)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    app.run(debug=True)