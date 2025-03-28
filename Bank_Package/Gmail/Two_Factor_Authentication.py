import smtplib, time, datetime, socket
from email.message import EmailMessage
from . import SingleGmail, CREDENTIALS, HISTORY, Authorization_Code


class Two_Factor_Authentication(SingleGmail):
    
    '''
    # Two_Factor_Authentication Class Documentation

    ## <ins>***Overview***</ins>
    ### The `Two_Factor_Authentication` class is a child class of `SingleGmail` and is used to send Two-Factor Authentication (2FA) emails to a \
    given Gmail address. It generates a unique 2FA code, embeds it in an HTML email template, and sends the email to the specified recipient.

    ## <ins>***Attributes***</ins>
    ### `Code` : Stores the generated 2FA code. Default is None.

    ## <ins>***Methods***</ins>
    ### *1. html_Code(self, Code: str) -> str*
    > #### Generates the HTML content for the 2FA email with the provided 2FA code.
    ### *2. Send_Gmail(self) -> str*
    > #### Jekbrbkbfkbksbkkbkbkjbk
    '''

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

'''.replace('2FA-Code',Code)

    def Send_Gmail(self) -> str:

        Email = EmailMessage()

        self.Code = Authorization_Code()
        HTML_DATA = self.html_Code(self.Code)

        Email['Subject'] = 'Two Factor Authentication Code'
        Email['From'] = 'Virati Akira Nandhan Reddy'
        Email['To'] = self.ReceiverMailAddress
        
        Email.set_content(HTML_DATA, subtype = 'html')

                    
        try:

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as SMTP:

                SMTP.login(CREDENTIALS.get('Bank Email','None'), CREDENTIALS.get('Password','None'))
                SMTP.send_message(Email)

                HISTORY.write(f'\nTwo Factor Authentication Mail To {self.ReceiverMailAddress} At {datetime.datetime.now().strftime('%d/%b/%Y - %A @ %I:%M:%S %p')}  :  Status: Successful  :  Reason: Error Free')
                return 'Error Free'
            
        except smtplib.SMTPAuthenticationError:
            
            HISTORY.write(f'\nTwo Factor Authentication Mail To {self.ReceiverMailAddress} At {datetime.datetime.now().strftime('%d/%b/%Y - %A @ %I:%M:%S %p')}  :  Status: Unsuccessful  :  Reason: Credentials Error')
            return 'Credentials Error'

        except smtplib.SMTPServerDisconnected:

            HISTORY.write(f'\nTwo Factor Authentication Mail To {self.ReceiverMailAddress} At {datetime.datetime.now().strftime('%d/%b/%Y - %A @ %I:%M:%S %p')}  :  Status: Unsuccessful  :  Reason: Slow Internet')
            return 'Slow Internet'
        
        except socket.gaierror:

            HISTORY.write(f'\nTwo Factor Authentication Mail To {self.ReceiverMailAddress} At {datetime.datetime.now().strftime('%d/%b/%Y - %A @ %I:%M:%S %p')}  :  Status: Unsuccessful  :  Reason: No Internet')
            return 'No Internet'
        
        except Exception:

            HISTORY.write(f'\nTwo Factor Authentication Mail To {self.ReceiverMailAddress} At {datetime.datetime.now().strftime('%d/%b/%Y - %A @ %I:%M:%S %p')}  :  Status: Unsuccessful  :  Reason: Unknown Error')
            return 'Unknown Error'


    def Resend_Gmail(self) -> None:
        self.Send_Gmail()


