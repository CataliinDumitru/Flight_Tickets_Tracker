from FlightSearch import FlightSearch
import json

test = FlightSearch()
test.get_token()
all_data = test.get_flight( "OTP", "IST", "2025-04-20", 1)

