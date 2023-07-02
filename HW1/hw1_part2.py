# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 21:56:42 2022

@author: Nevin Joshy
"""
import math as m

min = input("Minutes ==> ")
print(min)
min = float(min)
sec = input("Seconds ==> ")
print(sec)
sec = float(sec)
mil = input("Miles ==> ")
print(mil)
mil = float(mil)
targ = input("Target Miles ==> ")
print(targ)
targ = float(targ)

pacec= ((min*60)+sec)/60/mil
pacemin= m.floor(((min*60)+sec)/60/mil)
pacesec = m.floor(((((min*60)+sec)/60/mil)-pacemin)*60)
speed = mil/(((min*60)+sec)/3600)
timemin = m.floor(targ * pacec)
timesec= m.floor(((targ*pacec)- timemin)*60)

print("")

print("Pace is {:.0f} minutes and {:.0f} seconds per mile.".format(pacemin,pacesec))
print("Speed is {:.2f} miles per hour.".format(speed))
print("Time to run the target distance of {:.2f} miles is {:.0f} minutes and {:.0f} seconds.".format(targ,timemin,timesec))