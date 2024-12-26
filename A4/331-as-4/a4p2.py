#!/usr/bin/env python3

#---------------------------------------------------------------
#
# CMPUT 331 Student Submission License
# Version 1.0
# Copyright 2023 Zhiyu Li (Titus)
#
# Redistribution is forbidden in all circumstances. Use of this software
# without explicit authorization from the author is prohibited.
#
# This software was produced as a solution for an assignment in the course
# CMPUT 331 - Computational Cryptography at the University of
# Alberta, Canada. This solution is confidential and remains confidential 
# after it is submitted for grading.
#
# Copying any part of this solution without including this copyright notice
# is illegal.
#
# If any portion of this software is included in a solution submitted for
# grading at an educational institution, the submitter will be subject to
# the sanctions for plagiarism at that institution.
#
# If this software is found in any public website or public repository, the
# person finding it is kindly requested to immediately report, including 
# the URL or other repository locating information, to the following email
# address:
#
#          gkondrak <at> ualberta.ca
#
#---------------------------------------------------------------

"""
Nomenclator cipher
"""

import random, sys

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def translateMessage(key: str, message: str, codebook: dict, mode: str):
    """
    Encrypt or decrypt using a nomenclator.
    Takes a substitution cipher key, a message (plaintext or ciphertext),
    a codebook dictionary, and a mode string ('encrypt' or 'decrypt')
    specifying the action to be taken. Returns a string containing the
    ciphertext (if encrypting) or plaintext (if decrypting).
    """

    # validating given simple key
    keyList = list(key)
    lettersList = list(LETTERS)
    keyList.sort()
    lettersList.sort()
    if keyList != lettersList:
        sys.exit('There is an error in the key or symbol set.')

    # setting up for translation
    translated = ''
    charsA = LETTERS
    charsB = key

    # decrypt
    if mode == 'decrypt':
        # For decrypting, we can use the same code as encrypting. We
        # just need to swap where the key and LETTERS strings are used.
        charsA, charsB = charsB, charsA

        # loop through each symbol in the message
        for symbol in message:
            if symbol.isnumeric():
                for i in codebook.values():
                    if symbol in i:
                        # Using a value to find the key that contains a list of values
                        # https://note.nkmk.me/en/python-dict-get-key-from-value/
                        keys = [k for k, v in codebook.items() if v == i][0]
                        translated += str(keys)
                    else:
                        continue
            elif symbol.upper() in charsA:
                # encrypt/decrypt the symbol
                symIndex = charsA.find(symbol.upper())
                if symbol.isupper():
                    translated += charsB[symIndex].upper()
                else:
                    translated += charsB[symIndex].lower()
            else:
                # symbol is not in LETTERS, just add it
                translated += symbol
    
    # encrypt
    elif mode == "encrypt":
        # create two list of words that contained in msg
        words = message.split()
        upperWords = message.upper().split()

        # create a list of upper case keys from codebook and create another list of values corresponding to the keys
        codeWords = list(codebook.keys())
        upperCodeWords = [x.upper() for x in codeWords]
        codeList = list(codebook.values())

        # loop through the word list, if anyword is found in the code keys, get a random value from the value list,
        # then replace the original word from the msg with the value
        for i in upperWords:
            if i in upperCodeWords:
                value = random.choice(codeList[upperCodeWords.index(i)])
                message = message.replace(words[upperWords.index(i)], value)
                
        # Since we have done the codebook encrpyt, now its just simple sub cypther
        for symbol in message:
                if symbol.upper() in charsA:
                    # encrypt/decrypt the symbol
                    symIndex = charsA.find(symbol.upper())
                    if symbol.isupper():
                        translated += charsB[symIndex].upper()
                    else:
                        translated += charsB[symIndex].lower()
                else:
                    # symbol is not in LETTERS, just add it
                    translated += symbol

    return translated


def encryptMessage(key: str, codebook: dict, message: str):
    return translateMessage(key, message, codebook, 'encrypt')


def decryptMessage(key: str, codebook: dict, message: str):
    return translateMessage(key, message, codebook, 'decrypt')


def test():
    # Provided test.
    key = 'LFWOAYUISVKMNXPBDCRJTQEGHZ'
    message = 'At the University of Alberta, examinations take place in December and April for the Fall and Winter terms.'
    codebook = {'university':['1', '2', '3'], 'examination':['4', '5'], 'examinations':['6', '7', '8'], 'WINTER':['9']}
    cipher = translateMessage(key, message, codebook, 'encrypt')
    print(cipher)
    print(translateMessage(key, cipher, codebook, 'decrypt'))
    # End of provided test.

if __name__ == '__main__':
    test()

