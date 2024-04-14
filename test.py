from cryptography.fernet import Fernet
from urllib.parse import quote, unquote

# Generate a random key
key = 'VEfUSTm7dsygH0qJWOClYPWW182_z6JQfZSqf_ujEw0='
cipher_suite = Fernet(key)

# Encrypt the data
body = "This is the email body."
sender = "sender@example.com"
subject = "Sample Email Subject"

encrypted_body = cipher_suite.encrypt(body.encode())
encrypted_sender = cipher_suite.encrypt(sender.encode())
encrypted_subject = cipher_suite.encrypt(subject.encode())

# URL encode the encrypted data
url_body = quote(encrypted_body)
url_sender = quote(encrypted_sender)
url_subject = quote(encrypted_subject)

# Construct the URL
url = f"http://localhost:5000/?body={url_body}&sender={url_sender}&subject={url_subject}"
print("URL:", url)

# Decryption on the receiving end
decrypted_body = cipher_suite.decrypt(unquote(url_body).encode()).decode()
decrypted_sender = cipher_suite.decrypt(unquote(url_sender).encode()).decode()
decrypted_subject = cipher_suite.decrypt(unquote(url_subject).encode()).decode()

print("Decrypted Body:", decrypted_body)
print("Decrypted Sender:", decrypted_sender)
print("Decrypted Subject:", decrypted_subject)
