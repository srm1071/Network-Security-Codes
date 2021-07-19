# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 10:19:32 2021

@author: suraj
"""

errorMessage = "Error: Length of Key Must be >= Length of Plaintext"
mappingsDict = {}

def main():
    plaintext = input("Enter the plaintext : ")
    key = input("Enter the key (length should be >= length of plaintext) : ")
    print()
    alphabets = "abcdefghijklmnopqrstuvwxyz".upper()
    # Initializing values to alphabets
    for alphabet in alphabets:
        mappingsDict[alphabet] = ord(alphabet) - 65

    plaintext = plaintext.upper()
    key = key.upper()
    
    if len(key) < len(plaintext):
        print(errorMessage)
    else:
        ciphertext = vernamEncryption(plaintext, key)
        plaintext = vernamDecryption(ciphertext, key)

        print()
        print("Encrypted ciphertext is : ", ciphertext)
        print("Decrypted plaintext is  : ", plaintext)
        print()
    return

def vernamEncryption(plaintext, key):
    """Function to encrypt the plaintext using Vernam Encryption."""

    # Initializing ciphertext
    ciphertext = ''

    for i in range(len(plaintext)):
        ptLetter = plaintext[i]
        keyLetter = key[i]
        # Performing vernam encryption step
        sum = mappingsDict[ptLetter] + mappingsDict[keyLetter]
        # Subtracting 26 if sum overflows above values
        if sum >= 26:
            sum -= 26
        # Adding to ciphertext
        ciphertext += chr(sum + 65)

    # Returning ciphertext
    return ciphertext

def vernamDecryption(ciphertext, key):
    plaintext = ''

    for i in range(len(ciphertext)):
        ctLetter = ciphertext[i]
        keyLetter = key[i]
        diff = mappingsDict[ctLetter] - mappingsDict[keyLetter]
        if diff < 0:
            diff += 26
        plaintext += chr(diff + 65)
    return plaintext


if __name__ == "__main__":
    main()