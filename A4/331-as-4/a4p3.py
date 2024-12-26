#!/usr/bin/env python3

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
Enhanced substitution cipher solver.
"""

import re, simpleSubCipher, simpleSubHacker, itertools

LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def hackSimpleSub(message: str):
    """
    Simple substitution cipher hacker.
    First runs the textbook program to get an initial, potentially incomplete decipherment.
    Then uses regular expressions and a dictionary to decipher additional letters.
    """

    # Possible word list
    f = open('dictionary.txt','r')
    wordDictList = f.read().split('\n')
    f.close()

    # First pass
    letterMapping = simpleSubHacker.hackSimpleSub(message)
    hackedMessage = simpleSubHacker.decryptWithCipherletterMapping(message, letterMapping)
    
    # creat a dict with all letters and its corresponding encrypted letter
    # https://www.geeksforgeeks.org/python-initializing-dictionary-with-empty-lists/
    missingMapping = dict(zip(list(LETTERS), list(itertools.repeat([], len(list(LETTERS))))))
    
    # Find all mapped letters
    for i in range(0, len(message)):
        if hackedMessage[i] != '_' and (hackedMessage[i].upper() in LETTERS):
            missingMapping[message[i].upper()] = hackedMessage[i].upper()

    # split up both original msg and the msg after first pass
    wordHackedMsg = re.split(r"[-,.\s]\s*", hackedMessage)
    oriMsg = re.split(r"[-,.\s]\s*", message)


    # Get all possible word for its corresponding encrypted word
    # https://builtin.com/software-engineering-perspectives/python-remove-character-from-string
    deMsgWord = []
    oriDeMsgWordLoc = []
    for i in range(len(wordHackedMsg)): 
        if '_' in wordHackedMsg[i]:
            temp = re.sub('_', '[a-zA-Z]', wordHackedMsg[i].upper())

            possibleList = []
            for eachWord in range(len(wordDictList)):
                if re.match(temp, str(wordDictList[eachWord])):
                    possibleList.append(wordDictList[eachWord])

            deMsgWord.append(possibleList)
            oriDeMsgWordLoc.append(i)


    # find the greatest length of possible word in the nested list
    for i in deMsgWord:
        if len(i) > -1:
            largestLen = len(i)


    for length in range(1, largestLen+1):
        for eachDeMsgWord in range(len(deMsgWord)):

            # find the corresponding word 
            if len(deMsgWord[eachDeMsgWord]) == length:
                oriWord = oriMsg[oriDeMsgWordLoc[eachDeMsgWord]]
                missWord = wordHackedMsg[oriDeMsgWordLoc[eachDeMsgWord]]  
                
                # Try the mapping, see if its already assigned to one of the letter, if not assign it
                for pos in range(len(missWord)):
                    if missWord[pos] == '_':
                        for eachPoss in deMsgWord[eachDeMsgWord]:
                            if (missingMapping[oriWord[pos].upper()] == []):
                                missingMapping[oriWord[pos].upper()] = eachPoss[pos].upper()
                                continue

    # Run the message again with the new letter mapping                                
    deMsg = ''
    for i in range(len(hackedMessage)):
        if hackedMessage[i] == '_':
            if message[i].isupper():
                deMsg += missingMapping[message[i].upper()]
            else:
                deMsg += missingMapping[message[i].upper()].lower()
        else:
            deMsg += hackedMessage[i]
    
    return deMsg

def test():
    # Provided test.
    message = 'Sy l nlx sr pyyacao l ylwj eiswi upar lulsxrj isr sxrjsxwjr, ia esmm rwctjsxsza sj wmpramh, lxo txmarr jia aqsoaxwa sr pqaceiamnsxu, ia esmm caytra jp famsaqa sj. Sy, px jia pjiac ilxo, ia sr pyyacao rpnajisxu eiswi lyypcor l calrpx ypc lwjsxu sx lwwpcolxwa jp isr sxrjsxwjr, ia esmm lwwabj sj aqax px jia rmsuijarj aqsoaxwa. Jia pcsusx py nhjir sr agbmlsxao sx jisr elh. -Facjclxo Ctrramm'
    print(hackSimpleSub(message))
    # End of provided test.

if __name__ == '__main__':
    test()
