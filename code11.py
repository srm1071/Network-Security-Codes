# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 16:15:24 2021

@author: suraj
"""

def ceaser_enc(text,s):
    result = ""
    
    for i in range(len(text)):
        word = text[i]
        if (word.isupper()):
            result= result+ chr((ord(word) + s-65) % 26 + 65)
        else:
            result= result+ chr((ord(word) + s - 97) % 26 + 97)
    return result
 
    
text = "Come Home Tomorrow"
s=int(input())
print('number is: ', s)
print ("PlainText is : " + text)
print ("CipherText is : " + ceaser_enc(text,s))
