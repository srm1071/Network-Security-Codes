# -*- coding: utf-8 -*-
"""
Created on Mon May 31 16:18:57 2021

@author: suraj
"""
def transform(inp):
    bina=''.join(format(ord(i), '08b') for i in inp)
    print(bina)
    arr1=[]
    n=len(bina)
    
    for i in range(n):
        if((i+1)%8!=0):
            arr1.append(bina[i])
            
    return arr1

def keyto48(arr,key_comp):
    arr1=[]
    for i in range(48):
        k=key_comp[i]
        arr1.append(arr[k-1])
    return arr1

shift_tab= [1, 1, 2, 2,2, 2, 2, 2, 
            1, 2, 2, 2,2, 2, 2, 1 ]

key_comp = [14, 17, 11, 24, 1, 5, 
            3, 28, 15, 6, 21, 10, 
            23, 19, 12, 4, 26, 8, 
            16, 7, 27, 20, 13, 2, 
            41, 52, 31, 37, 47, 55, 
            30, 40, 51, 45, 33, 48, 
            44, 49, 39, 56, 34, 53, 
            46, 42, 50, 36, 29, 32 ]

arr=[]
arr3=[]
arr4=[]
ss=''
inp=input('enter input string: ')
while(len(inp)!=8):
    print('please enter 8 character string for a key.')
    inp=input()
    
arr2=transform(inp)
arr3=arr2[0:28]
arr4=arr2[28:56]
for i in range(0,16):
    n=shift_tab[i]
    arr3=(arr3[-n:] + arr3[:-n])
    arr4=(arr4[-n:] + arr4[:-n])
    comb=arr3+arr4
    comb=keyto48(comb,key_comp)
    
for i in range(len(comb)):
    ss=ss+comb[i]
    
print('output is: ', ss)
print('output bit length is: ', len(ss))
    
    