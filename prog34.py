# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 18:48:23 2021

@author: suraj
"""

errorMessage = "Error: Length of Key Must be = Length of Plaintext"

def decode1(str):
    message = ""
    while str != "":
        i = chr(int(str[:8], 2))
        message = message + i
        str = str[8:]
    return message

def zerolistmaker(n):
    listofzeros = [0] * n
    return listofzeros

def Encryption(plain):
    cypher=zerolistmaker(len(plain)+2)
    cyp=''
    i=0
    while i<(len(plain)):
        cypher[i]=plain[i]
        if (plain[i] == plain[i+1]):
            cypher[i+1]= "0"
        else:
            cypher[i+1]= "1"
        i=i+2
        
    for i in range(len(cypher)-2):
        cyp=cyp+str(cypher[i])
    return cyp
    
inp= str(input("Enter the plaintext : "))
while(len(inp)!=16):
    print('please enter 16 character string for a key.')
    inp=input()

plain=''.join(format(ord(i), '08b') for i in inp)

ciphertext = Encryption(plain)
print("Encrypted ciphertext is : ", decode1(ciphertext))
plaintext = Encryption(ciphertext)
print("Decrypted plaintext is  : ", decode1(plaintext))

