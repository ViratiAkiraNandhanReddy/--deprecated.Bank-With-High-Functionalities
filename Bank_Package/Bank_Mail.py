import smtplib
# from . import 

class Mail():
  
    def __init__(self,ReceiverMailAddress: str) -> None:
        self.MailAddress = ReceiverMailAddress
    
    def SendMail(self) -> None:
        pass


class Two_Factor_Authentication(Mail):
    pass

class Forgot_Password(Mail):
    pass

class Send_Multiple_Mail(Mail):
    pass

