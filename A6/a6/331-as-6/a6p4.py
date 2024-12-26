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
Problem 4
"""

from sys import flags
from string import ascii_uppercase
from a6p1 import ngramsFreqsFromFile
from a6p3 import bestSuccessor

ETAOIN = "ETAOINSHRDLCUMWFGYPBVKJXQZ"


def breakSub(
    cipherFile: "str path to a cipher file", textFile: "str path to a text file", n: int
) -> None:
    """
    Inputs:
        cipherFile:
            'text_finnegan_cipher.txt' for implementation
            'text_cipher.txt' for submission
        textFile: 'wells.txt'
    Outputs:
        'text_finnegan_plain.txt' for implementation
        'text_plain.txt' for submission
    """
    cipherF = open(cipherFile, "r").read()

    # map the more frequently used ciphertext to english letter
    freqList = []
    for i in range(len(cipherF)):
        if cipherF[i] != " ":
            freqList.append(cipherF[i])

    # find the number of each letter
    numDict = {}
    for i in freqList:
        if i not in numDict.keys():
            numDict[i] = 1
        else:
            numDict[i] += 1

    for i in ascii_uppercase:
        if i not in numDict:
            numDict[i] = 0

    # sort the dict
    sortDict = dict(sorted(numDict.items(), key=lambda x: x[1], reverse=True))
    sortKeys = list(sortDict.keys())

    englishFreq = ngramsFreqsFromFile(textFile, 1)
    englishFreq.pop(" ", None)
    englishFreq = dict(sorted(englishFreq.items(), key=lambda x: x[1], reverse=True))
    englishFreqkey = list(englishFreq.keys())

    # print(englishFreqkey)

    # avoid 0 appearance
    for i in ascii_uppercase:
        if i not in englishFreqkey:
            englishFreqkey.append(i)

    mapDict = {}
    # map to english frequency
    for i in range(len(englishFreqkey)):
        mapDict[sortKeys[i]] = englishFreqkey[i]
    mapDict[" "] = " "

    # print(mapDict)

    # get frequencies for cipherFile
    frequencies = ngramsFreqsFromFile(textFile, n)

    # while loop until find the best matching map
    prevBestMap = bestSuccessor(mapDict, cipherF, frequencies, n)
    curBestMap = bestSuccessor(prevBestMap, cipherF, frequencies, n)

    while curBestMap != prevBestMap:
        prevBestMap = curBestMap
        curBestMap = bestSuccessor(prevBestMap, cipherF, frequencies, n)

    # use the map to creat decipherment
    deMsg = ""
    for i in cipherF:
        deMsg += curBestMap[i]

    f = open("text_plain.txt", "w").write(deMsg)


def test():
    "Run tests"  # TODO: test thoroughly by writing your own regression tests
    # This function is ignored in our marking
    breakSub("text_cipher.txt", "well.txt", 3)


if __name__ == "__main__" and not flags.interactive:
    test()
