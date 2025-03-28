import smtplib
from email.message import EmailMessage
from . import MultipleGmail, CREDENTIALS

class PromotionalMail(MultipleGmail):
    
    def SendGmails(self) -> str:
        pass 