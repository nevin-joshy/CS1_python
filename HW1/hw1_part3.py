# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 13:50:25 2022

@author: Nevin Joshy
"""
import math as m

char = input("Enter frame character ==> ").strip()
print(char)
height = input("Height of box ==> ").strip()
print(height)
height = int(height)
width = input("Width of box ==> ").strip()
print(width)
width = int(width)
print("\nBox:")

cap = char * width
normrow = char + (" "*(width-2)) + char
remrow = height - 3
rowtop = m.floor(remrow/2)
rowbot = m.ceil(remrow/2)
dim = str(width)+"x"+str(height)
remcol = width-2-(len(dim))
coll = m.floor(remcol/2)
colr = m.ceil(remcol/2)
midrow = char + (" "*coll) + dim + (" "*colr) + char
print(cap + rowtop*("\n"+normrow) + ("\n"+midrow) + rowbot*("\n"+normrow) + ("\n"+cap))