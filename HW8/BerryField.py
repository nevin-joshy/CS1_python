# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 20:51:48 2022

@author: Nevin Joshy
"""


class BerryField(object):
    def __init__(self, berrygrid, bearlist, tourlist):#initializer takes in a grid of berries, a list of bears, and a list of tourists
        self.berries = berrygrid#self function self.berries becomes the grid of berries
        self.tourists = tourlist#self function self.tourists becomes the list of tourists
        self.bears = bearlist#self function self.bears becomes the list of bears
        numberries = 0
        for row in self.berries:#counts the number of berries
            numberries+=sum(row)
        self.num = numberries#assigns the total number or berries to self.num
        self.bearcord = []
        for bear in self.bears:#creates a list of tuples that are the coordinates of the bears
            self.bearcord.append((bear.r,bear.c))
        self.tourcord = []#creates a list of tuples that are the coordinates of the tourists
        for tour in self.tourists:
            self.tourcord.append((tour.r,tour.c))
        
    def __str__(self):#string funtion of berryfield
        final = "Field has {} berries.\n".format(self.num)#starts a string that begins with the number of berries on the grid, using self.num
        for r in range(len(self.berries)):
            for c in range(len(self.berries[0])):#iterates through every point on the grid
                val = str(self.berries[r][c])#assigns val to the value of the grid point
                if (r,c) in self.bearcord and (r,c) in self.tourcord:#if the coordinate is in both of the lists of bears and tourists, val becomes X
                    val = "X"
                elif (r,c) in self.tourcord:#if it is not in both and only in tourists, then val becomes T
                    val = "T"
                elif (r,c) in self.bearcord:#if it is not in both and only in bears, then val becomes B
                    val = "B"
                final += "{:>4}".format(val)#adds val to the string and spaces them out
            final+="\n"
        return final#return the final string
    
    def growfield(self):#growfield function of berryfield
        for r in range(len(self.berries)):
            for c in range(len(self.berries[0])):#iterates through each coordinate of the berrygrid
                if self.berries[r][c]>=1 and self.berries[r][c]<10:#checks if the number of the berries is greater than 1 and less than 10
                    self.berries[r][c]+=1#if so, adds 1 to the value of the coordinate
        for r in range(len(self.berries)):
            for c in range(len(self.berries[0])):#iterates through each coordinate of the berrygrid
                if self.berries[r][c]==0:#checks if there are no berries at the coordinate
                    if c-1>=0:#checks whether it is possible to subtract 1 from the column number
                        if self.berries[r][c-1]==10:#if so, the coordinate to the left is checked to see if it has 10 berries
                            self.berries[r][c]=1#if so, the number of berries on the current coordinate grows to 1
                        if r-1>=0:#checks whether it is possible to subtract 1 from the row number
                            if self.berries[r-1][c-1]==10:#if so, the coordinate to the top left is checked to see if it has 10 berries
                                self.berries[r][c]=1#if so, the number of berries on the current coordinate grows to 1
                        if r+1<len(self.berries):#checks whether it is possible to add 1 from the row number
                            if self.berries[r+1][c-1]==10:#if so, the coordinate to the bottom left is checked to see if it has 10 berries
                                self.berries[r][c]=1#if so, the number of berries on the current coordinate grows to 1
                    if c+1<len(self.berries):#checks whether it is possible to add 1 to the column number
                        if self.berries[r][c+1]==10:#if so, the coordinate to the right is checked to see if it has 10 berries
                            self.berries[r][c]=1#if so, the number of berries on the current coordinate grows to 1
                        if r-1>=0:#checks whether it is possible to subract 1 from the row number
                             if self.berries[r-1][c+1]==10:#if so, the coordinate to the top right is checked to see if it has 10 berries
                                 self.berries[r][c]=1#if so, the number of berries on the current coordinate grows to 1
                        if r+1<len(self.berries):#checks whether it is possible to add 1 to from the row number
                             if self.berries[r+1][c+1]==10:#if so, the coordinate to the bottom right is checked to see if it has 10 berries
                                 self.berries[r][c]=1#if so, the number of berries on the current coordinate grows to 1
                    if r-1>=0:#checks whether it is possible to subract 1 from the row number
                        if self.berries[r-1][c]==10:#if so, the coordinate to the top is checked to see if it has 10 berries
                            self.berries[r][c]=1#if so, the number of berries on the current coordinate grows to 1
                    if r+1<len(self.berries):#checks whether it is possible to add 1 to from the row number
                        if self.berries[r+1][c]==10:#if so, the coordinate to the bottom is checked to see if it has 10 berries
                            self.berries[r][c]=1#if so, the number of berries on the current coordinate grows to 1
                    
        numberries = 0#recalculates the number of berries after growing the field and updates self.num
        for row in self.berries:
            numberries+=sum(row)
        self.num = numberries
        
