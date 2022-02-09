import smtplib

def sentmail():
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(sent_from, to, email_text)
    server.close()

    print('Email sent!')


gmail_user = 'email here'
gmail_password = 'email passwd'

sent_from = gmail_user
to = ['email here']
subject = 'PS5 IS AVAILABLE!!'
body = 'GO GET IT NOW!!! https://store.sony.com.sg/collections/playstation-consoles'
# body = test.body
email_text = """\
From: %s
To: %s
Subject: %s
%s
""" % (sent_from, ", ".join(to), subject, body)

if __name__ == "__main__":
    sentmail()
