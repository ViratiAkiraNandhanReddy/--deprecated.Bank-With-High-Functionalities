'''


# Gmail


'''

import json
from random import random, randint
from abc import ABC, abstractmethod

#Reads The Important Login Credentials Which Are Used For Sending The Mail's
with open(r'Bank_Package\Gmail\Login Credentials.json', 'r') as LOGIN:
    
    CREDENTIALS: dict = json.load(LOGIN)

# A Code Of Length 10 Characters  
def Authorization_Code() -> str: # EG: 546G63W55E

    '''
    ## <ins>***Returns***</ins>
    ### A Code Of Length 10 Characters
    ### <ins>***Return Type : str***</ins> * 
    
    ## <ins>***Examples***</ins>
    * 734L34F33O
    * 157T29U59H  
    * 983A78K98L

    '''

    return str(int(random()*(999-100)+100)) + chr(randint(65,90)) + str(int(random()*(99-11)+11)) + chr(randint(65,90)) + str(int(random()*(99-11)+11)) + chr(randint(65,90))


class SingleGmail(ABC):

    def __init__(self,ReceiverMailAddress: str) -> None:

        self.ReceiverMailAddress: str = ReceiverMailAddress 

    @abstractmethod
    def Send_Gmail(self) -> None:
        pass
    
    @abstractmethod
    def Resend_Gmail(self) -> None:
        pass
        
class  MultipleGmail(ABC):
    
    def __init__(self,ReceiverMailAddresses: list[str]) -> None:

        self.ReceiverMailAddresses = ReceiverMailAddresses

    @abstractmethod
    def SendGmails(self) -> None:
        pass

