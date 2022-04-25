import smtplib
import getpass
server = smtplib.SMTP('smtp.gmail.com' , 587)
isConnected = server.ehlo()
server.starttls()
print(isConnected)

email = input("Enter your Email : ")
password = getpass.getpass("Enter your password : ")

print(server.login(email, password))

from_address = email
to_address = input("Email to (enter mail id) : ")

subject = input("Enter your subject : ")
message = input("Enter your message : ")

send_msg  = "Subject: " + subject + '\n' + message

print(server.sendmail(from_address, to_address, send_msg))

