# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 12:54:28 2022

@author: Nevin Joshy
"""

import syllables as syl

par = input("Enter a paragraph => ").strip()
print(par)

def asl(paragraph):
    sentlength = []
    previndex = 0
    words = paragraph.split()
    for i in range(len(words)):
        if words[i].count(".")>0:
            length = (i+1)-previndex
            sentlength.append(length)
            previndex = i+1
    return sum(sentlength)/len(sentlength)


hardlist = []

def phw(paragraph):
    words = paragraph.split()
    count = 0
    for i in words:
        if syl.find_num_syllables(i)>=3 and i.count("-")==0 and i[len(i)-2:len(i)-1] != "ed" and i[len(i)-2:len(i)-1] != "es":
            count+=1
            hardlist.append(i)
    return (count/len(words))*100

def asyl(paragraph):
    words = paragraph.split()
    sylab = 0
    for i in words:
        sylab += syl.find_num_syllables(i)
    return sylab/len(words)

gfri =  0.4*(asl(par) + phw(par))
fkri = 206.835-(1.015*asl(par))-(86.4*asyl(par))

    
print("Here are the hard words in this paragraph:\n"+str(hardlist))
print("Statistics: ASL:{:.2f} PHW:{:.2f}% ASYL:{:.2f}".format(asl(par),phw(par),asyl(par)))
print("Readability index (GFRI): {:.2f}".format(gfri))
print("Readability index (FKRI): {:.2f}".format(fkri))


        
    