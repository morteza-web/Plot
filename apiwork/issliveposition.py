import requests
import json

Iss_pos_api_url = "http://api.open-notify.org/iss-now.json"

geocode_location_url = "https://api.distancematrix.ai/maps/api/geocode/json?latlng="

key = "&key=BMy3DkHfQ0rjbbNtv5bWOV4OtmaUPbD2BUbby6WDZoFdtxAeZUlIiNPFVA6SA3Jo"





def get_Iss_position():

	response = requests.get(Iss_pos_api_url)
	data = response.json()

	if data["message"]=="success":
		lat = data["iss_position"]["latitude"]
		lon = data["iss_position"]["longitude"]
		print(f"The ISS position is {lat} latitude and {lon} longitude.")
		return(lat, lon)
	else:
		print('erorr')

def get_location():

	lat, lng = get_Iss_position()
	response = requests.get(geocode_location_url+lat+","+lng+key)

	data = response.json()

	#print(data["status"])
	if data["status"] == "OK":
		return(data)



def location_finder(data):

	adrr_cmp = data["result"][0]["address_components"]
	if adrr_cmp is None:
		print("its not over a known area...")
		return
	else:
		for i in adrr_cmp:
			if i["types"] == ["country"]:
				print(i["long_name"])
	#print(adrr_cmp)

Data = get_location()
location_finder(Data)
