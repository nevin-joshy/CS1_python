# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 17:05:22 2022

@author: Nevin Joshy
"""

turns = input("How many turns? => ").strip()
print(turns)
turns = int(turns)
name = input("What is the name of your pikachu? => ").strip()
print(name)
often = input("How often do we see a Pokemon (turns)? => ").strip()
print(often)
often = int(often)

def move_pokemon(coord, direction, steps):
    row = coord[0]
    column = coord[1]
    if direction.lower()=="n":
        if (row - steps)<=0:
            row =0
        else:
            row -= steps
    elif direction.lower()=="s":
        if (row + steps)>=150:
            row = 150
        else:
            row +=steps
    elif direction.lower() =="e":
        if (column + steps)>=150:
            column =150
        else:
            column+=steps
    elif direction.lower() =="w":
        if (column - steps)<=0:
            column =0
        else:
            column-=steps
    coord = (row,column)
    return coord

coord = (75,75)
record = []
val = 0
turnsleft =turns
print("\nStarting simulation, turn 0 {:s} at ".format(name)+str(coord))
while val<=turns:
    val+=often
    if often<turns:
        often2 = often
    else:
        often2=turns
    if turns ==0:
        break
    counter =0
    while turnsleft>0:
        if counter == often2:
            counter = 0
            break
        direction = input("What direction does {:s} walk? => ".format(name)).strip()
        print(direction)
        direction = direction.lower()
        coord = move_pokemon(coord, direction, 5)
        counter+=1
        turnsleft-=1
        
    if often>turns:
        break
    if val>turns:
        break
    print("Turn "+str(val)+", {:s} at ".format(name)+ str(coord))
    poktype = input("What type of pokemon do you meet (W)ater, (G)round? => ").strip()
    print(poktype)
    if poktype.lower() == "w":
        coord = move_pokemon(coord, direction, 1)
        print("{:s} wins and moves to ".format(name)+ str(coord))
        record.append("Win")
    elif poktype.lower() == "g":
        if direction == "n":
            coord = move_pokemon(coord, "s", 10)
        elif direction == "s":
            coord = move_pokemon(coord, "n", 10)
        elif direction == "e":
            coord = move_pokemon(coord, "w", 10)
        elif direction == "w":
            coord = move_pokemon(coord, "e", 10)
        print("{:s} runs away to ".format(name) + str(coord))
        record.append("Lose")
    else:
        record.append("No Pokemon")
    if turnsleft==0:
        break
    if val == turns:
        break

print("{:s} ends up at ".format(name) + str(coord) + ", Record: "+ str(record))
    

    