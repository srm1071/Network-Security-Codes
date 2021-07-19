# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 10:43:33 2021

@author: suraj
"""

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
while(len(inp)!=64):
    print('please enter 8 character string for a key.')
    inp=input()
bina=''.join(format(ord(i), '08b') for i in inp)
sub=[]
nterms = len(bina)
sub=[]
s1=''
sub2=[]
s2=''
count=0

for num in range(2, len(bina)):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               sub2.append(num)
               break
       else:
           sub.append(num)
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
print('Decrypted string is: ',decode1(s3))