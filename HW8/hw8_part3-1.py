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
    
turns = 0
while not (len(currentbears)==0 and len(reservebears)==0) or (len(currentbears)==0 and berry.num==0):
    turns+=1
    print()
    print("Turn: {}".format(turns))
    berry.growfield()
    for bear in currentbears:
        bear.move(berry.berries,currenttours)
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
    if len(reservebears)>0 and berry.num>=500:
        reservebears[0].added = True
        currentbears.append(reservebears[0])
        reservebears.remove(reservebears[0])
    if len(reservetours)>0 and len(currentbears)>0:
        reservetours[0].added = True
        currenttours.append(reservetours[0])
        reservetours.remove(reservetours[0])
    for bear in currentbears:
        if bear.added:
            print("Bear at ({},{}) moving {} - Entered the Field".format(bear.r, bear.c, bear.di))
            bear.added = False
    for tourist in currenttours:
        if tourist.added:
            print("Tourist at ({},{}), {} turns without seeing a bear. - Entered the Field".format(tourist.r,tourist.c,tourist.turn))
            tourist.added=False
    berry = BerryField.BerryField(berry.berries,currentbears,currenttours)
    print(berry)
    if turns%5==0:
        
        print("Active Bears:")
        for bear in currentbears:
            print(bear)
        print()
        print("Active Tourists:")
        for tourist in currenttours:
            print(tourist)
    print()
    
print(berry)
print("Active Bears:")
for bear in currentbears:
    print(bear)
print()
print("Active Tourists:")
for tourist in currenttours:
    print(tourist)
