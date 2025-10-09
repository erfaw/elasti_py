import subprocess as sp; sp.call('cls', shell=True)
import smtplib

my_email = ''
password = '' 

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls() # Secure with encryption
    connection.login(user=my_email, password= password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs='moperfarish@gmail.com',
        msg='Subject:HEllo bitch2\n\nThis is a fucking test2'
        )
