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

def feedbackcode(subject,body,sender,response):
    solvedurl = feedbacksolvedurl(subject,body,sender)
    unsolvedurl = feedbackunsolvedurl(subject,body,sender)
    code = f"""
    <html>
    <head>
    <title>Feedback</title>
    </head>
    <body>
    <div>Responce : <br>{response}</div>
    <h2>Please give us your feedback</h2>
    <div>
    <a href="https://youtu.be/GGTorJjJq-c?si=TcgY6PUJKVp8NOHu"><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQDpH7joGT-VlFWy48EDcIbPd38kBCmbFxGuVA1U96QSvyfLbunlxpxJEqR04edoA4G0Xw&usqp=CAU" ></a></div>
    <p>is your problem solved : </p>  <a href="{solvedurl}">👍</a><br>  
    <p>DO you still have problem : </p>  <a href="{unsolvedurl}">👍</a><br>
    <p>Thank you</p>
    </body>
    </html>
    """
    
    return code