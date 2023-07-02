# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 13:15:15 2022

@author: Nevin Joshy
"""

import hw5_util as hw

"""This function takes in the row and column of a certain point , and the number of rows and 
colums in the grid and uses them to find the neighbors of the point. first it adds
to the row and column to find the up,down,left,right points and then adds them to a list 
the list is then sorted through to see if there are any points that are out of bounds"""
def get_nbrs(row,col,numrow,numcol):
    up = (row-1,col)
    down = (row+1,col)
    right = (row, col+1)
    left = (row,col-1)
    neighbors = [up,left,right,down]  
    newneighbors = neighbors.copy()
    for tup in neighbors:
        if tup[0]<0 or tup[0]>numrow-1:
            newneighbors.remove(tup)
        if tup[1]<0 or tup[1]>numcol-1:
            newneighbors.remove(tup)
    return newneighbors

"""checks to make sure the next point in the path is a neighbor of the current point
by comparing it to the neighbirs of the current point"""
def isneighbor(row,col,rownext,colnext,numrow,numcol):
    firstneighbors = get_nbrs(row,col,numrow,numcol)
    for item in firstneighbors:
        if item == (rownext,colnext):
            return True
    return False

"""loop to make sure valid grid is inputted"""
isLegal = False
while not isLegal:
    n = input("Enter a grid index less than or equal to 3 (0 to end): ").strip()
    print(n)
    n = int(n)
    grid = hw.get_grid(n)
    if n<=3 and n>=0:
        break
"""printing part of code: prints grid if user says so, and prints neighbors of each starting location
by printing the elements reutrned from the get_nbrs function"""
shouldprint= input("Should the grid be printed (Y or N): ").strip()
print(shouldprint)
numrows = len(grid)
numcols = (len(grid[0]))
if shouldprint.lower()=="y":
    print("Grid {:d}".format(n))
    for r in range(numrows):
        for c in range(numcols):
            print(" {:3d}".format(grid[r][c]),end=(""))
        print("")
print("Grid has {:d} rows and {:d} columns".format(numrows, numcols))
for point in hw.get_start_locations(n):
    final = get_nbrs(point[0], point[1], numrows, numcols)
    new = ""
    for item in final:
        new +=(" "+str(item))
    print("Neighbors of "+str(point)+":"+new)
    
"""main body of code: finds whether there is a decrease or increase in elevation between the 
current and next points using if statements, then follows the path and adds the increase 
and decrease to their counters, totalup or totaldown. Then if it is a valid loop, prints
the info and if not, it prints the points where the jump cannot be made"""
totalup = 0
totaldown = 0
isValid = True
for num in range(len(hw.get_path(n))-1):
    rowfirst = hw.get_path(n)[num][0]
    colfirst = hw.get_path(n)[num][1]
    rowsecond = hw.get_path(n)[num+1][0]
    colsecond = hw.get_path(n)[num+1][1]
    if isneighbor(rowfirst,colfirst,rowsecond,colsecond,numrows,numcols):
        if grid[rowfirst][colfirst]-grid[rowsecond][colsecond]>0:
            totaldown +=(grid[rowfirst][colfirst]-grid[rowsecond][colsecond])
        else:
            totalup +=(grid[rowsecond][colsecond]-grid[rowfirst][colfirst])
    else:
        point1 = (rowfirst,colfirst)
        point2 = (rowsecond,colsecond)
        isValid=False
        break
if isValid:
    print("Valid path")
    print("Downward {:d}".format(totaldown))
    print("Upward {:d}".format(totalup))
else:
    print("Path: invalid step from {0} to {1}".format(point1,point2))
        