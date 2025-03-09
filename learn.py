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

