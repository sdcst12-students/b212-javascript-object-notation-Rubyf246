#Task 3
#Use the Weather API builder at https://open-meteo.com/en/docs to generate an API call for a city.
# We are going to make use of the REQUESTS.Request method to retrieve this data and unpack it with json.
# loads into a variable that we can use. Retrieve the data and present it in a more organized format. 
# You may use text output or a window using Tkinter.  Our goal is to format the result in a reasonably organized format.

# RF: reference: https://cran.r-project.org/web/packages/openmeteo/openmeteo.pdf
 

import requests
import json
 
url = "https://api.open-meteo.com/v1/forecast"
params = {
	"latitude": 49.2497,  #vancouver
	"longitude": -123.1193,
	"hourly": "temperature_2m",
	"timezone": "Pacific/Auckland",
	"models": "gem_seamless"
}
response = requests.get(url, params)


response_dict = json.loads(response.text)

#print(f"response_dict is a variable of type {type(response_dict)} and contains {response_dict}")

hourly =  response_dict["hourly"] # hourly is an item of response_dict, and hourly is a dict itself, which contain two dictionary
#print(f"hourly is a variable of type {type(hourly)} and contains {hourly}")

hourly_time_list = hourly["time"] #time is an item of hourly, which is a dictionary, of which value is a list
hourly_temp_2m_list = hourly["temperature_2m"] #temperature_2m is also a list


latitude = str(response_dict["latitude"])
longitude =  str(response_dict["longitude"])
timezone = str(response_dict["timezone_abbreviation"])
elevation = str(response_dict["elevation"])
time_dic = response_dict["hourly_units"] 
timeformat = str(time_dic["time"])
tempunit = str(time_dic["temperature_2m"])

 
print("Temperature Forcast of City of Vancouver, British Columbia, Canada")
print("------------------------------------------------------------------")
print(f"latitude:  {latitude.rjust(15)} ")
print(f"longitude:  {longitude.rjust(15)} ")
print(f"timezone:  {timezone.rjust(15)} ")
print(f"elevation:  {elevation.rjust(15)} ")
print(f"timeformat:  {timeformat.rjust(15)} ")
print(f"tempunit:  {tempunit.rjust(15)} ")
print(f"temperature forcast:")
 
n = len(hourly_time_list)
 
#iterate the two lists of time and temperature 
for i in range(n):
    print("\t" + hourly_time_list[i] + ":\t" + str(hourly_temp_2m_list[i]) + tempunit )
 
 
    
 