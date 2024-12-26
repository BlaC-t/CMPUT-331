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
Assignment 7 Problem 1
"""

from sys import flags


LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# https://www.geeksforgeeks.org/vigenere-cipher/
def encode(key: str, plaintext: str):
    # create key stream
    if len(key) < len(plaintext):
        for i in range(len(plaintext) - len(key)):
            key += key[i % len(key)]

    # for each letter, first add key then module by 26 to find its place in alphbetical order
    # then add a 65 ("A") to help it find the correct code in the chart
    enMsg = ""
    for i in range(len(plaintext)):
        eachLetter = (ord(plaintext[i]) + ord(key[i])) % 26
        eachLetter += ord("A")
        enMsg += chr(eachLetter)

    return enMsg


def antiKasiski(key: str, plaintext: str):
    """
    Thwart Kasiski examination
    """
    orginalMsg = plaintext
    oriKey = key
    repeat = True
    enMsg = ""

    # look for multiple X insert
    while repeat:
        enMsg = encode(oriKey, orginalMsg)

        # find all the 3 gram
        ngram = []
        for i in range(len(enMsg)):
            sub = enMsg[i : i + 3]
            if len(sub) == 3:
                ngram.append(sub)

        # get the number of times it appears in the list
        numDict = {}
        for i in ngram:
            if i not in numDict.keys():
                numDict[i] = 1
            else:
                numDict[i] += 1

        # remove all 3-gram word only appeared once
        modDict = {}
        for key, val in numDict.items():
            if val > 1:
                modDict[key] = val

        # Terminate Condition, if not more word with len of 3 that is repeated end!
        if modDict == {}:
            repeat = False
            return enMsg

        # find the location of each apperance
        locDict = {}
        for eachWord in modDict:
            for ngramLoc in range(len(ngram)):
                if eachWord == ngram[ngramLoc]:
                    if eachWord not in locDict:
                        locDict[eachWord] = [ngramLoc]
                    else:
                        locDict[eachWord].append(ngramLoc)

        # find its location, add x then encode
        addOn = 0
        for eachWord in locDict:
            for eachLoc in locDict[eachWord]:
                if locDict[eachWord].index(eachLoc) == len(locDict[eachWord]) - 1:
                    continue

                # insert x into the end of each word while increase the length by 1
                orginalMsg = (
                    orginalMsg[: (eachLoc + 3 + addOn)]
                    + "X"
                    + orginalMsg[(eachLoc + 3 + addOn) :]
                )
                addOn += 1

        enMsg = encode(oriKey, orginalMsg)
    return enMsg


def test():
    "Run tests"
    assert (
        antiKasiski(
            "WICK",
            "THOSEPOLICEOFFICERSOFFEREDHERARIDEHOMETHEYTELLTHEMAJOKETHOSEBARBERSLENTHERALOTOFMONEY",
        )
        == "PPQCAXQVEKGYBNZSYMTCTWHPAZGNDMTKNQFODWOOPPGHUBGVHBJOTUCTKSGDDWUOXITLAZUVAVVRAZCVKBQPIWPOU"
    )

    # print(antiKasiski("WICK", "AAADAAAD"))
    # TODO: test thoroughly by writing your own regression tests
    # This function is ignored in our marking


# Invoke test() if called via `python3 a7p1.py`
# but not if `python3 -i a7p1.py` or `from a7p1 import *`
if __name__ == "__main__" and not flags.interactive:
    test()
