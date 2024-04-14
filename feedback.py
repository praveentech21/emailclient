import urllib.parse

def feedbacksolvedurl(subject,body,sender):
    encoded_body = urllib.parse.quote(body)
    encoded_subject = urllib.parse.quote(subject)
    encoded_sender = urllib.parse.quote(sender)
    
    url = f"https://praveentech21.github.io/supportpixceltest/solved.html?some=something&body={encoded_body}&sender={encoded_sender}&subject={encoded_subject}"
    return url

def feedbackunsolvedurl(subject,body,sender):
    encoded_body = urllib.parse.quote(body)
    encoded_subject = urllib.parse.quote(subject)
    encoded_sender = urllib.parse.quote(sender)
    
    url = f"https://praveentech21.github.io/supportpixceltest/unsolved.html?some=something&body={encoded_body}&sender={encoded_sender}&subject={encoded_subject}"
    return url

def feedbackcode(subject,body,sender):
    solvedurl = feedbacksolvedurl(subject,body,sender)
    unsolvedurl = feedbackunsolvedurl(subject,body,sender)
    code = f"""
    <html>
    <head>
    <title>Feedback</title>
    </head>
    <body>
    <h2>Please give us your feedback</h2>
    <iframe width="560" height="315" src="https://www.youtube.com/embed/GGTorJjJq-c?si=OYCnkingQGboKOq1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
    <p>is your problem solved : </p>  <a href="{solvedurl}">👍</a><br>
    <p>DO you still have problem : </p>  <a href="{unsolvedurl}">👍</a><br>
    <p>Thank you</p>
    </body>
    </html>
    """
    return code
    
