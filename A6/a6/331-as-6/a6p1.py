#!/usr/bin/env python3

# ---------------------------------------------------------------
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
# ---------------------------------------------------------------

"""
Problem 1
"""

from sys import flags
import re


def ngramsFreqsFromFile(textFile: "str path to a text file", n: int) -> dict:
    """
    textFile: 'wells.txt'
    """
    f = open(textFile, "r").read()

    # get all the substring based on n from txt file
    nGramList = []
    for i in range(len(f)):
        sub = f[i : i + n]
        if len(sub) == n:
            nGramList.append(sub)

    # get the number of times it appears in the list
    numDict = {}
    for i in nGramList:
        if i not in numDict.keys():
            numDict[i] = 1
        else:
            numDict[i] += 1

    # calculate the frequency of such substring
    freqDict = {}
    for i in numDict:
        freqDict[i] = numDict[i] / len(nGramList)

    return freqDict


def test():
    "Run tests"
    # TODO: test thoroughly by writing your own regression tests
    # This function is ignored in our marking


if __name__ == "__main__" and not flags.interactive:
    test()
