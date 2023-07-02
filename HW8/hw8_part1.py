# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 21:01:20 2022

@author: Nevin Joshy

This code takes an input file and prints the berryfield and all of the active bears and tourists
in the starting configuration
"""

#import statements to read json file, import berryfield, bear, and tourist classes
import json
import BerryField
import Bear
import Tourist

if __name__ == "__main__":#main code
        
    #input statement to recieve name of json file
    file = input("Enter the json file name for the simulation => ").strip()
    print(file)
    
    #reads the file and names it data
    f = open(file)
    data = json.loads(f.read())
    
    #creates a list of bear objects from each bear in data[active_bears] called currentbears
    currentbears=[]
    for bear in data["active_bears"]:
        currentbears.append(Bear.Bear(bear[0],bear[1],bear[2]))
        
    #creates a list of tourist objects from each bear in data[active_tourists] called currenttours
    currenttours=[]
    for tour in data["active_tourists"]:
        currenttours.append(Tourist.Tourist(tour[0],tour[1],len(data["berry_field"])))
        
    #initializes a berryfield called berry, which takes a grid, list of bears, and list of tourists as an input
    #then, the string function of the berrygrid is called by print(berry)
    print()
    berry = BerryField.BerryField(data["berry_field"],currentbears,currenttours)
    print(berry)
    
    #calls the string function of the bear class for each item in currentbears
    print("Active Bears:")
    for bear in currentbears:
        print(bear)
        
    #calls the string function of the tourist class for each item in currenttours
    print("\nActive Tourists:")
    for tourist in currenttours:
        print(tourist)