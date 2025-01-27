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
Assignment 7 Problems 2, 3, and 4
"""

import re
from sys import flags


def stringIC(text: str):
    """
    Compute the index of coincidence (IC) for text
    """

    # create dict with letter being the key and the number of its apperance being value
    count = {}
    for i in text:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    # calculate according to the equation
    num = 0
    den = len(text) * (len(text) - 1)
    for each in count:
        num += count[each] * (count[each] - 1)

    return num / den


def subseqIC(ciphertext: str, keylen: int):
    """
    Return the average IC of ciphertext for
    subsequences induced by a given a key length
    """
    # for each sub string with length of n, get its IC value to find the avg at the end
    IC = []
    for i in range(1, keylen + 1):
        nthStr = getNthSubkeysLetters(i, keylen, ciphertext)
        strIC = stringIC(nthStr)
        IC.append(strIC)

    return sum(IC) / len(IC)


def keyLengthIC(ciphertext: str, n: int):
    """
    Return the top n keylengths ordered by likelihood of correctness
    Assumes keylength <= 20
    """
    # Use the funtion above to find all possible avg IC for n lower than 20
    keyDict = {}
    for i in range(1, 21):
        avgIC = subseqIC(ciphertext, i)
        keyDict[i] = avgIC

    # find the top nth avg IC
    outList = []
    for i in range(n):
        maxIC = [0, 0]

        # compare inside the dict, tie breaker been lower key (length) wins
        for j in keyDict:
            if keyDict[j] > maxIC[1]:
                maxIC[0], maxIC[1] = j, keyDict[j]
            elif keyDict[j] == maxIC[1]:
                if j < maxIC[0]:
                    maxIC[0], maxIC[1] = j, keyDict[j]

        # add to output list, change the value of that key to -1 for avoid further comparison
        outList.append(maxIC[0])
        keyDict[maxIC[0]] = -1

    return outList


def getNthSubkeysLetters(nth: int, keyLength: int, message: str):
    # Returns every nth letter for each keyLength set of letters in text.
    # E.g. getNthSubkeysLetters(1, 3, 'ABCABCABC') returns 'AAA'
    #      getNthSubkeysLetters(2, 3, 'ABCABCABC') returns 'BBB'
    #      getNthSubkeysLetters(3, 3, 'ABCABCABC') returns 'CCC'
    #      getNthSubkeysLetters(1, 5, 'ABCDEFGHI') returns 'AF'

    # Use a regular expression to remove non-letters from the message:
    message = re.compile("[^A-Z]").sub("", message)

    i = nth - 1
    letters = []
    while i < len(message):
        letters.append(message[i])
        i += keyLength
    return "".join(letters)


def test():
    "Run tests"
    print(
        keyLengthIC(
            "PPQCAXQVEKGYBNKMAZUYBNGBALJONITSZMJYIMVRAGVOHTVRAUCTKSGDDWUOXITLAZUVAVVRAZCVKBQPIWPOU",
            5,
        )
    )
    # assert stringIC("ABA") == 1 / 3
    # TODO: test thoroughly by writing your own regression tests
    # This function is ignored in our marking


# Invoke test() if called via `python3 a7p234.py`
# but not if `python3 -i a7p234.py` or `from a7p234 import *`
if __name__ == "__main__" and not flags.interactive:
    test()
