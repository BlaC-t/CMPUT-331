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
    assert key in LETTERS
    # set up key and encrypt msg string
    enMsg = ""
    shiftAmt = SHIFTDICT[key]

    # Check every single letter in the plain message
    for eachLetter in message:
        # check if the letter is a character, if its not append to msg no matter what
        if not eachLetter.isalpha() or eachLetter not in LETTERS:
            enMsg += eachLetter
            continue

        letterPos = SHIFTDICT[eachLetter]

        # check for the added position if its over 52 or not 
        enPos = letterPos + shiftAmt
        if (enPos < len(LETTERS)):
            enMsg += LETTERDICT[enPos]
        else:
            enPos -= len(LETTERS)
            enMsg += LETTERDICT[enPos]
        
        # the algorithm requires us to use the previous letter as the shifting amount for next,
        # there we need to re-assign it to the shifting amount for the next avalible letter in the msg
        shiftAmt = SHIFTDICT[eachLetter]

    return enMsg

def decrypt(message: str, key: str):
    assert key in LETTERS
    # set up key and decrypt msg string
    deMsg = ""
    shiftAmt = len(LETTERS) - SHIFTDICT[key]

    # Check every single letter in the encrypt message
    for eachLetter in message:
        # check if the letter is a character, if its not append to msg no matter what
        if not eachLetter.isalpha() or eachLetter not in LETTERS:
            deMsg += eachLetter
            continue

        letterPos = SHIFTDICT[eachLetter]
        # It's different then part 1 and the encrypt part cuz it need to record what
        # the previous letter has become and change according to it
        enLetter = ""

        dePos = letterPos + shiftAmt
        if (dePos < len(LETTERS)):
            enLetter = LETTERDICT[dePos]
            deMsg += enLetter
        else:
            dePos -= len(LETTERS)
            enLetter = LETTERDICT[dePos]
            deMsg += enLetter
        
        shiftAmt = len(LETTERS) - SHIFTDICT[enLetter]

    return deMsg

def test():
    global SHIFTDICT, LETTERDICT 
    SHIFTDICT, LETTERDICT = get_map()
    # print(encrypt("Welcome to 2023 Fall CMPUT 331!", "y"))
    # print(decrypt("uaQORBR YI 2023 tfMX nOBJN 331!", "y"))
    # assert decrypt(encrypt("foo", "g"), "g") == "foo"

if __name__ == "__main__" and not flags.interactive:
    test()