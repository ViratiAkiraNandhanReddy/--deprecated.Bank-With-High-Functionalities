'''
# Gmail Module

## Purpose
This module handles email-related functionalities, including sending single or multiple emails and generating authorization codes.

## Key Functionalities
1. **Authorization_Code**: Generates a random 10-character authorization code.
2. **SingleGmail**: Abstract base class for sending a single email.
3. **MultipleGmail**: Abstract base class for sending multiple emails.

## Usage
- Use `Authorization_Code` to generate unique codes for email verification or 2FA.
- Extend `SingleGmail` and `MultipleGmail` to implement specific email-sending logic.

---

## Classes and Functions

### `Authorization_Code`
- **Description**: Generates a random 10-character alphanumeric code.
- **Return Type**: `str`
- **Examples**:
  - `734L34F33O`
  - `157T29U59H`

### `SingleGmail`
- **Description**: Abstract base class for sending a single email.
- **Attributes**:
  - `ReceiverMailAddress (str)`: The recipient's email address.
- **Methods**:
  - `Send_Gmail`: Abstract method to send an email.
  - `Resend_Gmail`: Abstract method to resend an email.

### `MultipleGmail`
- **Description**: Abstract base class for sending multiple emails.
- **Attributes**:
  - `ReceiverMailAddresses (list[str])`: List of recipient email addresses.
- **Methods**:
  - `SendGmails`: Abstract method to send emails to multiple recipients.

---

## Notes
- The module reads login credentials from `Login Credentials.json`.
- Email history is logged in `Gmail History.txt`.

'''

import json
from random import random, randint
from abc import ABC, abstractmethod

HISTORY = open(r'Bank_Package\Gmail\Gmail History.txt', 'a')

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
    def Send_Gmail(self) -> str:
        pass
    
    @abstractmethod
    def Resend_Gmail(self) -> None:
        pass
        
class  MultipleGmail(ABC):
    
    def __init__(self,ReceiverMailAddresses: list[str]) -> None:

        self.ReceiverMailAddresses = ReceiverMailAddresses

    @abstractmethod
    def SendGmails(self) -> str:
        pass

