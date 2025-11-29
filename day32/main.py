import smtplib

my_eamil = "awakiyang9@gmail.com"
password = "jtry lvtb oaog qckl"

proceed = True
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(user=my_eamil, password=password)

    subject = 'Grab dinner bro'
    body= 'How you doing'

    message = f'Subject: {subject}\n\n {body}'
    smtp.sendmail(from_addr= my_eamil, to_addrs= 'awakiyang4@gmail.com', msg=message)  