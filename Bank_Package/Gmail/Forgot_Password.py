import smtplib, time
from email.message import EmailMessage
from . import SingleGmail, CREDENTIALS, Authorization_Code

class Forgot_Password(SingleGmail):
    
    Code = None

    def html_Code(self, Code: str) -> str: # Code For The html Mail
        return ''

    def Send_Gmail(self) -> None:
        Email = EmailMessage()

        self.Code = Authorization_Code()
        HTML_DATA = self.html_Code(self.Code)

        Email['Subject'] = 'Forgot Password Request Authentication Code'
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
        return super().Resend_Gmail()