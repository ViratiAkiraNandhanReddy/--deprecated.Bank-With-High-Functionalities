import smtplib
from email.message import EmailMessage
from . import SingleGmail, CREDENTIALS

class WelcomeGreetings(SingleGmail):

    def __init__(self, ReceiverMailAddress: str, Username: str) -> None:
        super().__init__(ReceiverMailAddress)
        self.Username = Username

    # Changes The html Code With The Given Username
    def html_Code(self, Username: str) -> str: # Code For The html Mail
        
        '''
        ## <ins>***Parameters***</ins>
        ### Username: str = `"Virati Akira Nandhan Reddy"`
        ## <ins>***Returns***</ins>
        ### A Code Of The html Which Consists Of The Given Username
        '''

        return '''

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to Our Service</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
        body {
            font-family: 'Roboto', sans-serif;
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
            background-color: #4CAF50; /* Green color */
            color: #ffffff;
        }
        .header h1 {
            margin: 0;
            font-size: 24px;
        }
        .content {
            padding: 20px;
            text-align: center;
        }
        .content img {
            max-width: 100%;
            height: auto;
            margin-bottom: 20px;
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
            color: #4CAF50; /* Green color */
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
            <h1>Welcome to Our Service, USERNAME!</h1>
        </div>
        <div class="content">
            <img src="https://github.com/ViratiAkiraNandhanReddy/Bank-With-High-Functionalities/blob/0d0b232404b94a6306a87b89615c34609deaf46d/Bank_Package/Visual%20Data/Welcome%20Image.png?raw=true" alt="Welcome Image">
            <p>Dear <i><b>USERNAME</b></i>,</p>
            <p>We Are Thrilled To Have You With Us. Thank You For Joining Our Service!</p>
            <p>We Are Committed To Providing You With The Best Experience Possible. If You Have Any Questions Or Need Assistance, Please Do Not Hesitate To Reach Out To Our Support Team.</p>
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

'''.replace('USERNAME', Username)

    def Send_Gmail(self) -> None:

        Email = EmailMessage()

        HTML_DATA = self.html_Code(self.Username)

        Email['Subject'] = 'Welcome to Our Service'
        Email['From'] = 'Virati Akira Nandhan Reddy'
        Email['To'] = self.ReceiverMailAddress

        Email.set_content(HTML_DATA, subtype='html')

        try:

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as SMTP:

                SMTP.login(CREDENTIALS.get('User Name', 'None'), CREDENTIALS.get('Password', 'None'))
                SMTP.send_message(Email)

        except smtplib.SMTPAuthenticationError:

            pass

        except smtplib.SMTPServerDisconnected:

            pass

    
    def Resend_Gmail(self) -> None:
        self.Send_Gmail()
    