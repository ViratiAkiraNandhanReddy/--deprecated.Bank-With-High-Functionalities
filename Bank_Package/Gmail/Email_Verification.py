import smtplib, time
from email.message import EmailMessage
from . import SingleGmail, CREDENTIALS, Authorization_Code

class EmailVerification(SingleGmail):
    
    Code = None
    
    # Changes The html Code With The Given Email Verification Code
    def html_Code(self, Code: str) -> str: # Code For The html Mail

        '''
        ## <ins>***Parameters***</ins>
        ### Code: str = 265A74J74L (len = 10)

        ## <ins>***Returns***</ins>
        ### A Code Of The html Which Consists Of The Given Email Verification Code
        ### <ins>***Return Type : str***</ins> * 
        '''

        return '''

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Email Verification</title>
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
            background-color: #ff6600;
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
            color: #ff6600;
            text-align: center;
            margin: 20px 0;
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
        .footer a {
            color: #ff6600;
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
            <h1>Email Verification</h1>
        </div>
        <div class="content">
            <p>Dear User,</p>
            <p>To Verify Your Email Address, Please Use The Following Verification Code:</p>
            <div class="code">Email-Verification</div>
            <p>This Code is Valid For 10 Minutes. If You Did Not Request This Verification, Please Ignore This Email.</p>
            <p>Thank You For Using Our Service.</p>
            <p>Best Regards,</p>
            <p><b>Virati Akira Nandhan Reddy</b></p>
        </div>
        <div class="footer">
            <p>&copy; 2026 Virati Akira Nandhan Reddy. All Rights Reserved.</p>
            <p><a href="https://github.com/ViratiAkiraNandhanReddy">GitHub</a> | <a href="https://linkedin.com/in/virati-akira-nandhan-reddy">LinkedIn</a> | <a href="https://x.com/Viratiaki53">Twitter</a> | <a href="https://instagram.com/Viratiaki53">Instagram</a></p>
            <p><b> This is An Automated Email </b></p> 
            <p><b> Please Do Not Reply To This Email </b></p>
        </div>
    </div>
</body>
</html>

'''.replace('Email-Verification', Code)

    def Send_Gmail(self) ->None:
        
        Email = EmailMessage()
            
        self.Code = Authorization_Code()
        HTML_DATA = self.html_Code(self.Code)

        Email['Subject'] = 'Email Verification'
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