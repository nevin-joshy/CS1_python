# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 21:01:20 2022

@author: Nevin Joshy

This code grows the field and updates the status of the bears and tourists through 5 turns of the 
berryfield. it prints out the state of the simulation at each turn.
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
    print("")
    
    #reads the file and names it data
    f = open(file)
    data = json.loads(f.read())
    
    #creates a list of bear objects from each bear in data[active_bears] called currentbears
    currentbears=[]
    for bear in data["active_bears"]:
        currentbears.append(Bear.Bear(bear[0],bear[1],bear[2]))
        
    #creates a list of bear objects from each bear in data[reserve_bears] called reservebears
    reservebears=[]
    for bear in data["reserve_bears"]:
        reservebears.append(Bear.Bear(bear[0],bear[1],bear[2]))
        
    #creates a list of tourist objects from each bear in data[active_tourists] called currenttours
    currenttours=[]
    for tour in data["active_tourists"]:
        currenttours.append(Tourist.Tourist(tour[0],tour[1],len(data["berry_field"])))
        
    #creates a list of tourist objects from each tourist in data[reserve_tourists] called reservetours
    reservetours=[]
    for tour in data["reserve_tourists"]:
        reservetours.append(Tourist.Tourist(tour[0],tour[1],len(data["berry_field"])))
        
    #prints starting config by initializing a berryfield called berry, which takes a grid, list of bears, and 
    #list of tourists as an input. then, the string function of the berrygrid is called by print(berry)
    print("Starting Configuration")
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
        
    #initializes a variable i as 1, which is the counter for the while loop and the number of turns
    turns = 1
    while turns<6:#will only go through 5 turns
        print()
        print("Turn: {}".format(turns))#prints out the current turn number at the beginning of each turn
        berry.growfield()#calls the growfield function of berryfield, which grows all the berries according to their neighbors
        for bear in currentbears:
            bear.move(berry.berries,currenttours)#iterates through each bear in the currentbears and moves them using the move function of bear, which takes in a berrygrid and the list of tourists
            
        bearcopy = currentbears.copy()#makes a copy of the currentbears to remove from
        for bear in currentbears:
            if not bear.inbounds:#checks if each bear is inbounds or not(self function of bear)
                print("Bear at ({},{}) moving {} - Left the Field".format(bear.r, bear.c, bear.di))#if the bear is out of bounds, prints that it has left the field
                bearcopy.remove(bear)#after printing, the bear is removed from the copied list
        currentbears = bearcopy#currentbears is updated to bearcopy, so the properbears are removed
        
        for tour in currenttours:
            tour.tourcheck(currentbears)#runs tourcheck for each tourist, which updates its status whether it can see 3 bears, cant see a bear, or is with a bear
            
        tourcopy = currenttours.copy()#makes a copy of the currenttours to remove from
        for tourist in currenttours:
            if not tourist.isalive:#checks whether tourist is alive
                print("Tourist at ({},{}), {} turns without seeing a bear. - Left the Field".format(tourist.r,tourist.c,tourist.turn))#if the tourist is not alive(left the field due to not seeing, seeing to many, or being with a bear), it prints that it has left the field
                tourcopy.remove(tourist)#removes the tourist from the copied list
        currenttours = tourcopy#currenttours is updated to tourcopy, so the proper tourists are removed
        
        berry = BerryField.BerryField(berry.berries,currentbears,currenttours)#reinitializes berry because currentbears,currenttours were updated
        print(berry)#calls the string fuction of the berryfield object to print out the berryfield
        
        #calls the string function of the bear class for each item in currentbears
        print("Active Bears:")
        for bear in currentbears:
            print(bear)
        print()
        
        #calls the string function of the tourist class for each item in currenttours
        print("Active Tourists:")
        for tourist in currenttours:
            print(tourist)
        print()
        
        turns+=1#increases the turns by 1
