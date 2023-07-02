# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 16:15:19 2022

@author: Nevin Joshy
"""

import hw4_util as h

week = 1

''' This module takes an input of a state and uses it to calculate the average positive cases
per 100000 people. It sorts through a list of the given week and once it finds the list with 
the correct state, it creates a new list with that list. Then, the average is calculated 
from indexes 2-8 of that list.'''
def daily(state):
    exists = False
    for lists in data:
        if lists[0] == state:
            newlist = lists
            exists = True
    if exists == False:
        print("State {:s} not found".format(state))
        return
    total = 0
    for item in range(2,9):
        total += newlist[item]/(newlist[1]/100000)
        avg = round((total/7),1)
    return avg

''' This module takes an input of a state and uses it to calculate the average percent 
positive cases. It sorts through a list of the given week and once it finds the list with 
the correct state, it creates a new list with that list. Then, the total positive cases is calculated 
from indexes 2-8 of that list, and total negative with 9-15, then we us percent = 
P/N+P *100'''
def pct(state):
    exists = False
    for lists in data:
        if lists[0] == state:
            newlist = lists
            exists = True
    if exists == False:
        print("State {:s} not found".format(state))
        return
    postotal=0
    for item in range(2,9):
        postotal += newlist[item]
    negtotal = 0
    for item in range(9,16):
        negtotal += newlist[item]
    pcavg = (postotal/(postotal+negtotal))*100
    return pcavg

""" This module takes lists that are "high spread" and adds the state to a list. The list 
is then sorted and printed using the module from hw4.util"""
def quar(week):
    newlist = []
    for lists in data:
        if daily(lists[0])>10 or pct(lists[0])>10:
            newlist.append(lists[0])
    newlist.sort()
    h.print_abbreviations(newlist)
    
"""This module goes through the lists of the given week and uses the daily funtion to find
the highest daily positive cases"""
def high(week):
    num= 0
    abr = ""
    for lists in data:
        if daily(lists[0])>num:
            num = daily(lists[0])
            abr = lists[0]
    return (num,abr)

"""In this loop, the program is executed and takes all the required inputs and depending on the input
it runs one of the modules above"""
while week>=1 and week<=29:
    print("...")
    week = input("Please enter the index for a week: ").strip()
    print(week)
    week = int(week)
    if week<1:
        break
    if week>=1 and week<=29:
        key = input("Request (daily, pct, quar, high): ").strip()
        print(key)
        data = h.part2_get_week(week)
        if key.lower() =="daily":
            state = input("Enter the state: ").strip()
            print(state)
            if daily(state)!=None:
                print("Average daily positives per 100K population:",daily(state))
        elif key.lower() == "pct":
            state = input("Enter the state: ").strip()
            print(state)
            if pct(state)!=None:
                print("Average daily positive percent: {:.1f}".format(pct(state)))
        elif key.lower() == "quar":
            print("Quarantine states:")
            quar(week)
        elif key.lower() == "high":
            print("State with highest infection rate is",high(week)[1])
            print("Rate is {:.1f} per 100,000 people".format(high(week)[0]))
        else:
            print("Unrecognized request")
    else:
        print("No data for that week")
        week = 1
    