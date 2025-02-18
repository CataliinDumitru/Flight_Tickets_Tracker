FlightSearch Class

Overview

The FlightSearch class searches for flights using the Amadeus API, filters them based on a budget, and sends email notifications with the results.

Key Features

Retrieve Flights: Fetches flight data from the Amadeus API.
Filter by Budget: Finds flights within a user-defined budget.
Send Email: Sends flight details to the user via email.
Methods

1. __init__(self, email)

Initializes the class.
Sets up email notifications and empty lists for flight data.

2. get_token(self)

Generates an access token for the Amadeus API.
Stores the token for future requests.

3. get_flight(self, departure, arrival, departure_date, adults, return_date=None)

Fetches flight data from the API.
Saves flight details (departure and return) in self.departures and self.returns.
Prints flight details to the console.

4. budget_flight(self, param)

Filters flights based on the user's budget.
Stores matching flights in self.track_flight.
Sends an email with the filtered flight details.
Notification Class

Overview

Handles sending email notifications using Gmail's SMTP server.

Methods

1. send_mail(self, data)

Sends an email with flight details.
Constructs a message from the flight data and sends it to the user.
How It Works

Initialize FlightSearch with an email address.
Generate an API token using get_token.
Search for flights using get_flight.
Filter flights by budget with budget_flight.
Send flight details via email using send_mail.