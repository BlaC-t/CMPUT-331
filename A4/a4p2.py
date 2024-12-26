#!/usr/bin/env python3

#---------------------------------------------------------------
#
# CMPUT 331 Student Submission License
# Version 1.0
# Copyright 2023 <<Insert your name here>>
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

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def translateMessage(key: str, message: str, codebook: dict, mode: str):
    """
    Encrypt or decrypt using a nomenclator.
    Takes a substitution cipher key, a message (plaintext or ciphertext),
    a codebook dictionary, and a mode string ('encrypt' or 'decrypt')
    specifying the action to be taken. Returns a string containing the
    ciphertext (if encrypting) or plaintext (if decrypting).
    """
    raise NotImplementedError()


def encryptMessage(key: str, codebook: dict, message: str):
    return translateMessage(key, codebook, message, 'encrypt')


def decryptMessage(key: str, codebook: dict, message: str):
    return translateMessage(key, codebook, message, 'decrypt')


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

