import requests

geocode_location_url = "https://api.distancematrix.ai/maps/api/geocode/json?latlng="

key = "&key=BMy3DkHfQ0rjbbNtv5bWOV4OtmaUPbD2BUbby6WDZoFdtxAeZUlIiNPFVA6SA3Jo"



def get_location():

	lat = "36.383346"
	lng = "-115.221788"
	response = requests.get(geocode_location_url+lat+","+lng+key)

	data = response.json()

	print(data["status"])
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
	print(type(adrr_cmp))

Data = get_location()
location_finder(Data)

