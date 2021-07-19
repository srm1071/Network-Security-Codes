# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 00:16:18 2021

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

inp=input('Input String: ')

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
for i in range(len(bina)):
    if i%2==0:
        s1=s1+bina[i]
        sub.append(i)
    else:
        s2=s2+bina[i]
    
f= s1[0:len(s1)//2]
s= s1[len(s1)//2 if len(s1)%2 == 0 else ((len(s1)//2)+1):]
s3x=f+bina+s
print('Encrypted string is: ',decode1(f+bina+s))
s3=decode2(s3x,sub)
print('Decrypted string is: ',decode1(s3))