import smtplib
class GmailSender:
    def __init__(self):
        pass

    def send(self, sender_email, sender_app_password, recipient_email, subject, message_to_send):
        """send a email to someone"""
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(
                user=sender_email,
                password= sender_app_password,
            )
            
            connection.sendmail(
                from_addr= sender_email,
                to_addrs= recipient_email,
                msg=f"Subject:{subject}\n\n{message_to_send}"
            )
            print(f'MAIL sent Succesfully to "{recipient_email}"')
        