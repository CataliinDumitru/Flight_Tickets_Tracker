from FlightSearch import FlightSearch
import json

test = FlightSearch()
test.get_token()
test.get_flight( "OTP", "IST", "2025-05-20", 1, "2025-05-25")
print(test.departures)

