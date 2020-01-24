"""
@Author : P.Gnanender Reddy
@Since : Dec'2019
@Keywords:SMTP(simple mail transfer protocol),jwt.
@Description:This code is SMTP i.e., simple mail transfer protocol, and it  used for sending mails using jwt.
"""


import os
import smtplib
from email.mime.text import MIMEText
import jwt
from dotenv import load_dotenv

load_dotenv()


class smtp:
    """
    This class is for starting smtp and send email to other accounts.
    """
    def __init__(self):
        self.server = os.getenv("SMTP_EXCHANGE_SERVER")
        self.port = os.getenv("SMTP_EXCHANGE_PORT")
        self.s = smtplib.SMTP(self.server, self.port)

    def start(self):
        """
        Initilaizing the smtp.
        """
        self.s.starttls()

    def login(self):
        """
        This function is for starting the smtp.
        """
        self.s.login(os.getenv("SMTP_EXCHANGE_USER_LOGIN"), os.getenv("SMTP_EXCHANGE_USER_PASSWORD"))

    def send_mail(self, email_id):
        """
        This function is for sending the email using the smtp.
        """
        encoded_jwt = jwt.encode({'email': email_id}, 'secret', algorithm='HS256').decode("UTF-8")
        data = f"http://localhost:8080/reset/?new={encoded_jwt}"
        msg = MIMEText(data)
        print(msg)
        self.s.sendmail(os.getenv("SMTP_EXCHANGE_USER_LOGIN"), email_id, msg.as_string())

    def __del__(self):
        """
        This function is used for quitting the smtp.
        """
        self.s.quit()