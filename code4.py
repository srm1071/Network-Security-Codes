# -*- coding: utf-8 -*-
"""
Created on Mon May 31 19:59:16 2021

@author: suraj
"""


def  expan_right(arr,exp):
    #print(len(arr))
    arr1=[]
    for i in range (48):
        k=exp[i]
        arr1.append(arr[k-1])
        
    return(arr1)

exp=[32, 1 , 2 , 3 , 4 , 5 , 4 , 5, 
     6 , 7 , 8 , 9 , 8 , 9 , 10, 11, 
     12, 13, 12, 13, 14, 15, 16, 17, 
     16, 17, 18, 19, 20, 21, 20, 21, 
     22, 23, 24, 25, 24, 25, 26, 27, 
     28, 29, 28, 29, 30, 31, 32, 1 ]

inp=input('input string: ')
while(len(inp)!=8):
    print('please enter 8 character string for a key.')
    inp=input()
ss=''  
bina=''.join(format(ord(i), '08b') for i in inp)
left=bina[0:32]
right=bina[32:64]
for i in range(0,16):
    right_perm=expan_right(right,exp)
for i in range(len(right_perm)):
    ss=ss+right_perm[i]
    
print('output is: ', ss)
print('length of output is:', len(ss))