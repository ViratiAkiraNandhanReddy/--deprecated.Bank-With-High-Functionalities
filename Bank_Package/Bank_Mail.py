import smtplib
import email
from random import random

class Mail():
  
    def __init__(self,ReceiverMailAddress: str) -> None:
        self.MailAddress = ReceiverMailAddress
    
    def SendMail(self) -> None:
        pass


class Two_Factor_Authentication(Mail):

    @staticmethod
    def __Code () -> int:
        return int(random()*10000)
    
    def Two_Factor_Authentication(self) -> bool:
        AuthorizationCode = self.__Code()







        return False



class Forgot_Password(Mail):
    pass

class Send_Multiple_Mail(Mail):
    pass

