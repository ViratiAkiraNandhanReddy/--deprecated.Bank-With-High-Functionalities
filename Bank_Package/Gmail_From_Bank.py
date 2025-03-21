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
import json
from email.message import EmailMessage
import smtplib
import asyncio
from random import random, randint
from abc import ABC, abstractmethod

with open(r'Bank_Package\Bank Initialization.json') as Values:
     Data: dict = json.load(Values)


'''                                                          Single Mail's Sending Classes!                                                   '''


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
    def Change_Code(self,Code: str) -> str:
        pass

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
    def Read_Authorization_Code(self,Given_Code) -> None:
        pass

    @abstractmethod
    def isAuthorizationSuccessful(self) -> bool:
        pass

class Two_Factor_Authentication(Gmail):
    '''This Child Class is Used To Send Mail's To The Given Gmail Address For The Two Factor Authentication Purpose!'''
    
    Code = None
    isCodeAccepted = False


    def Change_Code(self,Code: str) -> str:
        return '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Two Factor Authentication Code</title>
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
            border-radius: 5px;
        }
        .footer {
            text-align: center;
            padding: 10px 0;
            background-color: #f4f4f4;
            color: #777777;
        }
        .footer p {
            margin: 0;
        }
        .footer a {
            color: #007bff;
            text-decoration: none;
        }
        .footer a:hover {
            text-decoration: underline;
        }
        p {
            margin: 0 0 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Two Factor Authentication</h1>
        </div>
        <div class="content">
            <p>Dear User,</p>
            <p>To Complete Your login, Please Use The Following Two Factor Authentication (2FA) Code:</p>
            <div class="code">2FA-Code</div>
            <p>This Code is Valid For 10 Minutes. If You Did Not Request This Code, Please Ignore This Email.</p>
            <p>Thank You For Using Our Service.</p>
            <p>Best regards,</p>
            <p><b>Virati Akira Nandhan Reddy</b></p>
        </div>
        <div class="footer">
            <p>&copy; 2026 Virati Akira Nandhan Reddy. All rights reserved.</p>
            <p><a href="mailto:viratiaki29@gmail.com">viratiaki29@gmail.com</a></p>
            <p><a href="https://www.viratiaki29.github.io">www.viratiaki29.github.io</a></p>
        </div>
    </div>
</body>
</html>
'''.replace('2FA-Code',Code)
    
    def __str__(self) -> str:
        return '''This Child Class is Used To Send Mail's To The Given Gmail Address For The Two Factor Authentication Purpose!
                        Note: *Don't Try To Retrieve Any Information From This Class'''

    def Authorization_Code(self) -> str:
        return str(int(random()*(999-100)+100)) + chr(randint(65,90)) + str(int(random()*(99-11)+11)) + chr(randint(65,90)) + str(int(random()*(99-11)+11)) + chr(randint(65,90))
        
    def Send_Gmail(self) -> None:

        Email = EmailMessage()

        self.Code = self.Authorization_Code()
        html_Data = self.Change_Code(self.Code)
        
        Email['Subject'] = 'Two Factor Authentication Code'
        Email['From'] = 'Virati Akira Nandhan Reddy'
        Email['To'] = self.MailAddress
        Email.set_content(html_Data,subtype='html')

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login("viratiaki29@gmail.com", "hxwt wduo cnii pico")
            smtp.send_message(Email)
            print('Mail Sent Successfully!')
    
    def Read_Authorization_Code(self,Given_Code) -> None:
        if Given_Code == self.Code:
            self.isCodeAccepted = True
        
    
    def Resend_Gmail(self) -> None:
        self.Send_Gmail()

    def isAuthorizationSuccessful(self) -> bool:
        return True if self.isCodeAccepted else False


class Forgot_Password(Gmail):
    
    Code = None

    def __str__(self) -> str:
        return '''This Child Class is Used To Send Mail's To The Given Gmail Address For The Forgot Password Purpose!
                    Note: *Don't Try To Retrieve Any Information From This Class'''
    
    def Authorization_Code(self) -> str:
        return str(int(random()*(999-100)+100)) + chr(randint(65,90)) + str(int(random()*(99-11)+11)) + chr(randint(65,90)) + str(int(random()*(99-11)+11)) + chr(randint(65,90))

    def Send_Gmail(self) -> None:
        pass

    def Read_Authorization_Code(self,Given_Code) -> None:
        pass
    
    def Resend_Gmail(self) -> None:
        return super().Resend_Gmail()
    
    def isAuthorizationSuccessful(self) -> bool:
        AuthorizationCode = self.Authorization_Code()
        if self.Code == AuthorizationCode:
            return True
        return False


'''                                                          Multiple Mail's Sending Classes!                                                 '''


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
            # Val.replace('VALCODE',Aut)
            # print(Val)
            Emai  = EmailMessage()
            Emai['Subject'] = 'Promotional Mail'
            Emai['From'] = 'Virati Akira Nandhan Reddy'
            Emai['To'] = Gmail_Addresses
            # Emai.set_content(Val,subtype='html')
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login("viratiaki29@gmail.com", "hxwt wduo cnii pico")
                smtp.send_message(Emai)
                print('Mail Sent Successfully!')
                
            

        

# print(Two_Factor_Authentication(''))
# Promotional_Mail(['viratiaki53@gmail.com','viratiaki29@gmail.com','samsungsmarttv451@gmail.com']).Send_Gmail()
# Two_Factor_Authentication('viratiaki53@gmail.com').Send_Gmail()
# while True:
#     eval(input('Bot: '))
#     print('Bot: Done!')


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