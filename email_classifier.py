import json
import cohere
from cohere.responses.classify import Example
import requests
import subprocess
import time

# Function to classify emails
def classify_emails(emails, examples):
    # Initialize Cohere client with your API key
    co = cohere.Client('Qdkqns4Mm8O9XvHZV0oO5RSoMomki7sQsYbX7Yqd')
    classified_emails = []

    # Classify each email
    for email_data in emails:
        email_body = email_data.get('body', '')  # Extract email body
        if email_body:
            # Classify the email
            classification_response = co.classify(
                inputs=[email_body],  # Wrap email_body in a list
                examples=examples,
            )

            # Add classification result to email data
            email_data['classification_result'] = classification_response
            classified_emails.append(email_data)

    return classified_emails

# Load examples from category.json
with open('category.json', 'r') as file:
    examples_data = json.load(file)

# Extract examples and labels
examples = [Example(example['message'], example['label']) for example in examples_data['examples']]

# Start gmail_api.py script in a separate process
gmail_api_process = subprocess.Popen(["python3", "gmail_api.py"])

# Wait for a moment to ensure gmail_api.py has started
time.sleep(10)  # Adjust the delay as needed

# Retry fetching emails for a few times
retry_count = 5
for _ in range(retry_count):
    # Fetch emails from gmail_api.py
    response = requests.get('http://127.0.0.1:5000/fetch_emails')  # Replace with your actual endpoint URL

    if response.status_code == 200:
        emails = response.json()

        # Classify emails
        classified_emails = classify_emails(emails, examples)

        # Print the classified emails
        print(classified_emails)
        break
    else:
        print("Failed to fetch emails. Retrying...")
        time.sleep(5)  # Adjust the delay between retries as needed
else:
    print("Failed to fetch emails after multiple retries.")
