# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 20:19:59 2021

@author: suraj
"""
import binascii

errorMessage = "Error: Length of Key Must be = Length of Plaintext"
def Encryption(plain):
    cypher=[]
    i=0
    stt=''
    while i+4<=(len(plain)):
        a=chr(ord(plain[i]) ^ ord(plain[i+1]))
        b=chr(ord(a) ^ ord(plain[i+2]))
        c=chr(ord(b) ^ ord(plain[i+3]))
        
        cypher.append(c)
        cypher.append(c)
        cypher.append(plain[i+2])
        cypher.append(plain[i+3])
        i=i+4
        
    if (len(plain)-len(cypher))>0:
        n=len(plain)
        k=len(cypher)
        while k<n:
            t=plain[k]
            cypher.append(t)
            k=k+1

    return cypher
           
plain = str(input("Enter the plaintext : "))
plain=list(plain)

ciphertext = Encryption(plain)
print("Encrypted ciphertext is : ", ciphertext)
        #print("Decrypted plaintext is  : ", plaintext)
