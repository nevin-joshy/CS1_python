# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 21:01:20 2022

@author: Nevin Joshy
"""

import json
import BerryField
import Bear
import Tourist

file = input("Enter the json file name for the simulation => ").strip()
print(file)
print("")

f = open(file)
data = json.loads(f.read())

currentbears=[]
for bear in data["active_bears"]:
    currentbears.append(Bear.Bear(bear[0],bear[1],bear[2]))
    
reservebears=[]
for bear in data["reserve_bears"]:
    reservebears.append(Bear.Bear(bear[0],bear[1],bear[2]))
    
currenttours=[]
for tour in data["active_tourists"]:
    currenttours.append(Tourist.Tourist(tour[0],tour[1],len(data["berry_field"])))
    
reservetours=[]
for tour in data["reserve_tourists"]:
    reservetours.append(Tourist.Tourist(tour[0],tour[1],len(data["berry_field"])))
    
print("Starting Configuration")
berry = BerryField.BerryField(data["berry_field"],currentbears,currenttours)
print(berry)

print("Active Bears:")
for bear in currentbears:
    print(bear)

print("\nActive Tourists:")
for tourist in currenttours:
    print(tourist)
    
turns = 1
while turns<3:
    print()
    print("Turn: {}".format(turns))
    berry.growfield()
    for bear in currentbears:
        bear.move(berry.berries,currenttours)
    bearcopy = currentbears.copy()
    bearcopy = currentbears.copy()
    for bear in currentbears:
        if not bear.inbounds:
            print("Bear at ({},{}) moving {} - Left the Field".format(bear.r, bear.c, bear.di))
            bearcopy.remove(bear)
    currentbears = bearcopy
    for tour in currenttours:
        tour.tourcheck(currentbears)
    tourcopy = currenttours.copy()
    for tourist in currenttours:
        if not tourist.isalive:
            print("Tourist at ({},{}), {} turns without seeing a bear. - Left the Field".format(tourist.r,tourist.c,tourist.turn))
            tourcopy.remove(tourist)
    currenttours = tourcopy
    berry = BerryField.BerryField(berry.berries,currentbears,currenttours)
    print(berry)
    print("Active Bears:")
    for bear in currentbears:
        print(bear)
    print()
    print("Active Tourists:")
    for tourist in currenttours:
        print(tourist)
    print()
    turns+=1
