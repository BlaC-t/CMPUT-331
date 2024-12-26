#!/usr/bin/python3

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
CMPUT 331 Assignment 1 Student Solution
September 2023
Author: Zhiyu Li (Titus)
"""


import string
from sys import flags

LETTERS = ''.join([u+l for u, l in 
    zip(string.ascii_uppercase, string.ascii_lowercase)])


def get_map(letters=LETTERS):
    enDict = {}
    deDict = {}

    # Put the corresponding value to its character and its reverse into two different dictionary
    for i in range(len(letters)):
        enDict[letters[i]] = i
        deDict[i] = letters[i]

    return enDict, deDict


def encrypt(message: str, key: str):
    # set up key and encrypt msg string
    enMsg = ""
    count = 0

    # Check every single letter in the plain message
    for eachLetter in message:
        if not eachLetter.isalpha() or eachLetter not in LETTERS:
            enMsg += eachLetter
            continue
        
        # By the addition of the counting unit, the key can return to begining whenever
        # we reach its length
        if count >= len(key):
            count = 0
        
        # Set up shift amount
        assert key[count] in LETTERS
        shiftAmt = SHIFTDICT[key[count]]
        letterPos = SHIFTDICT[eachLetter]

        # check for the added position if its over 52 or not 
        enPos = letterPos + shiftAmt
        if (enPos < len(LETTERS)):
            enMsg += LETTERDICT[enPos]
        else:
            enPos -= len(LETTERS)
            enMsg += LETTERDICT[enPos]

        count += 1
    
    return enMsg


def decrypt(message: str, key: str):
    # set up key and decrypt msg string
    deMsg = ""
    count = 0

    # Check every single letter in the encrypt message
    for eachLetter in message:
        # check if the letter is a character or in the Letter list, if its not append to msg no matter what
        if not eachLetter.isalpha() or eachLetter not in LETTERS:
            deMsg += eachLetter
            continue
        
        if count >= len(key):
            count = 0

        # Set up shift amount
        assert key[count] in LETTERS
        shiftAmt = len(LETTERS) - SHIFTDICT[key[count]]
        letterPos = SHIFTDICT[eachLetter]

        dePos = letterPos + shiftAmt
        if (dePos < len(LETTERS)):
            deMsg += LETTERDICT[dePos]
        else:
            dePos -= len(LETTERS)
            deMsg += LETTERDICT[dePos]
        
        count += 1

    return deMsg

def test():
    global SHIFTDICT, LETTERDICT 
    SHIFTDICT, LETTERDICT = get_map()
    assert decrypt(encrypt("foo", "g"), "g") == "foo"

if __name__ == "__main__" and not flags.interactive:
    test()