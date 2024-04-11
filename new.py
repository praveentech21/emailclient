import os
import webbrowser
from threading import Thread
from google_auth_oauthlib.flow import Flow
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from flask import Flask, request

mailapp = Flask(__name__)
mailapp.run(port=8000)

SCOPES = ['https://www.googleapis.com/auth/gmail.send']

def mailauthenticate():
    creds = None
    
    if os.path.exists('mailtoken.json'):
        creds = Credentials.from_authorized_user_file('mailtoken.json', SCOPES)
        
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = Flow.from_client_secrets_file(
            'credentials.json',  # Path to your client secret JSON file
            scopes=SCOPES,
            redirect_uri='http://localhost:8000/callback')
            authorization_url, _ = flow.authorization_url(prompt='consent')
            
            webbrowser.open(authorization_url)

    return creds
        
@mailapp.route('/callback')
def callback():
    code = request.args.get('code')
    flow = Flow.from_client_secrets_file(
        'credentials.json',
        scopes=SCOPES,
        redirect_uri='http://localhost:8000/callback'
    )
    flow.fetch_token(code=code)
    creds = flow.credentials

    with open('mailtokens.json', 'w') as token:        
        token.write(creds.to_json())
