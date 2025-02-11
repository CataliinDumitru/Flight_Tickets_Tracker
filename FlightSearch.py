import json
import requests


class FlightSearch:
    '''This class is going to take all the flights from the API and store them'''


    def __init__(self):
        self.history = [] #It's going to gather all the history flight's
        self.departures = ""
        self.arrivals = ""
        self.access_token = {}


    def get_token(self):
        '''This method returns a authorization token than can be used for the API'''
        URL = "https://test.api.amadeus.com/v1/security/oauth2/token"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {
            "grant_type": "client_credentials",
            "client_id": "yFADAvQIUjGVfb2Qw7mOPm7CQJs5Js8Q",
            "client_secret": "Sji3NxqIlrkcprIb"
        }
        if self.access_token:
            print(self.access_token)
        else:
            response = requests.post(url=URL, data=data, headers=headers)
            self.access_token = response.json().get('access_token')
            print(self.access_token)


    def get_flight(self, token, departure, arrival, departure_date, adults):
        URL = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        headers = {"Authorization":f"Bearer {token}"}
        params = {
            "originLocationCode": departure,
            "destinationLocationCode": arrival,
            "departureDate": departure_date,
            "adults": adults,
        }
        try:
            response = requests.get(url=URL, headers=headers, params=params)
            if response.status_code == 200:
                print(json.dumps(response.json(), indent=4))
                #Am reusit sa afisez JSON-ul intr-un format citet, dar as vrea acum sa accesez cheile care ma intereseaza din el
                #TODO Show the relevant keys

            else:
                print(f"Eroare la cererea GET: {response.status_code} - {response.text}")

        except requests.exceptions.RequestException as e:
            print(f"Eroare la cererea GET: {e}.")
