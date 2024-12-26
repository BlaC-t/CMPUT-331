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
CMPUT 331 Assignment 2 Student Solution
September 2023
Author: Zhiyu Li (Titus)
"""

from typing import List
import math

def encryptMessage(key: List[int], message: str):
    enMsg = ""

    # initiate total column number and row number for transposition matrix
    colNumber = len(key)
    rowNumber = math.ceil(len(message)/len(key))

    # Generate an matrix with calculated row and col size that is filled with value: None
    keyMsg = [[None for i in range(colNumber)] for j in range(rowNumber)]

    # loop through the message and put each letter in message into the matrix
    col = 0
    row = 0
    for eachLetter in message:
        keyMsg[row][col] = eachLetter
        
        # Go through the matrix row by row 
        if col == (colNumber-1):
            col = 0
            row += 1
        else:
            col += 1

    # All the key will be -1 to get the correct colmn number
    modKey = []
    for i in key:
        i -= 1
        modKey.append(i)

    # Go through the matrix top to bottom, and read all value thats not None into encrypt msg
    for i in range(len(modKey)):
        for j in range(rowNumber):
            if keyMsg[j][modKey[i]] == None:
                continue

            enMsg += keyMsg[j][modKey[i]]

    return enMsg


def test():
    assert encryptMessage([2, 4, 1, 5, 3], "CIPHERS ARE FUN") == "IS HAUCREERNP F"
    assert encryptMessage([1, 3, 2], "ABCDEFG") == "ADGCFBE"
    assert encryptMessage([2, 1], "HELLO WORLD") == "EL OLHLOWRD"
    

from sys import flags

if __name__ == "__main__" and not flags.interactive:
    test()
