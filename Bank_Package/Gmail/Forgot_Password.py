import smtplib, time
from email.message import EmailMessage
from . import SingleGmail, CREDENTIALS, Authorization_Code

class Forgot_Password(SingleGmail):
    
    Code = None

    def html_Code(self, Code: str) -> str: # Code For The html Mail
        
        ''' 
        ## <ins>***Parameters***</ins>
        ### Code: str = 265A74J74L (len = 10)

        ## <ins>***Returns***</ins>
        ### A Code Of The html Which Consists Of The Given Forgot Password Code
        ### <ins>***Return Type : str***</ins> * 
        '''

        return '''

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Forgot Password</title>
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
            background-color: #32CD32; 
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
            color: #32CD32; 
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
            color: #32CD32; 
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
            <h1>Forgot Password</h1>
        </div>
        <div class="content">
            <p>Dear User,</p>
            <p>We Received A Request To Reset Your Password. Please Use The Following Code To Reset Your Password:</p>
            <div class="code">Forgot-Password</div>
            <p>This Code is Valid For 10 Minutes. If You Did Not Request A Password Reset, Please ignore This Email.</p>
            <p>Thank You for Using Our Service.</p>
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

'''.replace('Forgot-Password', Code)

    def Send_Gmail(self) -> str:
        Email = EmailMessage()

        self.Code = Authorization_Code()
        HTML_DATA = self.html_Code(self.Code)

        Email['Subject'] = 'Forgot Password Request Code'
        Email['From'] = 'Virati Akira Nandhan Reddy'
        Email['To'] = self.ReceiverMailAddress
        
        Email.set_content(HTML_DATA, subtype = 'html')
    
        try:

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as SMTP:

                SMTP.login(CREDENTIALS.get('Bank Email','None'), CREDENTIALS.get('Password','None'))
                SMTP.send_message(Email)

        except smtplib.SMTPAuthenticationError:
            
            pass

        except smtplib.SMTPServerDisconnected:

            pass

    def Resend_Gmail(self) -> None:
        self.Send_Gmail()