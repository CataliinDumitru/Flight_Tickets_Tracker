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
        '''This method generate an authorization token that it's used to return the response from the server'''
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



    def get_flight(self, departure, arrival, departure_date, adults):
        URL = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        headers = {"Authorization":f"Bearer {self.access_token}"}
        params = {
            "originLocationCode": departure,
            "destinationLocationCode": arrival,
            "departureDate": departure_date,
            "adults": adults,
        }
        try:
            response = requests.get(url=URL, headers=headers, params=params)
            if response.status_code == 200:
                with open('data.json', 'w', encoding='utf-8') as file:
                    json.dump(response.json(), file, indent=4)
                    print("Data download successful")
                with open('data.json', 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    for next_id, element in enumerate(data['data']):
                        print(f'''\nFlight id: {element["id"]}\n
                        Departure from: {element['itineraries'][0]["segments"][0]["arrival"]["iataCode"]}\n
                        Arrival from: {element['itineraries'][0]["segments"][0]["departure"]["at"]}\n
                        Departure time: {element['itineraries'][0]["segments"][0]["departure"]["at"]}\n
                        Arrival time: {element['itineraries'][0]["segments"][0]["arrival"]["at"]}\n
                        Price: {element['price']['total']}\n''', end='-' * 50)
            else:
                print(f"Eroare la cererea GET: {response.status_code} - {response.text}")

        except requests.exceptions.RequestException as e:
            print(f"Eroare la cererea GET: {e}.")
            #TODO Sa idenfic numarul zborului dorit, sa fac o functie care sa-mi filtreze zbourile returnare si sa-mi trimita mail cu zborurile
            #gasite pana intr-un anumit pret