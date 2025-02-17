from FlightSearch import FlightSearch
import json

test = FlightSearch("d.catalin99@yahoo.com")
test.get_token()
test.get_flight( "OTP", "IST", "2025-05-20", 1, "2025-05-25")
test.budget_flight(300)
print(test.departures)