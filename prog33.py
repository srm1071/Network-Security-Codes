# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 14:10:15 2021

@author: suraj
"""


errorMessage = "Error: Length of Key Must be = Length of Plaintext"

def zerolistmaker(n):
    listofzeros = [0] * n
    return listofzeros

def Encryption(plain):
    cypher=zerolistmaker(len(plain))
    cyp=''
    i=0
    while i+2<=(len(plain)):
        cypher[i]=plain[i]
        cypher[i+1]=chr(ord(plain[i]) ^ ord(plain[i+1]))
        i=i+2   
    for i in range(len(cypher)):
        cyp=cyp+str(cypher[i])

    return cyp
        
plain = str(input("Enter the plaintext : "))
while(len(plain)!=16):
    print('please enter 16 character string for a key.')
    plain=input()
ciphertext = Encryption(plain)
print("Encrypted ciphertext is : ", ciphertext)
plaintext = Encryption(ciphertext)
print("Decrypted plaintext is  : ", plaintext)

