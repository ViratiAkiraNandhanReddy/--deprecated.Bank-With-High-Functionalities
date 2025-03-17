'''
import smtplib
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
# start TLS for security
s.starttls()
# Authentication
s.login("viratiaki29@gmail.com", "hxwt wduo cnii pico")
# message to be sent
message = "I Have Sucessfully Sent The Mail <bold> This is a test mail </bold>"
# sending the mail
s.sendmail("viratiaki29@gmail.com", "viratiaki53@gmail.com", message)
# terminating the session
s.quit()

import webbrowser
# from . import 
web = webbrowser.open('www.google.com')
webbrowser.open_new('www.google.com')
webbrowser.WindowsDefault().open('www.google.com')'''
from Bank_Package.Bank_Mail import Two_Factor_Authentication
val = Two_Factor_Authentication('')._Code()
print(val)