import json
import cohere
from cohere.responses.classify import Example

def classify_emails(email_body,email_subject,email_sender):
    co = cohere.Client('Qdkqns4Mm8O9XvHZV0oO5RSoMomki7sQsYbX7Yqd')
    
    with open('category.json', 'r') as file:
        examples_data = json.load(file)
        
    examples = [Example(example['message'], example['label']) for example in examples_data['examples']]

    # Classify each email
    if email_body:
        classification_response = co.classify(
            inputs=[email_body],  
            examples=examples,
        )

        classification = classification_response[0]
        predition = classification.prediction

    return predition
    
if __name__ == '__main__':
    classify_emails("Hello, I am writing to inform you that the meeting has been rescheduled to 2:00 PM tomorrow.", "Meeting rescheduled", "ravikumar_csd@srkrec.edu.in")
