import smtplib
class Notification:

    def __init__(self, email):
        self.mail = email

    def send_mail(self, data):
        '''This function send to the user a mail with the detalis about the filight it found'''
        email = "cataliindumitru@gmail.com"
        password = "mnrbyiselqiuougb"

        if not data:
            print("No flights found to send via email.")
            return

        subject = "Flights Found"
        message = "We found the following flights for you:\n\n"

        for departure, returns in data:
            message += f"Departure Flight:\n"
            message += f"From: {departure['Departure']}\n"
            message += f"To: {departure['Arrival']}\n"
            message += f"Departure Time: {departure['Departure time']}\n"
            message += f"Arrival Time: {departure['Arrival time']}\n"
            message += f"Flight ID: {departure['Flight ID'][0]} {departure['Flight ID'][1]}\n"

            message += f"Return Flight:\n"
            message += f"From: {returns['Departure']}\n"
            message += f"To: {returns['Arrival']}\n"
            message += f"Departure Time: {returns['Departure time']}\n"
            message += f"Arrival Time: {returns['Arrival time']}\n"
            message += f"Flight ID: {returns['Flight ID'][0]} {returns['Flight ID'][1]}\n"
            message += f"Price: {returns['Price']}\n\n"
            message += "-" * 45 + "\n\n"

        try:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=email, password=password)
                connection.sendmail(
                    from_addr=email,
                    to_addrs=self.mail,
                    msg=f"Subject: {subject}\n\n{message}"
                )
            print("Email sent successfully.")
        except Exception as e:
            print(f"Failed to send email: {e}")