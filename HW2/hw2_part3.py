# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 14:37:13 2022

@author: Nevin Joshy
"""
sent = input("Enter a sentence => ").strip()
print(sent)
sent = sent.lower()

def number_happy(phrase):
    count = 0
    count += phrase.count("laugh")
    count += phrase.count("happiness")
    count += phrase.count("love")
    count += phrase.count("excellent")
    count += phrase.count("good")
    count += phrase.count("smile")
    return count

def number_sad(phrase):
    count = 0
    count += phrase.count("bad")
    count += phrase.count("sad")
    count += phrase.count("terrible")
    count += phrase.count("horrible")
    count += phrase.count("problem")
    count += phrase.count("hate")
    return count

happy = number_happy(sent)
sad= number_sad(sent)
sentiment = ("+"*happy)+("-"*sad)
mood = ""

if happy>sad:
    mood = "happy"
elif sad>happy:
    mood = "sad"
else: 
    mood = "neutral"
    
print("Sentiment: "+sentiment)
print("This is a {:s} sentence.".format(mood))