#!/usr/bin/env python3

#---------------------------------------------------------------
#
# CMPUT 331 Student Submission License
# Version 1.0
# Copyright 2023 Zhiyu Li
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
Subsititution cipher frequency analysis
"""
ETAOIN = "ETAOINSHRDLCUMWFGYPBVKJXQZ"
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
from sys import flags
from collections import Counter # Helpful class, see documentation or help(Counter)
import itertools

def freqDict(ciphertext: str) -> dict:
    """
    Analyze the frequency of the letters
    """

    # set up dictionary
    tempDict = dict(zip(list(LETTERS), list(itertools.repeat(-1, len(list(LETTERS))))))
    fDict = {}

    # dictionary for the locations of letters last appear in the text
    for i in ciphertext:
        if i in tempDict:
            lastFound = ciphertext.rfind(i)
            tempDict[i] = lastFound
    
    # sort location dictionary
    # https://www.freecodecamp.org/news/sort-dictionary-by-value-in-python/
    tempDict = dict(sorted(tempDict.items(), key=lambda x:x[1], reverse=True))
    # print(tempDict)

    # find frequency of letters into dict
    countDict = dict(Counter(ciphertext))
    # print(countDict)
    
    # sort frequency of letters into dict
    sortedDict = dict(sorted(countDict.items(), key=lambda x:x[1], reverse=True))
    
    modList = []
    maxValue = 0

    # compare the number of time it appears, if the number is the seem, compare location,
    # whoever ends first goes first
    for i in sortedDict:
        # sort out none alphas
        if i not in tempDict:
            continue
        
        # if modified list contain values, then check for comprison
        if len(modList) != 0:
            # if larger than max value, just added to the front
            if sortedDict[i] > maxValue:
                maxValue = sortedDict[i]
                modList.insert(0, i)
                continue
            
            # if not then extract the letter with same value, compare location, 
            # who ends first, who goes first
            for eachLetter in modList:
                # find the letter with the same value, if find check location,
                # if did not end earlier, continue
                if sortedDict[eachLetter] == sortedDict[i]:
                    if tempDict[eachLetter] > tempDict[i]:
                        modList.insert(modList.index(eachLetter), i)
                    else:
                        continue
                    
                # skip if the letter value is larger
                if sortedDict[eachLetter] > sortedDict[i]:
                    continue
                # replace if the letter value is smaller
                if sortedDict[eachLetter] < sortedDict[i]:
                   modList.insert(modList.index(compareLetter), i)
                

            # if its the smallest, append
            if sortedDict[i] < sortedDict[modList[-1]]:
                modList.append(i)

        else:
            # initial case
            modList.append(i)
            maxValue = sortedDict[i]


    corList = list(ETAOIN)
    pos = 0
    for i in corList:
        if pos < len(modList):
            fDict[modList[pos]] = i
            pos += 1
    
    return fDict
    
    

def freqDecrypt(mapping: dict, ciphertext: str) -> str:
    """
    Apply the mapping to ciphertext
    """
    deMsg = ""
    for eachLetter in ciphertext:
        if eachLetter in mapping.keys():
            deMsg += mapping[eachLetter]
        else:
            deMsg += eachLetter
    
    return deMsg

def test():
    "Run tests"
    assert type(freqDict("A")) is dict
    
    assert freqDict("AAAAAAAAAAAAAAAAAAAAAAAAAAAAA")["A"] == "E"
    assert freqDict("AABBA")['B'] == "T"
    assert freqDict("-: AB CD AH")['A'] == "E"
    assert freqDecrypt({"A": "E", "Z": "L", "T": "H", "F": "O", "U": "W", "I": "R", "Q": "D"}, "TAZZF UFIZQ!") == "HELLO WORLD!"
    

# Invoke test() if called via `python3 a5p1.py`
# but not if `python3 -i a5p1.py` or `from a5p1 import *`
if __name__ == '__main__' and not flags.interactive:
    test()
