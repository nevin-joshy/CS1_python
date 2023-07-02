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

"""uses recursion to return a list containing the steepest path. It finds the neighbors and
uses if statements to check whether each neighor is greater than the current, and also uses
a holding value which starts at the value of the current point but changes if a higher
value if found in neighbors that is still within the highest step. the point
that is the highest is appended to a list, and the function is called again"""
def steepest(row,col,step,steeplist):
    
    bordering = get_nbrs(row,col,numrows,numcols)
    highest= grid[row][col]
    for item in bordering:
        r=item[0]
        c=item[1]
        if grid[r][c]>grid[row][col] and grid[r][c]>highest and grid[r][c]-grid[row][col]<=step:
            highest = grid[r][c]
            final = (r,c)
    if highest == grid[row][col]:
        return (steeplist)
    if highest>grid[row][col]:
        steeplist.append(final)
        steepest(final[0],final[1],step,steeplist)
        return (steeplist)

"""uses recursion to return a list containing the most gradual path. It finds the neighbors and
uses if statements to check whether each neighor is greater than the current, and also uses
a holding value which starts at the value of the current point but changes if a lower highest
value if found in neighbors that is still within the highest step. the point
that is the lowest highest is appended to a list, and the function is called again"""
def gradual(row,col,step,graduallist):
    bordering = get_nbrs(row, col, numrows, numcols)
    currenthighest = 1000
    for item in bordering:
        r= item[0]
        c=item[1]
        if grid[r][c]>grid[row][col] and grid[r][c]<currenthighest and grid[r][c]-grid[row][col]<=step:
            currenthighest = grid[r][c]
            final = (r,c)
    if currenthighest==1000:
        return (graduallist)
    if currenthighest>grid[row][col]:
        graduallist.append(final)
        gradual(final[0],final[1],step,graduallist)
        return (graduallist)
    
"""loop to make sure valid grid is inputted"""

isLegal = False
while not isLegal:
    n = input("Enter a grid index less than or equal to 3 (0 to end): ").strip()
    print(n)
    n = int(n)
    grid = hw.get_grid(n)
    if n<=3 and n>=0:
        break
    
numrows = len(grid)
numcols = (len(grid[0]))

"""gathers user inputs for each necessary piece of info"""
step = input("Enter the maximum step height: ").strip()
print(step)
answer = input("Should the path grid be printed (Y or N): ").strip()
print(answer)
step= int(step)
print("Grid has {:d} rows and {:d} columns".format(numrows, numcols))
    
"""finds the global max and its index by shuffling through the grid and ressigning a
number max if a higher value is found, until it becomes the highest. the index of that
max is saved"""
maxnum = 0
for r in range(numrows):
    for c in range(numcols):
        if grid[r][c]>maxnum:
            maxnum = grid[r][c]
            index= (r,c)
print("global max: {0} {1}".format(index,maxnum))

"""main body of code: first, in a loop of each starting point, lists are made containing the starting points
then, the steepest path is printed using the function steepest and printing the list that is
returned. Next, if the last element of the list is equal to the coordinates of the global
max, then it is printed that a global max has been reached. if not, then it is tested for 
no max by using the get_nbrs and if the numbers around it are less, then it is a local max and
 that is printed. Else, it is a no max and that is printed. The same code repeats with gradual"""
finallist=[]
for item in hw.get_start_locations(n):
        print("===")
        mylist = [(item[0],item[1])]
        mylist2 = [(item[0],item[1])]
        newlist = steepest(item[0], item[1], step, mylist)
        newlist2 = gradual(item[0],item[1],step,mylist2)
        finallist.append(newlist)
        finallist.append(newlist2)
        print("steepest path")
        count = 0
        for item in newlist:
            if count ==5:
                print("")
                count = 0
            print (str(item),end=" ")
            count +=1
        if newlist[len(newlist)-1] == index:
            print("\nglobal maximum")
        if not newlist[len(newlist)-1]==index:
            temp = newlist[len(newlist)-1]
            firstrow=temp[0]
            firstcol=temp[1]
            newnbrs = get_nbrs(firstrow,firstcol,numrows,numcols)
            ismax = True
            for item in newnbrs:
                r=item[0]
                c=item[1]
                if grid[r][c]>grid[firstrow][firstcol]:
                    ismax=False
            if ismax:
                print("\nlocal maximum")
            else:
                print("\nno maximum")
        print("...")
        print("most gradual path")
        count2 = 0
        for item in newlist2:
            if count2 ==5:
                print("")
                count2 = 0
            print (str(item),end=" ")
            count2 +=1
        if newlist2[len(newlist2)-1] == index:
            print("\nglobal maximum")
        if not newlist2[len(newlist2)-1]==index:
            temp = newlist2[len(newlist2)-1]
            firstrow=temp[0]
            firstcol=temp[1]
            newnbrs = get_nbrs(firstrow,firstcol,numrows,numcols)
            ismax = True
            for item in newnbrs:
                r=item[0]
                c=item[1]
                if grid[r][c]>grid[firstrow][firstcol]:
                    ismax=False
            if ismax:
                print("\nlocal maximum")
            else:
                print("\nno maximum")

"""code for the path grid: first initializes a grid of the right size filled with "."
then it uses a list of lists initialized in the previous block called finallist 
and sorts through it and counts the occurences of each element, then prints it to the corrrect
coordinate of the new path grid"""
if answer.lower()=="y":
    finalgrid = []
    u = []
    for i in range(numrows):
        for j in range(numcols):
            u.append(".")
        finalgrid.append(u)
        u = []
    newcount=0
    for item in finallist:
        for tup in item:
            for lists in finallist:
                newcount += lists.count(tup)
            finalgrid[tup[0]][tup[1]] = newcount
            newcount = 0
    print("===")
    print("Path grid")
    for lists in finalgrid:
        for item in lists:
            print("  "+str(item), end=(""))
        print("")
    
            