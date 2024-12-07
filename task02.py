#!python3
import requests
import json

# we can use requests to retrieve json encoded data from the internet
# there are different methods that we can retrieve the data with: POST and GET
# You can google the difference between POST and GET requests

req = requests.get('http://sdcaf.hungrybeagle.com/menu.php') # go to internet to get info
data = req.text #data is str 

# Use the json encoded data that is retrieved from this website and print out the weekly menu
# You will need to decipher the json decoded data to determine what information the 
# dictionary object contains

decoded = json.loads(data) # decoded is a dictionary
print(f"decoded is a variable of type {type(decoded)} and contains {decoded}")

print ("----------------------------------")
json_formatted_str = json.dumps(decoded, indent=4) # convert json(essentially a dictionary) into a string
print(json_formatted_str)
 