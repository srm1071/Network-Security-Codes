# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 20:51:04 2021

@author: suraj
"""
import numpy as np

inp=input("Input String of length 4: ")

while(len(inp)!=4):
    print('please enter 4 character string for a key.')
    inp=input()
bina=''.join(format(ord(i), '08b') for i in inp)
print(bina)
bina1=[]
str=''
str1=[]
t1=''
t2=''

lst1=bina[0:4]
lst2=bina[4:8]
inner1= [lst1, lst2]
print(inner1)

lst1=bina[8:12]
lst2=bina[12:16]
inner2= [lst1, lst2]

lst1=bina[16:20]
lst2=bina[20:24]
inner3= [lst1, lst2]

lst1=bina[24:28]
lst2=bina[28:32]
inner4= [lst1, lst2]

print(inner1,inner2,inner3,inner4)
inner1[1]=inner1[1]+inner1[0][0]
inner2[1]=inner2[1]+inner2[0][0]
inner3[1]=inner3[1]+inner3[0][0]
inner4[1]=inner4[1]+inner4[0][0]
print(inner1,inner2,inner3,inner4)

inner1[0]=inner1[0]+inner1[1][4]
inner2[0]=inner2[0]+inner2[1][4]
inner3[0]=inner3[0]+inner3[1][4]
inner4[0]=inner4[0]+inner4[1][4]
print(inner1,inner2,inner3,inner4)
inner1[0]=inner1[1]+inner1[1][0]
inner2[0]=inner2[1]+inner2[1][0]
inner3[0]=inner3[1]+inner3[1][0]
inner4[0]=inner4[1]+inner4[1][0]
print(inner1,inner2,inner3,inner4)
inner1[1]=inner1[0][4]+inner1[1]
inner2[1]=inner2[0][4]+inner2[1]
inner3[1]=inner3[0][4]+inner3[1]
inner4[1]=inner4[0][4]+inner4[1]
print(inner1,inner2,inner3,inner4)

str1=inner1+inner2+inner3+inner4
for i in range(8):
    str=str+str1[i]

print('Output is',str)

            
            
            
            
    