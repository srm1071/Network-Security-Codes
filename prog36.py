# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 22:43:38 2021

@author: suraj
"""
import numpy as np
def zerolistmaker(n):
    listofzeros = [0] * n
    return listofzeros

def decode1(str):
    message = ""
    while str != "":
        i = chr(int(str[:8], 2))
        message = message + i
        str = str[8:]
    return message

def decode2(bina,sub):
    n1=len(bina)
    n2=len(sub)
    ss=bina[(n2//2):(n1-(n2//2))]
    return ss

inp=input("Input String: ")
#abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijkl
while(len(inp)!=64):
    print('please enter 8 character string for a key.')
    inp=input()
bina=''.join(format(ord(i), '08b') for i in inp)
sub=[]
nterms = len(bina)

n1, n2 = 0, 1
count = 0
if nterms <= 0:
   print("Please enter a positive integer")
# if there is only one term, return n1
elif nterms == 1:
   
  sub.append(n1)
else:
   print("Fibonacci sequence:")
   while n1<=len(bina):
       sub.append(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth

print(sub)
sub1=[]
s1=''
sub2=[]
s2=''
count=0
for i in range(len(sub)):
    n=sub[i]
    sub1.append(bina[n])
    s1=s1+bina[n]
for i in range(len(bina)):
    for j in range(len(sub)):
        if (i==sub[j]):
            count=1
    if count==0:
        sub2.append(bina[i])
        s2=s2+bina[i]
    count=0

f= s1[0:len(s1)//2]
s= s1[len(s1)//2 if len(s1)%2 == 0 else ((len(s1)//2)+1):]
s3x=f+bina+s
print('Encrypted string is: ',decode1(f+bina+s))
s3=decode2(s3x,sub)
print('Decrypted String is: ',decode1(s3))
