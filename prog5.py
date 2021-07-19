# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 00:36:39 2021

@author: suraj
"""
import binascii

P = [16, 7, 20, 21, 29, 12, 28, 17,
     1, 15, 23, 26, 5, 18, 31, 10,
     2, 8, 24, 14, 32, 27, 3, 9,
     19, 13, 30, 6, 22, 11, 4, 25]

out=""
out2=""
arr1=[]
inp=input('input: ')

while(len(inp)!=4):
    print('please enter 4 character to feed to P-Box.')
    inp=input()

bina=''.join(format(ord(i), '08b') for i in inp)

for i in range (0,len(bina),5):
    decim=int(bina[i:i+5], 2)
    perm=P[decim]
    out=out+str(perm)
    arr1.append(perm)

bina2=''.join(format((i), '08b') for i in arr1)
print('output is:', out)
