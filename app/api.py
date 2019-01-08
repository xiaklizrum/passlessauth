import smtplib
from .creditals import EMAIL_LOGIN, EMAIL_PASSWORD


class Email:
    EMAIL_SERVER_PORT = 587
    EMAIL_SERVER_URL = 'smtp.gmail.com'
    sender = None

    def __init__(self):
        sender = smtplib.SMTP(self.EMAIL_SERVER_URL, self.EMAIL_SERVER_PORT)
        sender.starttls()
        sender.login(EMAIL_LOGIN, EMAIL_PASSWORD)
        self.sender = sender

    def send(self, from_address, to_address, subject, text):
        msg = 'Subject: {}\n\n{}'.format(subject, text)
        response = self.sender.sendmail(from_address, to_address, msg)
        self.sender.quit()
        return response
