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
import numpy as np

def encryptMessage(key: int, message: str):
    # initiate encoded msg and nested list with same value (a value will not be in any text)
    enMsg = ""
    keyMsg = [[None for i in range(len(message))] for j in range(key)]
    
    # initiate row and col
    row = 0
    col = 0
    
    # set up flags for direction
    up = False
    for eachLetter in message:
        # assign letter to the nested list 
        keyMsg[row][col] = eachLetter
        col += 1

        # if the row number reach the top, direction changes. if the row number is zero, also change direction
        if row == (key - 1):
            up = True
        elif row == 0:
            up = False

        # check direct states, to see if i need to increase or decrease
        if row >= 0 and not up:
            row += 1
        else:
            row -= 1

    # Pull all the letter out from matrix horizontally, and added it to the encoded msg string
    for i in range(key):
        for j in range(len(message)):
            if keyMsg[i][j] != None:
                enMsg += keyMsg[i][j]
    
    return enMsg
        

    

def decryptMessage(key: int, message: str):
    # initiate decoded msg and nested list with same value (a value will not be in any text)
    deMsg = ""
    # https://stackoverflow.com/questions/74906565/python-creating-a-nested-list-with-value-using-one-line-code
    keyMsg = [[None for i in range(len(message))] for j in range(key)]

    row = 0
    col = 0

    # set up flags for direction
    up = False
    for eachLetter in message:
        # assign '\n' to the position of letters in the nested list 
        keyMsg[row][col] = "\n"
        col += 1

        # if the row number reach the top, direction changes. if the row number is zero, also change direction
        if row == (key - 1):
            up = True
        elif row == 0:
            up = False

        # check direct states, to see if i need to increase or decrease
        if row >= 0 and not up:
            row += 1
        else:
            row -= 1

    # Plug in the decode msg in to the matrix line by line
    pos = 0
    for i in range(key):
        for j in range(len(message)):
            if keyMsg[i][j] == '\n':
                keyMsg[i][j] = message[pos]
                pos += 1
    
    # Reset col and row, for next iterations of matrix
    col = 0
    row = 0

    # set up flags for direction
    up = False
    for eachLetter in message:
        # Go through the entire matrix in zip zap form, if the content does not equal to None, added to the back of the decoded string
        if keyMsg[row][col] != None:
            deMsg += keyMsg[row][col]
        col += 1

        # if the row number reach the top, direction changes. if the row number is zero, also change direction
        if row == (key - 1):
            up = True
        elif row == 0:
            up = False

        # check direct states, to see if i need to increase or decrease
        if row >= 0 and not up:
            row += 1
        else:
            row -= 1
    
    return deMsg

def test():
    assert decryptMessage(2, encryptMessage(2, "SECRET")) == "SECRET"
    assert decryptMessage(3, encryptMessage(3, "CIPHERS ARE FUN")) == "CIPHERS ARE FUN"
    assert decryptMessage(4, encryptMessage(4, "HELLO WORLD")) == "HELLO WORLD"
    

from sys import flags

if __name__ == "__main__" and not flags.interactive:
    test()
