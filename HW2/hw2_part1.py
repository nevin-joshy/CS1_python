# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 13:21:04 2022

@author: Nevin Joshy
"""
import math as m

def find_volume_sphere(radius):
    return (4/3)*m.pi*(radius**3)

def find_volume_cube(side):
    return side**3

rad = input("Enter the gum ball radius (in.) => ").strip()
print(rad)
rad = float(rad)
sales= input("Enter the weekly sales => ").strip()
print(sales)
sales = float(sales)

numgum = sales*1.25
side = m.ceil(numgum**(1/3))
length = (rad*2)*side
totgum = side**3
targsale = m.ceil(numgum)
vol = find_volume_cube(length)
extragum = totgum-targsale
space1 = vol- (targsale*find_volume_sphere(rad))
space2 = vol - (totgum*find_volume_sphere(rad))

print("\nThe machine needs to hold {:.0f} gum balls along each edge.".format(side))
print("Total edge length is {:.2f} inches.".format(length))
print("Target sales were {:.0f}, but the machine will hold {:.0f} extra gum balls.".format(targsale,extragum))
print("Wasted space is {:.2f} cubic inches with the target number of gum balls,".format(space1))
print("or {:.2f} cubic inches if you fill up the machine.".format(space2))