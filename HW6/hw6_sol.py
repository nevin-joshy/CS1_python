# -*- coding: utf-8 -*-
"""
Created on Mon Oct 31 16:40:17 2022

@author: Nevin Joshy

This is a Python program that reads two files containing
the text of two different documents, analyzes each document, and compares the documents. 
It uses a Jaccard comparison to compare the similarity
"""

""""This function takes in a large string, which is the contents of the document. 
it then splits it into a list of words, and then each wird is split up into letters to iterate through each element
and gets rid of any character that is not a letter in the alphabet. The clenaed-up
word is joined and is then added to a new list"""
def parse_doc(doc):
    list1=doc.split()
    list2 = []
    for item in list1:
        if not item.isalpha() or not item.isascii():
            letterlist = list(item)
            letterlistcopy = letterlist.copy()
            for letter in letterlistcopy:
                if not letter.isalpha() or not letter.isascii():
                    letterlist.remove(letter)
            if len(letterlist)>0:
                s ="".join(letterlist)
                list2.append(s.lower())
        else:
            list2.append(item.lower())
    return (list2)

"""This is simple code that removes every element of stoplist from wordlist using a 
for loop."""
def stop_parse(wordlist,stopl):
    for word in stopl:
        while word in wordlist:
            wordlist.remove(word)
    return (wordlist)

"""This function takes in the list of words and creates a new list that hass the length
of every word in the given list. Then, the average word length is calucated by using
sum and len funtions"""
def avg_length(wordlist):
    newlist = []
    for word in wordlist:
        newlist.append(len(word))
    return (sum(newlist)/len(newlist))

"""This function takes in the wordlist and removes all duplicates by converting into
a set. It then finds the ration of the length of the new set to the old list"""
def ratio_distinct(wordlist):
    wordset = set(wordlist)
    return (len(wordset)/len(wordlist))

"""This function first uses a for loop to find the lengt of the longest word and 
uses it to create the bound for a while loop. The counter starts at 1 to indicate 
words of length 1, and then for each length it finds the words that are of that length
and adds them to a set, which is then added to a list. Each time the while loop is
looped through, the set is cleared so that the finallist that is returned contains
a list of sets of the words of each length"""
def length_list(wordlist):
    lencount = 1
    newlist = []
    for word in wordlist:
        newlist.append(len(word))
    longest = max(newlist)
    finallist = []
    lengthset = set()
    while lencount<=longest:
        lengthset.clear()
        for word in wordlist:
            if len(word)==lencount:
                lengthset.add(word)
        finallist.append(sorted(lengthset))
        lencount+=1
    return finallist
            
"""this fuction takes in a list of words and the sep parameter. First, it adds the last
two elements of the list as a tuple to the set, as they are not included in the later loop
to avoid out of bounds errors. The loop iterates throught the length of the list minus the
sep, and checks exh value from where it is at to sep ahead of it. it adds a sorted tuple
to the set for exh of these indices."""
def word_pair_list(wordlist,sep):
    wordset = set()
    wordset.add((wordlist[-2],wordlist[-1]))
    for num in range(len(wordlist)-sep):
        for num2 in range(sep):
            l1 = [wordlist[num],wordlist[num+num2+1]]
            l1.sort()
            wordset.add((l1[0],l1[1]))
    return sorted(wordset)

"""This function is the same as the one above, except it does not remove duplicates by 
using a list instead of a set"""
def total_pair(wordlist,sep):
    wordset = []
    wordset.append((wordlist[-2],wordlist[-1]))
    for num in range(len(wordlist)-sep):
        for num2 in range(sep):
            l1 = [wordlist[num],wordlist[num+num2+1]]
            l1.sort()
            wordset.append((l1[0],l1[1]))
    return wordset

"""this function takes in two lists and finds their jaccard value by first checking if the
length of either is 0, and if not it didved the length of the intersection of the sets by the
length of the union of the sets"""
def get_jaccard(list1,list2):
    if len(list1)==0 or len(list2) ==0:
        return 0
    return len(set(list1)&set(list2))/len(set(list1)|set(list2))
    

if __name__ == "__main__":
    
    #takes the input values of the first, second and sep parameters
    doc1 = input("Enter the first file to analyze and compare ==> ").strip()
    print(doc1)
    doc2 = input("Enter the second file to analyze and compare ==> ").strip()
    print(doc2)
    max_sep = input("Enter the maximum separation between words in a pair ==> ").strip()
    print(max_sep)
    max_sep = int(max_sep)
    print()
    
    #opens and parses the stop list using the parse doc function above
    stopin = open("stop.txt",encoding='utf-8')
    stop = stopin.read()
    stoplist = parse_doc(stop)
    
    """This is the code for the first inputted document"""
    
    #opens, parses, and removes stop words from first document by using parse_doc and
    #stop_parse functions above
    in1 = open(doc1,encoding=('utf-8'))
    first= in1.read()
    parsed1 = parse_doc(first)
    doc1list = stop_parse(parsed1,stoplist)
    print("Evaluating document {}".format(doc1))
    
    #finds average word length by using avg length function above
    print("1. Average word length: {:.2f}".format(avg_length(doc1list)))
    #finds ratio of distinct words by using ratio_distint function above
    print("2. Ratio of distinct words to total words: {:.3f}".format(ratio_distinct(doc1list)))
    #gets the list of sets from length_list above and uses a for loop to iterate
    #through it and print out the first 3 and last 3 words in the list if the list is
    #above length of 6. If not, all the words are printed
    print("3. Word sets for document {}:".format(doc1))
    length1 = length_list(doc1list)
    counter = 1
    for lengthset in length1:
        print("{:4d}:{:4d}:".format(counter,len(lengthset)),end=(""))
        if len(lengthset)<7:
            for word in lengthset:
                print(" "+word, end = "")
            print("")
        else:
            print(" {} {} {} ... {} {} {}".format(sorted(lengthset)[0],sorted(lengthset)[1],sorted(lengthset)[2],sorted(lengthset)[-3],sorted(lengthset)[-2],sorted(lengthset)[-1]))
        counter+=1
    #uses word_pair_list function to get the list of tuples of word pairs. uses
    #a for loop to print the first 5 and last 5 elements in the list if the length is 
    #greater than 10, and if not it prints all of the values
    print("4. Word pairs for document {}".format(doc1))
    wordpair1 = word_pair_list(doc1list,max_sep)
    print("  "+str(len(wordpair1)) +" distinct pairs")
    if len(wordpair1)>10:
        for tup1 in wordpair1[:5]:
            print("  "+tup1[0]+" "+tup1[1])
        print("  ...")
        for tup1 in wordpair1[-5:]:
            print("  "+tup1[0]+" "+tup1[1])
    else:
        for tup1 in wordpair1:
            print("  "+tup1[0]+" "+tup1[1])
    #finds the ratio between total_pair and word_pair_list of the wordlist
    print("5. Ratio of distinct word pairs to total: {:.3f}".format(len(word_pair_list(doc1list,max_sep))/len(total_pair(doc1list,max_sep))))
    print()
    
    """This is the code for the second inputted document"""

    #opens, parses, and removes stop words from first document by using parse_doc and
    #stop_parse functions above
    in2 = open(doc2,encoding='utf-8')
    second= in2.read()
    parsed2 = parse_doc(second)
    doc2list = stop_parse(parsed2,stoplist)
    print("Evaluating document {}".format(doc2))
    
    #finds average word length by using avg length function above
    print("1. Average word length: {:.2f}".format(avg_length(doc2list)))
    #finds ratio of distinct words by using ratio_distint function above
    print("2. Ratio of distinct words to total words: {:.3f}".format(ratio_distinct(doc2list)))
    #gets the list of sets from length_list above and uses a for loop to iterate
    #through it and print out the first 3 and last 3 words in the list if the list is
    #above length of 6. If not, all the words are printed
    print("3. Word sets for document {}:".format(doc2))
    length2 = length_list(doc2list)
    counter2 = 1
    for lengthset in length2:
        print("{:4d}:{:4d}:".format(counter2,len(lengthset)),end=(""))
        if len(lengthset)<7:
            for word in lengthset:
                print(" "+word, end = "")
            print("")
        else:
            print(" {} {} {} ... {} {} {}".format(sorted(lengthset)[0],sorted(lengthset)[1],sorted(lengthset)[2],sorted(lengthset)[-3],sorted(lengthset)[-2],sorted(lengthset)[-1]))
        counter2+=1
    #uses word_pair_list function to get the list of tuples of word pairs. uses
    #a for loop to print the first 5 and last 5 elements in the list if the length is 
    #greater than 10, and if not it prints all of the values
    print("4. Word pairs for document {}".format(doc2))
    wordpair2 = word_pair_list(doc2list,max_sep)
    print("  "+str(len(wordpair2)) +" distinct pairs")
    if len(wordpair2)>10:
        for tup1 in wordpair2[:5]:
            print("  "+tup1[0]+" "+tup1[1])
        print("  ...")
        for tup1 in wordpair2[-5:]:
            print("  "+tup1[0]+" "+tup1[1])
    else:
        for tup1 in wordpair2:
            print("  "+tup1[0]+" "+tup1[1])
    #finds the ratio between total_pair and word_pair_list of the wordlist
    print("5. Ratio of distinct word pairs to total: {:.3f}".format(len(word_pair_list(doc2list,max_sep))/len(total_pair(doc2list,max_sep))))
    print()
    
    """This is the summary code"""
    
    print("Summary comparison")
    #uses the average length functions with each of the lists to find which is higher
    #and prints it
    if avg_length(doc1list)>avg_length(doc2list):
        print("1. {} on average uses longer words than {}".format(doc1,doc2))
    else:
        print("1. {} on average uses longer words than {}".format(doc2,doc1))
    #uses the get_jaccard to compare the two wordlists for similarity
    print("2. Overall word use similarity: {:.3f}".format(get_jaccard(doc1list,doc2list)))
    #using the list with the highest length as the range, this code checks the index
    #of both lists of sets(for each document) and uses get_jaccard to compare them and
    #print the similarity
    print("3. Word use similarity by length:")
    maxrange = max(len(length1),len(length2))
    for num in range(maxrange):
        print("{:4d}:".format(num+1),end=(" "))
        if num > len(length1)-1:
            print("{:.4f}".format(0))
        elif num > len(length2)-1:
            print("{:.4f}".format(0))
        else:
            print("{:.4f}".format(get_jaccard(length1[num], length2[num])))
    #uses the get_jaccard function with the wordlists for each of the documents and prints out the value
    print("4. Word pair similarity: {:.4f}".format(get_jaccard(wordpair1,wordpair2)))