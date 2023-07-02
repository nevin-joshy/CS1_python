# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 20:59:38 2022

@author: Nevin Joshy
"""

class Tourist(object):
    def __init__(self, row, col, length, turns=0):#tourist object takes in a row, column, direction, length value and turns which is 0 by default
        self.r = row#self.r function becomes the row
        self.c = col#self.c becomes the column
        self.turn = turns#self.turns, the number of turns without seeing a bear, becomes turns
        self.count=0#self.count, the number of bears the tourist can see, starts at 0
        self.isalive = True#self.isalive, which states whther the tourist is alive(still on the field) starts as True
        self.len = length# self.len, the length of the field, becomes length
        self.added = False#the boolean that checks whether the tourist was added, starts as False
        
    def __str__(self):#string function for tourist
        return "Tourist at ({},{}), {} turns without seeing a bear.".format(self.r,self.c,self.turn)#prints the tourist using its coordinates and the number of turns it has without seeing a bear
        
    def tourcheck(self, bearlist):#tourcheck function takes in a list of bears
        self.count=0#resets the count of bears the tourist sees to 0
        for bear in bearlist:
            if ((bear.r,bear.c)==(self.r,self.c)):#checks if any of the bears in the bearlist have the same coordinate
                self.isalive = False#if so, isalve becomes false
            elif ((((abs(bear.r-self.r))**2) + ((abs(bear.c-self.c))**2))**0.5)<=4:#else, checks to see if the bear is within 4 of the tourist
                self.count+=1#if so, adds 1 to the count
        if self.count>0:#if the number of bears the tourist saw is greater then 0, the number of turns without seeing a bear becomes 0
            self.turn=0
            if self.count>=3:#if the number of bears is sees is 3 or more, it leaves the field so isalive becomes false
                self.isalive=False
        elif self.isalive:#else if the tourist is still alive, the turns without seeing a bear goes up by 1
            self.turn+=1
        if self.turn>=3:#is the turns without seeing a bear is 3 or more, the tourist leaves the field so isalive becomes false
            self.isalive=False
                
