from datetime import datetime
import random
import smtplib
import os

today = datetime.now()
weekday = today.weekday()
day = today.day
year = today.year                 
hour = today.hour                 
minute = today.minute             
second = today.second
timestamp = today.timestamp()

if weekday == 3:  #initialization code to exucute if weekday is thursday
    '''
    #======================== opening file to access qoutes =============#
    '''
    with open("quotes.txt") as qoute_file:
        all_qoutes = qoute_file.readlines()
        qoute = random.choice(all_qoutes)

    '''
    #===================== Sending motivational qoute ====================#
    '''

    my_eamil = "awakiyang9@gmail.com"
    password = os.getenv("email_password") 

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(user=my_eamil, password=password)

        subject = 'Morning motivation'
        body= qoute

        message = f'Subject: {subject}\n\n {body}'
        smtp.sendmail(from_addr= my_eamil, to_addrs= 'awakiyang4@gmail.com', msg=message)  
        