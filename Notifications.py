import smtplib
class Notification:

    def __init__(self, email):
        self.mail = email

    def send_mail(self):
        '''This function send to the user a mail with the detalis about the filight it found'''
        email = "cataliindumitru@gmail.com"
        password = "mnrbyiselqiuougb"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user= email, password= password)
            connection.sendmail(
                from_addr=email,
                to_addrs=self.mail,
                msg="Subject:Test\n\nThis is a test"
            )