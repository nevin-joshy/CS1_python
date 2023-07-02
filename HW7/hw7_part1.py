# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 16:30:29 2022

@author: Nevin Joshy

This is a small autocorrect program. it goes through every single word in the input file, autocorrect each word and
print the correction. It uses various methods to autocorrect and gives the best 3
options using their frequency in the english language.
"""

from string import ascii_lowercase#list containing all lowercase letters

"""If the word is not found, considers all possible ways to drop a single letter from the word.
takes an input word from the file and a list to append to. it splits the word into a list of 
letters then removes each index of the word adn joins it back to gether, testing to see
if any are in the english ditionary. If it is, it is appended to finallist with its freqency in a tuple"""
def drop(word,finaldict):
    for num in range(len(word.strip())):
        wordlist = list(word)
        wordlist.pop(num)
        if "".join(wordlist) in dictionary:
            finaldict[word].add((dictionary["".join(wordlist)],"".join(wordlist)))

"""using ascii_lowercase, a list containing all lowercase letters, this definition 
puts each letter at each possible index of the word and tests if it is in the dictionary>
If it is, it is appended to finallist with its freqency in a tuple"""
def insert(word,finaldict):
    for letter in ascii_lowercase:
        for num in range(len(word.strip())+1):
            wordlist = list(word)
            wordlist.insert(num,letter)
            if "".join(wordlist) in dictionary:
                finaldict[word].add((dictionary["".join(wordlist)],"".join(wordlist)))
                
"""This definition takes the index of the current element of the loop and swaps it with the next element
in the word, and tests to see if it is a word and then continues on to the next pair. If it is, it is appended to finallist
with its freqency in a tuple"""
def swap(word,finaldict):
    for num in range(len(word.strip())-1):
        wordlist = list(word)
        wordlist[num],wordlist[num+1] = wordlist[num+1],wordlist[num]
        if "".join(wordlist) in dictionary:
            finaldict[word].add((dictionary["".join(wordlist)],"".join(wordlist)))
            
"""This definition replaces each letter in the word with each of its corresponding letters in 
the Keyboard file, which was read into a dictionary which will be explained later. If it is
found to be in the dictionary, it is appended to finallist with its freqency in a tuple"""
def replace(word,finaldict):
    for num in range(len(word)):
        wordlist = list(word)
        for replacement in keyboard[wordlist[num]]:
            wordlist.pop(num)
            wordlist.insert(num,replacement)
            if "".join(wordlist) in dictionary:
                finaldict[word].add((dictionary["".join(wordlist)],"".join(wordlist)))


#main code
if __name__ == "__main__":
    
    """Input statements for dictionary file, input file, and keyboard file"""
    dict_file = input("Dictionary file => ").strip()
    print(dict_file)
    input_file = input("Input file => ").strip()
    print(input_file)
    key_file = input("Keyboard file => ").strip()
    print(key_file)
    
    """dictionary file is read into a python dictionary with the word as the key
    and the frequency as the value"""
    dictionary = dict()
    for line in open(dict_file):
        newlist = line.split(",")
        dictionary[newlist[0].strip()]=float(newlist[1].strip())
    
    """keyboard dictionary which keeps the first letter as the key and all
    of the replacement letters as the key"""
    keyboard = dict()
    for line in open(key_file):
        newlist1 = line.split()
        keyboard[newlist1[0].strip()] = newlist1[1:]
    
    """opens and splits input file into a list of words called inputlist"""
    file = open(input_file)
    filein = file.read()
    inputlist = filein.split()
    
    
    finaldict = dict()#dictionary that all words are added to. in the loop
    #the key is defined to be the original word, and the value will be a set
    #of all of its possible replacements
    """if the word is found, the value corresponding to it is marked as found
    else, all of the autocorrect funtions are called, with the word and the finaldict"""
    for word in inputlist:
        finaldict[word] =set()
        if word in dictionary:
            finaldict[word] = "found"
        else:
            drop(word,finaldict)
            insert(word,finaldict)
            swap(word,finaldict)
            replace(word,finaldict)
            
    """printing portion: if the finaldict value is found, it prints thw word and found. If the length 
    of the corresponding set is 0, there were no matches so not found is printed. Finally,
    if it is none of those, the corresponding set is sorted in reverse order and the 
    first 3 elements are printed( sorted by frequency in tuple) and if only 3 or less elements are in the list, all
    elements are printed"""
    for key in finaldict:
        if finaldict[key]=="found":
            print("{:>15s} ->".format(key),"FOUND")
        elif len(finaldict[key])==0:
            print("{:>15s} ->".format(key),"NOT FOUND")
        else:
            sortlist=sorted(finaldict[key],reverse=True)
            print("{:>15s} ->".format(key),"FOUND{:>3d}: ".format(len(sortlist)),end="")
            if len(sortlist)<4:
                for item in sortlist:
                    print(" "+item[1],end="")
            else:
                for item in sortlist[:3]:
                    print(" "+item[1],end="")
            print()
                