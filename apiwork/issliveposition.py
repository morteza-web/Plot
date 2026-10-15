import requests
import json

Iss_pos_api_url = "http://api.open-notify.org/iss-now.json"

geocode_location_url = "https://api.distancematrix.ai/maps/api/geocode/json?latlng="

iswater_url = "https://api.isitwater.com/v1/locations/water?"

geocode_key = "&key=BMy3DkHfQ0rjbbNtv5bWOV4OtmaUPbD2BUbby6WDZoFdtxAeZUlIiNPFVA6SA3Jo"

iswater_key = "isw_KSwaaZ3A7EqPEU7thtXWdmfSA3ukwnPC8uyd"


class BearerAuth(requests.auth.AuthBase):
    def __init__(self, token):
        self.token = token
    def __call__(self, r):
        r.headers["authorization"] = "Bearer " + self.token
        return r


def get_Iss_position():

	response = requests.get(Iss_pos_api_url)
	data = response.json()

	

	if data["message"]=="success":
		lat = data["iss_position"]["latitude"]
		lon = data["iss_position"]["longitude"]
		#print(f"The ISS position is {lat} latitude and {lon} longitude.")
		return(lat, lon)
	else:
		print('erorr')

	

def Is_water():

	latitude, longitude = get_Iss_position()

	water_data = requests.get(iswater_url+"lat="+latitude+"&lon="+longitude, auth=BearerAuth(iswater_key))
	#print(type(water_data))
	data = water_data.json()
	#print(data)
	if data["water"] == True:
		print(data["features"])
		return
	elif data["water"] == False:
		loc = location_finder(get_location())
		print(loc)
		
def get_location():

	lat, lng = get_Iss_position()
	response = requests.get(geocode_location_url+lat+","+lng+geocode_key)

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


#Data = get_location()
#location_finder(Data)
Is_water()
