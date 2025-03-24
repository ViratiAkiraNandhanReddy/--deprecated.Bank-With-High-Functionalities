import smtplib, time
from email.message import EmailMessage
from . import SingleGmail, CREDENTIALS, Authorization_Code

class Two_Factor_Authentication(SingleGmail):

    Code = None

    # Changes The html Code With The Given 2FA-Code
    def html_Code(self, Code: str) -> str: # Code For The html Mail

        '''
        ## <ins>***Parameters***</ins>
        ### Code: str = 265A74J74L (len = 10)

        ## <ins>***Returns***</ins>
        ### A Code Of The html Which Consists Of The Given 2FA-Code 
        ### <ins>***Return Type : str***</ins> * 
        '''

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

    def Send_Gmail(self) -> None:

        Email = EmailMessage()

        self.Code = Authorization_Code()
        HTML_DATA = self.html_Code(self.Code)

        Email['Subject'] = 'Two Factor Authentication Code'
        Email['From'] = 'Virati Akira Nandhan Reddy'
        Email['To'] = self.ReceiverMailAddress
        
        Email.set_content(HTML_DATA, subtype = 'html')

        
            
        try:

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as SMTP:

                SMTP.login(CREDENTIALS.get('User Name','None'), CREDENTIALS.get('Password','None'))
                SMTP.send_message(Email)

        except smtplib.SMTPAuthenticationError:
            
            pass

        except smtplib.SMTPServerDisconnected:

            pass


    def Resend_Gmail(self) -> None:
        self.Send_Gmail()


