import phonenumbers
from phonenumbers import geocoder
import folium

# for location of number (only country)
number = input("Enter phone number with country code: ")
check_number = phonenumbers.parse(number)
number_location = geocoder.description_for_number(check_number, "en")
print(number_location)

# for mobile carrier
from phonenumbers import carrier
service_provider = phonenumbers.parse(number)
print(carrier.name_for_number(service_provider, "en"))

# for finding the location coordinates
from opencage.geocoder import OpenCageGeocode
open_cage_geocoder = OpenCageGeocode("0ca2aced1d7541a9aab6b8fe1e053ca7")

query = str(number_location)
results = open_cage_geocoder.geocode(query)

# for latitude and longitude
lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']
print(lat, lng)

# for marking location on map
map_location = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=number_location).add_to(map_location)
map_location.save("mylocation.html")
