import smtplib, ssl
from email.message import EmailMessage

email_essentials = data[['Title','Name', 'Email']]  # data frame with the title, name and email columns
email_essentials = email_essentials.dropna()

Salutations = [Title + " " +  Name + "," for Title, Name in zip(email_essentials['Title'] , email_essentials['Name'])] # create salutation
email_templates = [email for email in email_essentials['Email']]


for i in range(0, len(Salutations)-1):
    msg = EmailMessage()
    msg['Subject'] = '[Email Subject]'
    msg['From'] = "[Your Email]"
    msg['To'] = str(email_templates[i]).lower()
    msg.set_content("""\

        Dear {salutation}

       [INSERT BODY HERE]

        """.format(salutation = Salutations[i]))
    
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    password = "[Your Password]"
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login("[Your Email]", password)
        server.send_message(msg)
