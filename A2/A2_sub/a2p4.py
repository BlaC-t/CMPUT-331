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

def decryptMessage(key: List[int], message: str):
    deMsg = ""

    # initiate total column number and row number for transposition matrix
    colNumber = len(key)
    rowNumber = math.ceil(len(message)/len(key))

    # Generate an matrix with calculated row and col size that is filled with value: None
    keyMsg = [[None for i in range(colNumber)] for j in range(rowNumber)]

    # All the key will be -1 to get the correct colmn number
    modKey = []
    for i in key:
        i -= 1
        modKey.append(i)

    # Put all the message into the matrix col by col while working with the key
    pos = 0
    for i in range(colNumber):
        for j in range(rowNumber):
            keyMsg[j][modKey[i]] = message[pos]
            pos += 1

    # Read the matrix left to right, row by row, and plug it into the decrypt msg for answer
    for i in range(rowNumber):
        for j in range(colNumber):
            if(keyMsg[i][j] == None):
                continue
            deMsg += keyMsg[i][j]
    
    return deMsg

def test():
    f = open("mystery.txt", "r").read()
    d = decryptMessage([8,1,6,2,10,4,5,3,7,9], f)
    newFile = open("mystery.dec.txt", "w").write(d)
    
from sys import flags

if __name__ == "__main__" and not flags.interactive:
    test()
