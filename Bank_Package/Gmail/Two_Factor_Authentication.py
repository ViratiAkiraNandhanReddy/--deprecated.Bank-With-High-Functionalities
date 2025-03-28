'''
# *Two_Factor_Authentication Module <ins>Documentation</ins>*

## <ins>***Overview***</ins>
> ### The `Two_Factor_Authentication` module is designed to send Two-Factor Authentication (2FA) emails to a recipient's Gmail address. It ensures secure \
communication by generating a unique 2FA code and embedding it in an HTML email template. The module also provides functionality to validate the code and \
ensures it expires after 10 minutes.

## <ins>***Features***</ins>
> ### 1. `Send 2FA Emails` : Sends a 2FA email with a unique code to the recipient.
> ### 2. `Code Validation` : Validates the input code against the generated code.
> ### 3. `Code Expiry` : Ensures the code is valid only for 10 minutes.
> ### 4. `Error Handling` : Handles errors like invalid credentials, no internet, and server disconnection.
> ### 5. `Logging` : Logs email sending status and validation attempts for tracking purposes.

## <ins>***Key Methods***</ins>
### 1. Send_Gmail()
> #### Sends the 2FA email to the recipient's Gmail address.

### 2. Validate_Code(input_code: str) -> bool
> #### Validates the input code. Returns True if the code matches and is within 10 minutes of generation, otherwise False.

### 3. Resend_Gmail()
> #### Resends a new 2FA email by generating a new code.

## <ins>***Example Usage***</ins>
> ### 1. <ins>***Sending a 2FA Email***</ins>
```
from Two_Factor_Authentication import Two_Factor_Authentication

# Create an instance of the Two_Factor_Authentication class
two_fa = Two_Factor_Authentication("example@gmail.com")

# Send the 2FA email
status = two_fa.Send_Gmail()
print(f"Email Sending Status: {status}")
```

> ### 2. <ins>***Validating a Code***</ins>
```
# Validate the input code
user_input = input("Enter the 2FA code: ")
if two_fa.Validate_Code(user_input):
    print("Code is valid!")
else:
    print("Code is invalid or expired.")
```

## <ins>***Dependencies***</ins>
> ### 1. `smtplib` : For sending emails using SMTP protocol.
> ### 2. `datetime` : For handling date and time operations.
> ### 3. `socket` : For handling network-related errors.
> ### 4. `email.message` : For creating email messages.
> ### 5. Relative imports from __init__.py : For importing necessary modules and Parent Class.

## <ins>***Notes***</ins>
> * ### The 2FA code is valid for 10 minutes.
> * ### Ensure the CREDENTIALS and HISTORY modules are properly configured.
> * ### This module is designed to send emails to a single recipient at a time.
'''
import smtplib, datetime, socket
from email.message import EmailMessage
from . import SingleGmail, CREDENTIALS, HISTORY, Authorization_Code

class Two_Factor_Authentication(SingleGmail):

    '''
    # *Two_Factor_Authentication Class <ins>Documentation</ins>*

    ---
    ## <ins>***Overview***</ins>

    > ### The `Two_Factor_Authentication` class is a child class of `SingleGmail` and is used to send Two Factor Authentication (2FA) emails to a \
    given Gmail address. It generates a unique 2FA code, embeds it in an HTML email template, and sends the email to the specified recipient.
    
    ## <ins>***Attributes***</ins>

    > ### `Code` : Stores the generated 2FA code. Default is None.
    > ### `Timestamp` : Stores the generatation Time Of 2FA code. Default is None.

    ## <ins>***Methods***</ins>

    ### *1. html_Code(self, Code: str) -> str*
    > #### Generates the HTML content for the 2FA email with the provided 2FA code.
    > ### <ins>***Parameters***</ins>
    > #### `Code (str)` : The 2FA code to be embedded in the email. Example: "265A74J74L".
    > ### <ins>***Returns***</ins>
    > #### `str` : The HTML content of the email with the embedded 2FA code.

    ### *2. Send_Gmail(self) -> str*
    > #### Sends the 2FA email to the recipient's Gmail address.
    > ### <ins>***Workflow***</ins>
    > #### 1. Generates a unique 2FA code using the Authorization_Code() function.
    > #### 2. Embeds the code in the HTML email template using the html_Code() method.
    > #### 3. Sends the email using the smtplib library.
    > #### 4. Logs the email sending status in the HISTORY file.
    > ### <ins>***Returns***</ins>
    > #### `str` : A status message indicating the result of the email sending process:
    >> #### "Error Free": Email sent successfully.
    >> #### "Credentials Error": Incorrect email credentials.
    >> #### "Slow Internet": SMTP server disconnected due to slow internet.
    >> #### "No Internet": No internet connection.
    >> #### "Unknown Error": An unexpected error occurred.

    ### 3. *Resend_Gmail(self) -> None*
    > #### Resends the 2FA email by calling the Send_Gmail() method.

    ## <ins>***Example Usage***</ins>
    > ### <ins>***Sending a 2FA Email***</ins>
    ```
    from Two_Factor_Authentication import Two_Factor_Authentication

    # Create an instance of the Two_Factor_Authentication class
    Two_Factor_Auth = Two_Factor_Authentication("example@gmail.com")

    # Send the 2FA email
    status = Two_Factor_Auth.Send_Gmail()
    print(f"Email Sending Status: {status}")
    ```

    ## <ins>***Error Handling***</ins>
    > ### The Send_Gmail() method handles the following errors:
    >> #### `SMTPAuthenticationError` : Occurs when the email credentials are incorrect.
    >> #### `SMTPServerDisconnected` : Occurs when the SMTP server disconnects due to slow internet.
    >> #### `socket.gaierror` : Occurs when there is no internet connection.
    >> #### `Exception` : Catches any other unexpected errors.

    ## <ins>***Logging***</ins>
    > ### The Send_Gmail() method logs the email sending status in the HISTORY file with the following details:
    >> #### 1. Recipient's email address
    >> #### 2. Timestamp
    >> #### 3. Status (Successful or Unsuccessful)
    >> #### 4. Reason for failure (if any)

    ## <ins>***Notes***</ins>
    > * ### The 2FA code is valid for 10 minutes.
    > * ### This class is designed to send emails to a single recipient at a time.
    > * ### Ensure that the CREDENTIALS and HISTORY modules are properly configured before using this class.
    > * ### This documentation provides a comprehensive overview of the Two_Factor_Authentication class, its methods, and usage examples.
    '''

    Code = None # Store the generated 2FA code
    Timestamp = None  # Store the timestamp when the code is generated

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
        self.Timestamp = datetime.datetime.now()  # Store the current timestamp
        HTML_DATA = self.html_Code(self.Code)

        Email['Subject'] = 'Two Factor Authentication Code'
        Email['From'] = 'Virati Akira Nandhan Reddy'
        Email['To'] = self.ReceiverMailAddress
        
        Email.set_content(HTML_DATA, subtype = 'html')

                    
        try: # Error Free

            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as SMTP:

                SMTP.login(CREDENTIALS.get('Bank Email','None'), CREDENTIALS.get('Password','None'))
                SMTP.send_message(Email)

                HISTORY.write(f'\nTwo Factor Authentication Mail To {self.ReceiverMailAddress} At {datetime.datetime.now().strftime('%d/%b/%Y - %A @ %I:%M:%S %p')}  :  Status: Successful  :  Reason: Error Free')
                return 'Error Free'
            
        except smtplib.SMTPAuthenticationError: # Credentials Error 
            
            HISTORY.write(f'\nTwo Factor Authentication Mail To {self.ReceiverMailAddress} At {datetime.datetime.now().strftime('%d/%b/%Y - %A @ %I:%M:%S %p')}  :  Status: Unsuccessful  :  Reason: Credentials Error')
            return 'Credentials Error'

        except smtplib.SMTPServerDisconnected: # Slow Internet 

            HISTORY.write(f'\nTwo Factor Authentication Mail To {self.ReceiverMailAddress} At {datetime.datetime.now().strftime('%d/%b/%Y - %A @ %I:%M:%S %p')}  :  Status: Unsuccessful  :  Reason: Slow Internet')
            return 'Slow Internet'
        
        except socket.gaierror: # No Internet 

            HISTORY.write(f'\nTwo Factor Authentication Mail To {self.ReceiverMailAddress} At {datetime.datetime.now().strftime('%d/%b/%Y - %A @ %I:%M:%S %p')}  :  Status: Unsuccessful  :  Reason: No Internet')
            return 'No Internet'
        
        except Exception: # Unknown Error 

            HISTORY.write(f'\nTwo Factor Authentication Mail To {self.ReceiverMailAddress} At {datetime.datetime.now().strftime('%d/%b/%Y - %A @ %I:%M:%S %p')}  :  Status: Unsuccessful  :  Reason: Unknown Error')
            return 'Unknown Error'

    def Validate_Code(self, input_code: str) -> bool:
        """ 
        Validates the input code against the generated code.
        The code is valid only if it matches and is within 10 minutes of generation.
        """
        if self.Code is None or self.Timestamp is None:
            return False  # No code generated yet

        Time_Elapsed = (datetime.datetime.now() - self.Timestamp).total_seconds()
        if Time_Elapsed > 600:  # 10 minutes
            return False  # Code expired

        return input_code == self.Code

    def Resend_Gmail(self) -> None:
        '''
        #### Resends The New 2FA Email By Calling The Send_Gmail() Method And New 2FA Code Will Be Generated 
        '''
        self.Send_Gmail()


