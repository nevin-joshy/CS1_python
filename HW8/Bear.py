# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 21:00:55 2022

@author: Nevin Joshy
"""

class Bear(object):
    def __init__(self, row, col, direction):#intializes bears and takes in a row, column, and direction
        self.r = row#self.r function becomes the row
        self.c = col#self.c becomes the column
        self.di = direction#self.di becomes the direction
        self.berry = 0#self.berry, the number of berries the bear eats, starts at 0
        self.skip = 0#self.skip, the number of turns the bear has left to skip, starts at 0
        self.inbounds=True#the boolean that checks whter the bear is inbounds, starts as True
        self.added = False#the boolean that checks whether the bear was added, starts as False
        
    def __str__(self):#string function of bear
        if self.skip-1>0:#checks whether the skip value is greater than 0
            return "Bear at ({},{}) moving {} - Asleep for {} more turns".format(self.r, self.c, self.di, self.skip-1)# if so, the bear is printed with the fact that it is asleep 
        return "Bear at ({},{}) moving {}".format(self.r, self.c, self.di)#if not, the bear is printed normally
    
    def move(self, berryfield, tourlist):#move function of bear, takes in the grid of berries and the list of tourists
        
        if self.skip>0:#if the skip is greater than 0, subtract 1 from it(1 less turn)
            self.skip-=1
        while self.berry<30 and self.skip==0 and self.inbounds:#checks if the number of berries the bear has eaten so far is less than 30, it needs to skip any turns, and that it is inbounds
            for tourist in tourlist:
                if ((self.r,self.c)==(tourist.r,tourist.c)):#checks whether the coordinate of the bear is the same as any of the tourists
                    self.skip=3#if so, sets the skip value of the bear to 3
            if self.skip ==0:#checks if the bear has no skip value
                if self.berry+berryfield[self.r][self.c]>=30:#checks if adding the value of the coordinate makes the number of berries equal or go over 30 
                    berryfield[self.r][self.c]-=(30-self.berry)#if so, leaves the rest of the berries after 30 on the coordinate
                    self.berry = 30#selts the number of berries the bear ate to 30
                else:
                    self.berry+=berryfield[self.r][self.c]#adds the value of the coordinate to the number of berries the bear ate
                    berryfield[self.r][self.c] = 0#leaves 0 berries behind in the spot
                    if self.di=="N":#if the direction is N, the bear moves up by subracting one from the row value
                        self.r-=1
                    elif self.di=="S":#if the direction is S, moves down by adding 1 to the row value
                        self.r+=1
                    elif self.di=="E":#if the direction is E, moves right by adding 1 to column
                        self.c+=1
                    elif self.di=="W":#if the direction is W, moves left by subtracting 1 from column
                        self.c-=1
                    elif self.di=="NE":#if the direction is NE, moves top right by subtracting 1 from row and adding 1 to column
                        self.r-=1
                        self.c+=1
                    elif self.di=="NW":#if the direction is NW moves top left by subtracting 1 from row and column
                        self.r-=1
                        self.c-=1
                    elif self.di=="SE":#if the direction is SE moves bottom right by addind 1 to  row and column
                        self.r+=1
                        self.c+=1
                    elif self.di=="SW":#if the direction i SW moves bottom left by subtracting 1 from column and adding 1 to row
                        self.r+=1
                        self.c-=1
                    if self.r<0 or self.r>=len(berryfield) or self.c<0 or self.c>=len(berryfield):#if the row or column value is now less than 0 or greater then the length, self.inbounds becomes false
                        self.inbounds = False
        self.berry=0#resets the amount of berries the bear ate to 0
        