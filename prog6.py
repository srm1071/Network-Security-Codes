# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 16:13:02 2021

@author: suraj
"""

initial_perm= [40, 8, 48, 16, 56, 24, 64, 32,
        39, 7, 47, 15, 55, 23, 63, 31,
        38, 6, 46, 14, 54, 22, 62, 30,
        37, 5, 45, 13, 53, 21, 61, 29,
        36, 4, 44, 12, 52, 20, 60, 28,
        35, 3, 43, 11, 51, 19, 59, 27,
        34, 2, 42, 10, 50, 18, 58, 26,
        33, 1, 41, 9, 49, 17, 57, 25]

out=""
out2=""
arr1=[]
inp=input('input is: ')

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


print('output is:', out)