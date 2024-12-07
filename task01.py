#!python3
# Read the contents of a file that has a json encoded list of numbers.
# Find the largest number in each list
# task02a: 63545
# task02b: 63876
# task02c: 63892

import json

def find_sum():
    datatask2 = 'task01a.txt'
    data2 = open(datatask2,'r')
    str2 = data2.read()
    decoded2 = json.loads(str2)
    #print(f"decodedNumbers is a variable of type {type(decoded2)} and contains {decoded2}")
    print(max(decoded2))
    
    datatask2 = 'task01b.txt'
    data2 = open(datatask2,'r')
    str2 = data2.read()
    decoded2 = json.loads(str2)
    #print(f"decodedNumbers is a variable of type {type(decoded2)} and contains {decoded2}")
    print(max(decoded2))
    
    datatask3 = 'task01c.txt'
    data3 = open(datatask3,'r')
    str3 = data3.read()
    decoded3 = json.loads(str3)
    #print(f"decodedNumbers is a variable of type {type(decoded2)} and contains {decoded2}")
    print(max(decoded3))
    

if __name__ == "__main__":
    find_sum()    