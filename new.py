from flask import Flask, jsonify, redirect, session, request
from flask_cors import CORS
from flask import redirect
import os
import base64
import json
import secrets
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow


app = Flask(__name__)
app.secret_key = os.urandom(24)
CORS(app)

statesample = secrets.token_urlsafe(16)

CLIENT_SECRETS_FILE = 'credentials.json'
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
REDIRECT_URI = 'http://localhost:5000/oauth2callback'

def authenticate():
    try:
        creds = None

        if os.path.exists('token.json'):
            creds = Credentials.from_authorized_user_file('token.json', SCOPES)

        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)

            with open('token.json', 'w') as token:
                token.write(creds.to_json())

        return creds
    except Exception as e:
        print("An error occurred during authentication:", e)
        return None

def get_unseen_emails(service):     
    try:  
        messages = service.users().messages().list(userId='me', labelIds=['UNREAD']).execute()
        message_ids = messages.get('messages', [])
        return message_ids
    except Exception as e:
        print("An error occurred:", e)
        return None

def get_email(service, message_id):
    try:
        message = service.users().messages().get(userId='me', id=message_id['id']).execute()
        return message
    except Exception as e:
        print("An error occurred:", e)
        return None

@app.route('/')
def index():
    return "Welcome to the Gmail API!"

@app.route('/fetch_emails', methods=['GET'])
def fetch_emails():
    creds = authenticate()
    if creds is None:
        return creds
    
    service = build('gmail', 'v1', credentials=creds)
    message_ids = get_unseen_emails(service)
    emails = []

    if message_ids:
        for message_id in message_ids:
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
                emails.append(email_data)

    return jsonify(emails)

@app.route('/oauth2callback')
def oauth2callback():
    try:
        if 'state' not in session or request.args.get('state') != session['state']:
            return 'Invalid state parameter', 400

        flow = Flow.from_client_secrets_file(
            CLIENT_SECRETS_FILE, SCOPES, state=session['state'], redirect_uri=REDIRECT_URI)
        flow.fetch_token(authorization_response=request.url)

        creds = flow.credentials
        session['creds'] = creds.to_json()

        return redirect('/fetch_emails')
    
    except Exception as e:
        print("An error occurred during OAuth callback:", e)
        return 'An error occurred during OAuth callback', 500

if __name__ == "__main__":
    app.run()
