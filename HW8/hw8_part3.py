# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 21:01:20 2022

@author: Nevin Joshy

This code grows the field and updates the status of the bears and tourists through 5 turns of the 
berryfield. it adds bears from the reservelist to the currentlist, and the same with tourists. It runs until there are no
 more bears on the field and no more bears in the reserve list; or if there are no more bears on the field and no more berries.
 It prints out the state of the simulation every 5 turns, and at the end of the simulation

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
        
    turns = 0#initializes a variable turns as 0, which is the counter for the while loop and the number of turns
    while not (len(currentbears)==0 and len(reservebears)==0) or (len(currentbears)==0 and berry.num==0):#run until there are no more bears on the field and no more bears in the reserve list; or if there are no more bears on the field and no more berries.
        turns+=1#increases turns by 1
        print()
        print("Turn: {}".format(turns))#prints the current number of turns
        
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
        
        if len(reservebears)>0 and berry.num>=500:#checks whether there are bears int he reservelist and 500 or more berries
            reservebears[0].added = True#marks the first reserve bear as added
            currentbears.append(reservebears[0])#adds the reserve bear to the currentbears
            reservebears.remove(reservebears[0])#removes the bear from reservebears
            
        if len(reservetours)>0 and len(currentbears)>0:#checks whther there are tourists in the reservelist and activebears
            reservetours[0].added = True#marks the first reserve tourist as added
            currenttours.append(reservetours[0])#adds the reserve tourist to the currenttours
            reservetours.remove(reservetours[0])#removes the tourist from reservetours
            
        for bear in currentbears:
            if bear.added:#checks if each bear is added
                print("Bear at ({},{}) moving {} - Entered the Field".format(bear.r, bear.c, bear.di))#if it is added, it prints that the bear has entered the field
                bear.added = False#changes added to false
                
        for tourist in currenttours:
            if tourist.added:#checks if each tourist is added
                print("Tourist at ({},{}), {} turns without seeing a bear. - Entered the Field".format(tourist.r,tourist.c,tourist.turn))#if it is added, it prints that the tourist has entered the field
                tourist.added=False#changes added to false
                
        berry = BerryField.BerryField(berry.berries,currentbears,currenttours)#reinitialises berry because currentbears and currenttours were changed
        
        if turns%5==0:#checks whter the turn is a multiple of 5
            print(berry)#prints the berrygrid by calling the string funtion
            
            #calls the string function of the bear class for each item in currentbears
            print("Active Bears:")
            for bear in currentbears:
                print(bear)
                
            
            
            #calls the string function of the tourist class for each item in currenttours
            print("\nActive Tourists:")
            for tourist in currenttours:
                print(tourist)
        print()
        
    #prints the final configuration
    print(berry)#prints the berrygrid by calling the string funtion
    
    #calls the string function of the bear class for each item in currentbears
    print("Active Bears:")
    for bear in currentbears:
        print(bear)
        
    
    #calls the string function of the tourist class for each item in currenttours
    print("\nActive Tourists:")
    for tourist in currenttours:
        print(tourist)
