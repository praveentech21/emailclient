import json
import cohere
from cohere.responses.classify import Example
from send_resopnce import send_email

def classify_emails(emails):
    co = cohere.Client('Qdkqns4Mm8O9XvHZV0oO5RSoMomki7sQsYbX7Yqd')
    
    with open('category.json', 'r') as file:
        examples_data = json.load(file)
        
    examples = [Example(example['message'], example['label']) for example in examples_data['examples']]

    # Classify each email
    for email_data in emails:
        email_body = email_data.get('body', '')
        email_subject = email_data.get('subject', '')
        email_sender = email_data.get('sender', '')
        if email_body:
            # Classify the email
            classification_response = co.classify(
                inputs=[email_body],  
                examples=examples,
            )

            # Add classification result to email data
            email_data['classification_result'] = classification_response['prediction']
            print(f"Email from {email_sender} with subject {email_subject} classified as {classification_response['prediction']}")
            send_email(email_sender, email_subject, classification_response['prediction'])

    # return "done"
