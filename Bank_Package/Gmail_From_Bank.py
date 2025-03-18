'''

# Send's The Gmail To User's For Their Respective Purposes!
## <ins>*Parent Classes*</ins> 

### 1. Gmail
### 2. Send_Multiple_Gmail

## <ins>*Child Classes*</ins>
### 1. Two_Factor_Authentication
### 2. Forgot_Password
### 3. 




'''
Code = '754A87S56K'

Val = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Two-Factor Authentication Code</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
            -webkit-text-size-adjust: 100%;
            -ms-text-size-adjust: 100%;
        }
        .container {
            width: 100%;
            max-width: 600px;
            margin: 0 auto;
            background-color: #ffffff;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            box-sizing: border-box;
        }
        .header {
            text-align: center;
            padding: 10px 0;
            background-color: #007bff;
            color: #ffffff;
        }
        .content {
            padding: 20px;
        }
        .code {
            font-size: 24px;
            font-weight: bold;
            color: #007bff;
            text-align: center;
            margin: 20px 0;
        }
        .footer {
            text-align: center;
            padding: 10px 0;
            background-color: #f4f4f4;
            color: #777777;
        }
        p {
            margin: 0 0 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Two-Factor Authentication</h1>
        </div>
        <div class="content">
            <p>Dear User,</p>
            <p>To complete your login, please use the following Two-Factor Authentication (2FA) code:</p>
            <div class="code">VALCODE</div>
            <p>This code is valid for 10 minutes. If you did not request this code, please ignore this email.</p>
            <p>Thank you for using our service.</p>
            <p>Best regards,</p>
            <p>Your Company Name</p>
        </div>
        <div class="footer">
            <p>&copy; 2026 Virati Akira Nandhan Reddy. All rights reserved.</p>
        </div>
    </div>
</body>
</html>
'''.replace('VALCODE',Code)



import json
from email.message import EmailMessage
import smtplib
import asyncio
from random import random, randint
from abc import ABC, abstractmethod

Aut = str(int(random()*(999-100)+100)) + chr(randint(65,90)) + str(int(random()*(99-11)+11)) + chr(randint(65,90)) + str(int(random()*(99-11)+11)) + chr(randint(65,90))
Val.replace('VALCODE',Aut)
with open(r'Bank_Package\Bank Initialization.json') as Values:
     Data: dict = json.load(Values)

class Gmail(ABC):
    '''
    ### *This <ins>Parent Abstract Class</ins> is Used To Give A Basic Structure For The Child Classes Which Are Used To Send Mail's To The Given Gmail \
    Address For Their Respective Purposes!*
    ## <ins>*The Child Classes Are :*</ins>
    #### 1. Two_Factor_Authentication
    #### 2. Forgot_Password
    ## <ins>*Note*</ins>
    ### *The Child Classes <ins>Can't Be Used To Send Mail's To Multiple Gmail Address At A Time!</ins>

    '''

    SenderMailAddress = Data.get("Email")
    App_Password = Data.get("App Password")
  
    def __init__(self,ReceiverMailAddress: str) -> None:
        self.MailAddress = ReceiverMailAddress

    @abstractmethod
    def __str__(self) -> str:
        pass
        
    @abstractmethod
    def Authorization_Code(self) -> str: 
        pass
    
    @abstractmethod
    def Send_Gmail(self) -> None:
        pass

    @abstractmethod
    def Resend_Gmail(self) -> None:
        pass

    @abstractmethod
    def Read_Authorization_Code(self) -> None:
        pass

class Two_Factor_Authentication(Gmail):
    '''This Child Class is Used To Send Mail's To The Given Gmail Address For The Two Factor Authentication Purpose!'''

    Code = None

    def __str__(self) -> str:
        return '''This Child Class is Used To Send Mail's To The Given Gmail Address For The Two Factor Authentication Purpose!
                        Note: *Don't Try To Retrieve Any Information From This Class'''

    def Authorization_Code(self) -> str:
        return str(int(random()*(999-100)+100)) + chr(randint(65,90)) + str(int(random()*(99-11)+11)) + chr(randint(65,90)) + str(int(random()*(99-11)+11)) + chr(randint(65,90))
        
    def Send_Gmail(self) -> None:
        pass
    
    def Read_Authorization_Code(self) -> None:
        return super().Read_Authorization_Code()
    
    def Resend_Gmail(self) -> None:
        return super().Resend_Gmail()

    def isAuthorizationSuccessful(self) -> bool:
        AuthorizationCode = self.Authorization_Code()
        if self.Code == AuthorizationCode:
            return True
        return False

class Forgot_Password(Gmail):
    
    Code = None

    def __str__(self) -> str:
        return '''This Child Class is Used To Send Mail's To The Given Gmail Address For The Forgot Password Purpose!
                    Note: *Don't Try To Retrieve Any Information From This Class'''
    
    def Authorization_Code(self) -> str:
        return str(int(random()*(999-100)+100)) + chr(randint(65,90)) + str(int(random()*(99-11)+11)) + chr(randint(65,90)) + str(int(random()*(99-11)+11)) + chr(randint(65,90))

    def Send_Gmail(self) -> None:
        pass

    def Read_Authorization_Code(self) -> None:
        return super().Read_Authorization_Code()
    
    def Resend_Gmail(self) -> None:
        return super().Resend_Gmail()
    
    def isAuthorizationSuccessful(self) -> bool:
        AuthorizationCode = self.Authorization_Code()
        if self.Code == AuthorizationCode:
            return True
        return False


class Send_Multiple_Gmail(ABC):
    '''This Parent Abstract Class is Used To Give A Basic Structure For The Child Classes Which Are Used To Send Mail's To The Given Multiple Gmail's
    Address For Their Respective Purposes!
    ## The Child Classes Are:
    1. Promotional_Mail
    ### *The Child Classes Can Be Used To Send Mail's To Multiple Gmail Address At A Time!'''

    SenderMailAddress = Data.get("Email")
    App_Password = Data.get("App Password")

    def __init__(self,ReceiverMailAddresses: list[str]) -> None:
        self.ReceiverMailAddresses = ReceiverMailAddresses

    @abstractmethod
    def Send_Gmail(self) -> None:
        pass

class Promotional_Mail(Send_Multiple_Gmail):

    def Send_Gmail(self) -> None:
        
        for Gmail_Addresses in self.ReceiverMailAddresses:
            Val.replace('VALCODE',Aut)
            print(Val)
            Emai  = EmailMessage()
            Emai['Subject'] = 'Promotional Mail'
            Emai['From'] = 'Virati Akira Nandhan Reddy'
            Emai['To'] = Gmail_Addresses
            Emai.set_content(Val,subtype='html')
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login("viratiaki29@gmail.com", "hxwt wduo cnii pico")
                smtp.send_message(Emai)
                print('Mail Sent Successfully!')
                
            

        

# print(Two_Factor_Authentication(''))
Promotional_Mail(['viratiaki53@gmail.com','viratiaki29@gmail.com','samsungsmarttv451@gmail.com']).Send_Gmail()


'''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Forgot Password Code</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
            -webkit-text-size-adjust: 100%;
            -ms-text-size-adjust: 100%;
        }
        .container {
            width: 100%;
            max-width: 600px;
            margin: 0 auto;
            background-color: #ffffff;
            padding: 20px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            box-sizing: border-box;
        }
        .header {
            text-align: center;
            padding: 20px 0;
            background-color: #007bff;
            color: #ffffff;
        }
        .header h1 {
            margin: 0;
            font-size: 24px;
        }
        .content {
            padding: 20px;
        }
        .code {
            font-size: 24px;
            font-weight: bold;
            color: #007bff;
            text-align: center;
            margin: 20px 0;
            background-color: #f4f4f4;
            padding: 10px;
            border-radius: 5px;
        }
        .footer {
            text-align: center;
            padding: 20px 0;
            background-color: #f4f4f4;
            color: #777777;
        }
        .footer p {
            margin: 0;
        }
        p {
            margin: 0 0 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Forgot Password</h1>
        </div>
        <div class="content">
            <p>Dear User,</p>
            <p>We received a request to reset your password. Please use the following code to reset your password:</p>
            <div class="code">{{Code}}</div>
            <p>This code is valid for 10 minutes. If you did not request a password reset, please ignore this email.</p>
            <p>Thank you for using our service.</p>
            <p>Best regards,</p>
            <p>Your Company Name</p>
        </div>
        <div class="footer">
            <p>&copy; 2026 Your Company Name. All rights reserved.</p>
        </div>
    </div>
</body>
</html>'''