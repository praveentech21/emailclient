import base64
from authenticate import *
from send_resopnce import send_email
from email_classifier import classify_emails
from flask import Flask, redirect, request, Response
from googleapiclient.discovery import build

app = Flask(__name__)

SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

@app.route('/')
def index():
    creds = None         

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if creds and creds.valid:
        return redirect('/emails')
    else:
        authorization_url, flow = authenticate()
        return redirect(authorization_url)


@app.route('/callback')
def callback():
    code = request.args.get('code')
    flow = Flow.from_client_secrets_file(
        'credentials.json',
        scopes=SCOPES,
        redirect_uri='http://localhost:5000/callback'
    )
    flow.fetch_token(code=code)
    creds = flow.credentials

    with open('token.json', 'w') as token:        
        token.write(creds.to_json())

    return redirect('/emails')

@app.route('/emails')
def fetch_emails():
    creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    service = build('gmail', 'v1', credentials=creds)

    sample = fetch_and_update_emails()

    if sample:
        message = get_email(service, sample)
        if message:
            sender = next((header['value'] for header in message['payload']['headers'] if header['name'] == 'From'), '')
            subject = next((header['value'] for header in message['payload']['headers'] if header['name'] == 'Subject'), '')
            body = ''

            if 'parts' in message['payload']:
                for part in message['payload']['parts']:
                    if part['mimeType'] == 'text/plain':
                        body = base64.urlsafe_b64decode(part['body']['data']).decode('utf-8')
                        break

            predition = classify_emails(body, subject, sender)  
            print(predition)
            email_send = send_email(sender, subject, predition)  
                            
        return email_send
    else:
        return "No new emails found."


if __name__ == '__main__':
    app.run(port=5000)