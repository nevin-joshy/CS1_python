# -*- coding: utf-8 -*-
"""
Created on Tue Oct 11 14:51:27 2022

@author: Nevin Joshy
"""
import hw4_util


pas = input("Enter a password => ").strip()
print(pas)

count = 0
commonwords=hw4_util.part1_get_top()

"""This module checks the length of the password and assigns the correct number of points
depending on the length of the string"""
def lenpts(password):
    subcount = 0
    if len(password)==6 or len(password)==7:
        subcount+=1
    elif len(password)>=8 and len(password)<=10:
        subcount+=2
    elif len(password)>10:
        subcount+=3
    if subcount>0:
        print("Length: +"+str(subcount))
    return subcount

"""This module counts the number of capital and lowercase letters in the password string 
by using the isupper and islower modules. It then uses the number that is counted to 
assign the correct number of points"""
def casepts(password):
    subcount = 0
    numcap = 0
    numlower=0
    for letter in range(len(password)):
        if password[letter].isupper() == True:
            numcap+=1
        elif password[letter].islower() == True:
            numlower+=1
    if numcap>=2 and numlower>=2:
        subcount=2
    elif numcap>=1 and numlower>=1:
        subcount=1
    if subcount>0:
        print("Cases: +"+str(subcount))
    return subcount

"""This module uses the module isdigit to count the number of digits in the password, and then
assings apoints according to how many digits there are in the password"""
def digpts(password):
    numdig = 0
    subcount = 0
    for char in password:
        if char.isdigit() == True:
            numdig+=1
    if numdig>=2:
        subcount+=2
    elif numdig>=1:
        subcount+=1
    if subcount>0:
        print("Digits: +"+str(subcount))
    return subcount

"""This module evauluates what type of symbols are used in the password, either !@#$ or
 ^&%*, and then assigns the correct number of points depending on the symbol used"""
def puncpts(password):
    numpunc = 0
    numpunc2 = 0
    subcount = 0
    for char in password:
        if char == "!" or char == "@" or char == "#" or char == "$":
            numpunc=1
        if char == "%" or char == "^" or char == "*" or char == "&":
            numpunc2=1
    subcount = numpunc +numpunc2
    if numpunc>0:
        print("!@#$: +"+str(numpunc))
    if numpunc2>0:
        print("%^&*: +"+str(numpunc2))
    return subcount

"""This module determines whether the first 3 indexes of the string are letters using
islower and whether the last 4 digits are numbers using isdigit. If so, it gives
the correct nuber of points accordingly"""
def licpts(password):
    subcount = 0
    new = password.lower()
    new1 = new[0:3]
    new2 = new[3:]
    if new1.islower()==True and new2.isdigit() == True:
        subcount = -2
    if subcount == -2:
        print("License: -2")
    return subcount

"""This module seaches the common words list and if there is a match, it takes 3
points away from the total points"""
def commonpts(password):
    subcount = 0
    new = password.lower()
    for word in commonwords:
        if word == new:
            subcount = -3
    if subcount == -3:
        print("Common: -3")
    return subcount

"""Adds up the points, then asscoiates the number of points with a password rating"""
count = lenpts(pas)+casepts(pas)+digpts(pas)+puncpts(pas)+licpts(pas)+commonpts(pas)
print("Combined score:",count)
if count<=0:
    print("Password is rejected")
elif count==1 or count ==2:
    print("Password is poor")
elif count==3 or count==4:
    print("Password is fair")
elif count==5 or count ==6:
    print("Password is good")
elif count>=7:
    print("Password is excellent")