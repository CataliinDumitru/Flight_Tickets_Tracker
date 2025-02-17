import smtplib
class Notification:

    def __init__(self, email):
        self.mail = email

    def send_mail(self, data):
        '''This function send to the user a mail with the detalis about the filight it found'''
        email = "cataliindumitru@gmail.com"
        password = "mnrbyiselqiuougb"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user= email, password= password)
            connection.sendmail(
                from_addr=email,
                to_addrs=self.mail,
                msg=f'''Subject:Flights from {data['Departure']} to {data['Arrival']}\n\n
                We found {len(data)} flights for {data['Departure']} to {data['Arrival']}.
                Departure from: {data['Departure']}
                Arrival to: {data['Arrival']}
                Departure time: {data['Departure time']}
                Arrival time: {data['Arrival time']}
                Flight ID: {data['Flight ID']}
                Price: {data['Price']}\n\n
'''
            )