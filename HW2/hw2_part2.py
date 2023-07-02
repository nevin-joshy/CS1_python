# -*- coding: utf-8 -*-
"""
Created on Tue Sep 20 14:03:30 2022

@author: Nevin Joshy
"""

phrase = input("Enter a string to encode ==> ").strip()
print(phrase)

def encrypt(word):
    word1 = word
    word1 = word1.replace(" a", "%4%")
    word1 = word1.replace("he", "7!")
    word1 = word1.replace("e", "9(*9(")
    word1 = word1.replace("y", "*%$")
    word1 = word1.replace("u", "@@@")
    word1 = word1.replace("an", "-?")
    word1 = word1.replace("th", "!@+3")
    word1 = word1.replace("o", "7654")
    word1 = word1.replace("9", "2")
    word1 = word1.replace("ck", "%4")
    return word1

def decrypt(code):
    code1 = code
    code1 = code1.replace("%4", "ck")
    code1 = code1.replace("2", "9")
    code1 = code1.replace("7654", "o")
    code1 = code1.replace("!@+3", "th")
    code1 = code1.replace("-?", "an")
    code1 = code1.replace("@@@", "u")
    code1 = code1.replace("*%$", "y")
    code1 = code1.replace("9(*9(", "e")
    code1 = code1.replace("7!", "he")
    code1 = code1.replace("%4%", " a")
    return code1
new = encrypt(phrase)
new2 = decrypt(new)
diff = len(new)-len(phrase)

print("\nEncrypted as ==> "+new)
print("Difference in length ==>",diff)
print("Deciphered as ==> "+new2)

if new2!=phrase:
    print("Operation is not reversible on the string.")
else:
    print("Operation is reversible on the string.")