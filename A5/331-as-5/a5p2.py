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
Problem 2
"""

from sys import flags
import numpy as np
import sys
def evalDecipherment(text1: str, text2: str) -> [float, float]:
    """
    docstring
    """
    # initial value
    totalAlpha = 0
    rightT = 0
    rightM = 0

    if len(text1) != len(text2):
        print("Both text length are not the same!")
        sys.exit()

    letterList = []

    # loop begin
    for eachLetter in range(len(text1)):
        # if both text have letter in this location, then total location + 1
        if text1[eachLetter].isalpha() and text2[eachLetter].isalpha():
            totalAlpha += 1

            # if they are equal, total letter that matches + 1
            if text1[eachLetter] == text2[eachLetter]:
                rightT += 1
            
            # if the letter have not appeared in the list, add to the list
            # and if they are the same, similar letter + 1
            if text1[eachLetter] not in letterList:
                letterList.append(text1[eachLetter])
                if text1[eachLetter] == text2[eachLetter]:
                    rightM += 1
    

    keyAcc = rightM/len(letterList)
    decAcc = rightT/totalAlpha

    return [keyAcc, decAcc]

def test():
    "Run tests"
    
    np.testing.assert_array_almost_equal(evalDecipherment("this is an example", "tsih ih an ezample") , [0.7272727272727273, 0.7333333333333333])
    np.testing.assert_almost_equal(evalDecipherment("the most beautiful course is 331!", "tpq munt bqautiful cuurnq in 331!") , [0.7142857142857143, 0.625])
    
if __name__ == '__main__' and not flags.interactive:
    test()