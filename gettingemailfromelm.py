import email

# Path to the downloaded ".eml" file
eml_file_path = "emailbody.eml"
output_text_file = "sample.txt"

def read_eml_file(eml_file_path):
    with open(eml_file_path, "r") as f:
        # Parse the email content
        msg = email.message_from_file(f)
        return msg

def extract_email_body(msg):
    if msg.is_multipart():
        # If the email has multiple parts, concatenate them into a single body
        email_body = ""
        for part in msg.walk():
            if part.get_content_type() == "text/plain":
                email_body += part.get_payload(decode=True).decode()
            elif part.get_content_type() == "text/html":
                email_body += part.get_payload(decode=True).decode()
    else:
        email_body = msg.get_payload(decode=True).decode()
    
    return email_body

# Read the contents of the ".eml" file
eml_msg = read_eml_file(eml_file_path)
# Extract email body
email_body = extract_email_body(eml_msg)

# Write the extracted email body to a text file with UTF-8 encoding
with open(output_text_file, "w", encoding="utf-8") as f:
    f.write(email_body)

print("Email body extracted and saved to:", output_text_file)
