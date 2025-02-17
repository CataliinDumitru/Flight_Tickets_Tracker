import json
import requests
from Notifications import Notification


class FlightSearch:
    '''This class is going to take all the flights from the API and store them'''


    def __init__(self, email):
        self.email = Notification(email)
        self.track_flight = []
        self.departures = []
        self.returns = []
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



    def get_flight(self, departure, arrival, departure_date,adults, return_date=None):
        URL = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        headers = {"Authorization":f"Bearer {self.access_token}"}
        params = {
            "originLocationCode": departure,
            "destinationLocationCode": arrival,
            "departureDate": departure_date,
            "returnDate": return_date,
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

                        #The new_dict stores all the necessary data from the json and append it to the self.departure list
                        departure_dict = {
                            "Departure":element['itineraries'][0]["segments"][0]["departure"]["iataCode"],
                            "Arrival":element['itineraries'][0]["segments"][0]["arrival"]["iataCode"],
                             "Departure time":element['itineraries'][0]["segments"][0]["departure"]["at"],
                             "Arrival time":element['itineraries'][0]["segments"][0]["arrival"]["at"],
                             "Flight ID":[element['itineraries'][0]["segments"][0]["carrierCode"], element['itineraries'][0]["segments"][0]["number"]],
                             "Price": float(element['price']['total'])
                        }
                        self.departures.append(departure_dict)

                        returns_dict = {
                            "Departure": element['itineraries'][1]["segments"][0]["departure"]["iataCode"],
                            "Arrival": element['itineraries'][1]["segments"][0]["arrival"]["iataCode"],
                            "Departure time": element['itineraries'][1]["segments"][0]["departure"]["at"],
                            "Arrival time": element['itineraries'][1]["segments"][0]["arrival"]["at"],
                            "Flight ID": [element['itineraries'][1]["segments"][0]["carrierCode"],element['itineraries'][1]["segments"][0]["number"]],
                            "Price": float(element['price']['total'])
                        }
                        self.returns.append(returns_dict)

                        print(f'''\nFlight id: {element["id"]}
                            Departure from: {element['itineraries'][0]["segments"][0]["departure"]["iataCode"]}
                            Arrival to: {element['itineraries'][0]["segments"][0]["arrival"]["iataCode"]}
                            Departure time: {element['itineraries'][0]["segments"][0]["departure"]["at"]}
                            Arrival time: {element['itineraries'][0]["segments"][0]["arrival"]["at"]}
                            Flight ID: {element['itineraries'][0]["segments"][0]["carrierCode"]} {element['itineraries'][0]["segments"][0]["number"]}
                            
                            
                            Departure from: {element['itineraries'][1]["segments"][0]["departure"]["iataCode"]}
                            Arrival to: {element['itineraries'][1]["segments"][0]["arrival"]["iataCode"]}
                            Departure time: {element['itineraries'][1]["segments"][0]["departure"]["at"]}
                            Arrival time: {element['itineraries'][1]["segments"][0]["arrival"]["at"]}
                            Flight ID: {element['itineraries'][1]["segments"][0]["carrierCode"]} {element['itineraries'][1]["segments"][0]["number"]}
                            Price: {element['price']['total']}\n\n
''', end='-' * 50)
            else:
                print(f"Eroare la cererea GET: {response.status_code} - {response.text}")

        except requests.exceptions.RequestException as e:
            print(f"Eroare la cererea GET: {e}.")



    def budget_flight(self, param):
       budget = float(param)
       try:
           for departure, returns in zip(self.departures, self.returns):
               if 'Price' in departure and 'Price' in returns:
                   total_price = float(departure['Price']) + float(returns['Price'])
                   if total_price <= budget:
                       self.track_flight.append((departure, returns))
               else:
                   print("Key 'Price' not found in departure or returns dictionary.")

           self.email.send_mail(self.track_flight)
           print("An email was sent successfully.")

       except Exception as e:
           print(f"An error has occurred: {e}.")
           #TODO To solve list indices must be integers or slices, not str error