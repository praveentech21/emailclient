import urllib.parse

body = """
    Dear Jayanth, I am Ramesh,

I've enrolled for Pixeltests however I couldn't take up the online LMS
classes due to certain situations.
Would like to resume from FEB24 onwards.
Please help me how I can take it forward.

Thanks

Ramesh KJ
+91 9886041305

"""

subject = "Pixeltests - LMS classes"
sender = "ravikumar_csd@srkrec.edu.in"

encoded_body = urllib.parse.quote(body)
encoded_subject = urllib.parse.quote(subject)
encoded_sender = urllib.parse.quote(sender)

url = f"http://localhost:5000/?some=something&body={encoded_body}&sender={encoded_sender}&subject={encoded_subject}"
print(url)
