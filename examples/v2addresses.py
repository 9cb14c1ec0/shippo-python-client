import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
import shippo

api_key = '<API-KEY-HERE>'

#print(shippo.V2Addresses.retrieve(object_id='1e5ba7a7870b4fc7a49b79657b2566d7', api_key=api_key))
#print(shippo.V2Addresses.all(api_key=api_key, limit=20))
#print(shippo.V2Addresses.create(api_key=api_key, name="Shippo", address_line_1="731 Market Street",
#                                city_locality="San Francisco", state_province="CA", postal_code="94103", country_code="US"))
#print(shippo.V2Addresses.update(object_id='1e5ba7a7870b4fc7a49b79657b2566d7', api_key=api_key, name="Shippo",
#                                address_line_1="731 Market Street", address_line_2="#200",
#                                city_locality="San Francisco", state_province="CA", postal_code="94103", country_code="US"))
print(shippo.V2Addresses.parse(address_string='11605 W Belleview Ave, Littleton, Colorado, 80127, US', api_key=api_key))