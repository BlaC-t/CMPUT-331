#!/usr/bin/env python3

# ---------------------------------------------------------------
#
# CMPUT 331 Student Submission License
# Version 1.1
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
Assignment 8 Problems 1, 2 and 3
"""
from sys import flags
import itertools
import re
import a6
import a7
import time


LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# English letter frequencies for calculating IMC (by precentage)
ENG_LETT_FREQ = {'E': 12.70, 'T': 9.06, 'A': 8.17, 'O': 7.51, 'I': 6.97, 'N': 6.75, 'S': 6.33, 'H': 6.09, 
                 'R': 5.99,  'D': 4.25, 'L': 4.03, 'C': 2.78, 'U': 2.76, 'M': 2.41, 'W': 2.36, 'F': 2.23, 
                 'G': 2.02,  'Y': 1.97, 'P': 1.93, 'B': 1.29, 'V': 0.98, 'K': 0.77, 'J': 0.15, 'X': 0.15, 
                 'Q': 0.10,  'Z': 0.07}

def getLetterFrequency(message):
    # Returns a dictionary of letter frequencies in the message
    # Divide each letter count by total number of letters in the message to get it's frequency
    letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0, 'G': 0, 'H': 0, 
                   'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0, 'O': 0, 'P': 0, 
                   'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0, 'W': 0, 'X': 0, 
                   'Y': 0, 'Z': 0}

    for eachLetter in message:
        letterCount[eachLetter] += 1

    for i in letterCount:
        letterCount[i] = (letterCount[i] / len(message)) * 100
    
    letterCount = dict(sorted(letterCount.items(), key=lambda x:x[1], reverse=True))

    return letterCount


def getSubsequences(ciphertext, keylen):
    # This function takes in a ciphertext as a string and a key length as a int for its parameters
    # This function will return list of lists containing the characters in each subsequence
    subsequences = []

    kSubSequence = int(len(ciphertext) / keylen + 1)

    # for every single position of a key, find its corresponding ciphered letter
    for i in range(keylen):
        each = []
        for j in range(kSubSequence):
            loc = keylen * j + i
            if loc < len(ciphertext):
                each.append(ciphertext[loc])
        subsequences.append(each)

    return subsequences


def calculateTopIMC(subsequence):
    # Given a string, this function will calculate and return a list containing all 26 keys and their IMC values
    # Return a list of tuples containing key, IMC pairs from largest IMC to smallest

    IMCList = []

    # https://www.simplilearn.com/tutorials/python-tutorial/list-to-string-in-python#:~:text=To%20convert%20a%20list%20to%20a%20string%2C%20use%20Python%20List,and%20return%20it%20as%20output.
    subString = ''.join(map(str,subsequence))
    
    # for each substring decipher it using every single letter
    for eachLetter in LETTERS:
        deMsg = decryptVigenere(subString, eachLetter)

        subFreq = getLetterFrequency(deMsg)

        # https://stackoverflow.com/questions/13902805/list-of-all-unique-characters-in-a-string
        unique = list(set(deMsg))
        
        # IMC calculation
        IMC = 0
        for each in unique:
            e = ENG_LETT_FREQ[each]
            t = subFreq[each]
            IMC += (e * t)
        
        tup = (eachLetter, IMC/100)
        IMCList.append(tup)

    # https://stackoverflow.com/questions/3121979/how-to-sort-a-list-tuple-of-lists-tuples-by-the-element-at-a-given-index
    sortedIMC = sorted(IMCList, key=lambda tup: tup[1], reverse=True)
    return sortedIMC


def decryptVigenere(ciphertext, key):
    # This function takes in a vigenere ciphertext and it's key as the parameters
    # The decrypted message will be returned

    decryption = ""

    # creating key stream
    if len(key) < len(ciphertext):
        for i in range(len(ciphertext) - len(key)):
            key += key[i % len(key)]

    for i in range(len(ciphertext)):
        x = (ord(ciphertext[i]) - ord(key[i]) + 26) % 26
        x += ord('A')
        decryption += chr(x)

    return decryption


def vigenereKeySolver(ciphertext: str, keylength: int):
    """
    return a list of the ten most likely keys
    """
    # Remove non characters in ciphertext
    ciphertext = re.compile("[^A-Z]").sub("", ciphertext.upper())

    subSequences = getSubsequences(ciphertext, keylength)

    # find the all the possible keys given the length using IMC and
    # extract the top 3 for each letter for further calculation
    possKeyList = []
    for eachSequence in subSequences:
        possKeyList.append(calculateTopIMC(eachSequence)[0:3])
    
    # for all possible combinaiton, calculate its sum IMC and find the comb with highest IMC
    combList = []
    allComb = list(itertools.product(*possKeyList))
    for eachComb in allComb:
        probKey = ""
        probKeyIMC = 0
        for eachLetter in eachComb:
            probKey += eachLetter[0]
            probKeyIMC += eachLetter[1]
        combList.append((probKey, probKeyIMC))

    sortedCombList = sorted(combList, key=lambda x:x[1], reverse=True)
    
    if len(sortedCombList) > 10:
        bound = 10
    else:
        bound = len(sortedCombList)

    # return top IMC comb 
    topList = []
    for i in range(bound):
        topList.append(sortedCombList[i][0])
    
    return topList

def keyScore(key:str, ciphertext: str, freq: dict, n: int):
    deMsg = decryptVigenere(ciphertext, key)

    # find all n gram in the string
    nGramList = []
    for i in range(len(deMsg)):
        sub = deMsg[i : i + n]
        if len(sub) == n:
            nGramList.append(sub)

    score = 0

    # recored all appeared substring to avoid repitition
    appearedList = []
    for i in nGramList:
        if i not in appearedList:
            c = nGramList.count(i)
            if i in freq:
                f = freq[i]
            else:
                f = 0

            score += c * f
            appearedList.append(i)
        else:
            continue

    return score

def hackVigenere(ciphertext: str):
    """
    return a string containing the key to the cipher
    """
    # nGram tried: 3, 2, 4, 5 
    nGram = 2
    ciphertext = re.compile("[^A-Z]").sub("", ciphertext.upper())

    # find all possible key length usign IC
    possKeyLen = a7.keyLengthIC(ciphertext, 20)
    
    freqDict = a6.ngramsFreqsFromFile("wells.txt", nGram)

    # only use key length less than or equal to 10
    totalKeyList = []
    for eachPossLen in possKeyLen:
        if eachPossLen > 10:
            continue
        
        # for each key len find out top possible key
        possKeyList = vigenereKeySolver(ciphertext, eachPossLen)
        totalKeyList.append(possKeyList)

    # for all possible length and all possible key, run it throught keyScore
    # find the one with highest key score
    possKeyList = []
    for each in totalKeyList:
        score = keyScore(each[0], ciphertext, freqDict, nGram)
        possKeyList.append((each[0], score))
    
    sortedKey = sorted(possKeyList, key=lambda tup: tup[1], reverse=True)

    return sortedKey[0][0]

def crackPassword():
    """
    hack password_protected.txt and write it to a new file
    """
    
    # open the cipher file and find the key 
    ciphertext = open("password_protected.txt", "r").read()
    key = hackVigenere(ciphertext)

    # letter maps with its location in alphbet
    letterMap = {}
    letterLoc = 0
    for i in LETTERS:
        letterMap[i] = letterLoc
        letterLoc += 1

    deMsg = ""

    # creating key stream to avoid out of index
    if len(key) < len(ciphertext):
        for i in range(len(ciphertext) - len(key)):
            key += key[i % len(key)]
    
    # for every single character check if it can be decipher or not
    # if the character is a letter, decipher it else append to the back
    keyLoc = 0
    for loc in range(len(ciphertext)):
        curChar = ciphertext[loc]
        if(curChar.isalpha()):
            deLoc = letterMap[curChar] - letterMap[key[keyLoc]]
            if deLoc < 0:
                deLoc += 26
            deMsg += LETTERS[deLoc]
            keyLoc += 1
        else:
            deMsg += curChar


    open("plaintext.txt", 'w').write(deMsg)
    


def test():
    # vigenereKeySolver Tests
    ciphertext = "QPWKALVRXCQZIKGRBPFAEOMFLJMSDZVDHXCXJYEBIMTRQWNMEAIZRVKCVKVLXNEICFZPZCZZHKMLVZVZIZRRQWDKECHOSNYXXLSPMYKVQXJTDCIOMEEXDQVSRXLRLKZHOV"
    best_keys = vigenereKeySolver(ciphertext, 5)
    assert best_keys[0] == "EVERY"


    ciphertext = "Vyc fnweb zghkp wmm ciogq dost kft 13 eobp bdzg uf uwxb jv dxgoncw rtag ymbx vg ucrbrgu rwth gemjzv yrq tgcwxf"
    best_keys = vigenereKeySolver(ciphertext, 6)
    assert best_keys[0] == "CRYPTO"
    
    # hackVigenere Tests
    ciphertext = "ANNMTVOAZPQYYPGYEZQPFEXMUFITOCZISINELOSGMMOAETIKDQGSYXTUTKIYUSKWYXATLCBLGGHGLLWZPEYXKFELIEUNMKJMLRMPSEYIPPOHAVMCRMUQVKTAZKKXVSOOVIEHKKNUMHMFYOAVVMITACZDIZQESKLHARKAVEUTBKXSNMHUNGTNKRKIETEJBJQGGZFQNUNFDEGUU"
    key = hackVigenere(ciphertext)
    assert key == "MAGIC"
    
    ciphertext = "A'q nrxx xst nskc epu qr uet zwg'l aqiobfk, uf M gwif ks yarf jsfwspv xh lemv qx ls yfvd. Vmpfwtmvu sivsqg vbmarek e owva csgy xkdi tys. K teg linc mm'k lkd fr llg ner zi ugitcw Jv ghmpfe'x ldigg fxuewji hx xjv rhawg fymkmfv lbk akehho."
    key = hackVigenere(ciphertext)
    assert key == "SECRET"

    ciphertext = "JDMJBQQHSEZNYAGVHDUJKCBQXPIOMUYPLEHQFWGVLRXWXZTKHWRUHKBUXPIGDCKFHBZKFZYWEQAVKCQXPVMMIKPMXRXEWFGCJDIIXQJKJKAGIPIOMRXWXZTKJUTZGEYOKFBLWPSSXLEJWVGQUOSUHLEPFFMFUNVVTBYJKZMUXARNBJBUSLZCJXETDFEIIJTGTPLVFMJDIIPFUJWTAMEHWKTPJOEXTGDSMCEUUOXZEJXWZVXLEQKYMGCAXFPYJYLKACIPEILKOLIKWMWXSLZFJWRVPRUHIMBQYKRUNPYJKTAPYOXDTQ"
    key = hackVigenere(ciphertext)
    assert key == "QWERTY"

    crackPassword()


if __name__ == "__main__" and not flags.interactive:
    test()
