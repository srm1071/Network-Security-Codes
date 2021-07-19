# -*- coding: utf-8 -*-
"""
Created on Sun May 30 08:19:27 2021

@author: suraj
"""
import binascii

initial_perm=[58, 50, 42, 34, 26, 18, 10, 2,
              60, 52, 44, 36, 28, 20, 12, 4,
              62, 54, 46, 38, 30, 22, 14, 6,
              64, 56, 48, 40, 32, 24, 16, 8,
              57, 49, 41, 33, 25, 17, 9, 1,
              59, 51, 43, 35, 27, 19, 11, 3,
              61, 53, 45, 37, 29, 21, 13, 5,
              63, 55, 47, 39, 31, 23, 15, 7 ];
out=""
out2=""
arr1=[]
inp=input('input a 8 character string: ')

while(len(inp)!=8):
    print('please enter 8 character string for a key.')
    inp=input()

bina=''.join(format(ord(i), '08b') for i in inp)

for i in range (0,len(bina),6):
    decim=int(bina[i:i+6], 2)
    perm=initial_perm[decim]
    out=out+str(perm)
    arr1.append(perm)

bina2=''.join(format((i), '06b') for i in arr1)
print('output is: ', out)