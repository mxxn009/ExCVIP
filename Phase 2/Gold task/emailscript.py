import yagmail
import schedule
import time
from datetime import datetime, timedelta


def email_script():
    sender_email = input("Enter your email address: ")
    #senders password requires you to input your application specific password generated and given to you by google itself
    sender_password = input("Enter your Application-Specific-Passsword: ")
    receiver_email = input('Enter Recievers Email Address: ')
    y = yagmail.SMTP(sender_email, sender_password)
    subject = input('Enter Subject: ')
    body = input('Enter Body: ')
    alias = receiver_email
    to = alias
    img_req = input('Would you like to send attachment? Y/N: ')
    if img_req == 'Y' or img_req == 'y':
        path = input('Enter path to attachment: ')
        with open(path, 'rb') as f:
            y.send(to, subject, body, attachments =f)
    elif img_req == 'N' or img_req == 'n':
        y.send(to, subject, body)

    print("Email Sent")


s = input('Would you like to schedule this email? (y/n): ')
if s == 'y':
    a = int(input('Enter time (HH:MM):\t'))
    schedule.every().day.at(a).do(email_script)

    start_date = datetime.now()
    ss = int(input('For how many days?:\t'))
    end_date = start_date + timedelta(days=ss)

    while end_date < datetime.now():
        schedule.run_pending()
        time.sleep(1)
if s == 'n':
    pass


email_script()
