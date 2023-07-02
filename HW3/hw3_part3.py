# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 15:43:20 2022

@author: Nevin Joshy
"""
import math

def num_humans(numbears):
    if numbears<4 or numbears>15:
        tourists = 0
    elif numbears>3 and numbears<=10:
        tourists = int(numbears*10000)
    elif numbears>10 and numbears<=15:
        tourists = int((100000)+(numbears-10)*20000)
    return tourists

def find_next(bears,berries,tourists):
    bears_next = int(berries/(50*(bears+1)) + bears*0.60 - (math.log(1+tourists,10)*0.1))
    berries_next = (berries*1.5) - (bears+1)*(berries/14) - (math.log(1+tourists,10)*0.05)
    return (bears_next,berries_next)

bears = input("Number of bears => ").strip()
print(bears)
bears = int(bears)
berries = input("Size of berry area => ").strip()
print(berries)
berries = float(berries)
print("Year\tBears\tBerry\tTourists")
tourists = num_humans(bears)

years = 1
listbears =[]
listberries =[]
listtourists = []
while years<11:
    print("{:d}\t\t{:d}\t\t{:.1f}\t{:d}".format(years,bears,berries,tourists))
    listbears.append(bears)
    listberries.append(float(round(berries,1)))
    listtourists.append(tourists)
    nextbears = find_next(bears,berries,num_humans(bears))[0]
    if find_next(bears,berries,num_humans(bears))[1]>0:
        nextberries = find_next(bears,berries,num_humans(bears))[1]
    else:
        nextberries=0
    nexttourists = num_humans(nextbears)
    bears = nextbears
    berries = nextberries
    tourists = nexttourists
    years+=1
    
print("\nMin:\t{:s}\t\t{:s}\t{:s}".format(str(min(listbears)),str(min(listberries)),str(min(listtourists))))
print("Max:\t{:s}\t\t{:s}\t{:s}".format(str(max(listbears)),str(max(listberries)),str(max(listtourists))))
