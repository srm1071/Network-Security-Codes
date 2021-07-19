# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 16:30:26 2021

@author: suraj
"""


def rail_fence(word):
    res=""
    
    for i in range(len(word)):
        if(i%2==0):
            res=res+word[i]
    for i in range(len(word)):
        if(i%2!=0):
            res=res+word[i]
            
    return res

text="Come home tomorrow"
print("input is: ", text)
text=text.replace(" ", "")
print('Output is: ', rail_fence(text))