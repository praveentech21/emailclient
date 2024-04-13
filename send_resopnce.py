import base64
import json

from mailauthcate import mailauthenticate
from email.message import EmailMessage
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def get_responses():
    with open('responce_mails.json') as f:
        responses_data = json.load(f)
    return responses_data['responces']

def get_responce(classfi):
    responses = get_responses()
    response_content = responses.get(classfi, {}).get('responce', 'Default response')
    return response_content

def send_email(to_address, subject, classfi):
    creds = mailauthenticate()
    response_content = get_responce(classfi)
    
    try:
        service = build("gmail", "v1", credentials=creds)
        message = EmailMessage()

        message.set_content(response_content)
        message["To"] = to_address
        message["From"] = "testpixeltest8@gmail.com"
        message["Subject"] = subject

        # encoded message
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

        create_message = {"raw": encoded_message}
        send_message = (
            service.users()
            .messages()
            .send(userId="me", body=create_message)
            .execute()
        )
        print(f'Message Id: {send_message["id"]}')
        return send_message
    except HttpError as error:
        print(f"An error occurred: {error}")
        
