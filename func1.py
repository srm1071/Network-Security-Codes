# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 10:54:11 2021

@author: suraj
"""


def zerolistmaker(n):
    listofzeros = [0] * n
    return listofzeros

def decode2(bina,sub,s1,s2):
    n1=len(bina)
    str2=zerolistmaker(n1)
    s=''
    sub2=[]
    for i in range(len(bina)):
        count=0
        for j in range(len(sub)):
          n=sub[j]
          if(i==n):
            str2[n]=s1[j]
            count=1
        if (count==0):
          sub2.append(i)
          

    for i in range(len(bina)):
        count=0
        for j in range(len(s2)):
          n=sub2[j]
          if(i==n):
            str2[n]=s2[j]


    for i in range(len(bina)):
        s=s+str(str2[i])
        
    return s