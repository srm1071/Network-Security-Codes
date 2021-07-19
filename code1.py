# -*- coding: utf-8 -*-
"""
Created on Mon May 24 08:52:18 2021

@author: suraj
"""
inp=input("Input String: ")

while(len(inp)!=8):
    print('please enter 8 character string for a key.')
    inp=input()

bina=''.join(format(ord(i), '08b') for i in inp)

arr1=''
n=len(bina)

for i in range(n):
    if((i+1)%8!=0):
        arr1=arr1+bina[i]

print('new bitstream is: ',arr1)    
print('length of new bitstream is: ', len(arr1))