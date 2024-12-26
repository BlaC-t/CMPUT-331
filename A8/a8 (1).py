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
import re

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

    return letterCount


def getSubsequences(ciphertext, keylen):
    # This function takes in a ciphertext as a string and a key length as a int for its parameters
    # This function will return list of lists containing the characters in each subsequence
    subsequences = []

    return subsequences

def calculateTopIMC(subsequence):
    # Given a string, this function will calculate and return a list containing all 26 keys and their IMC values
    # Return a list of tuples containing key, IMC pairs from largest IMC to smallest
    pass

def decryptVigenere(ciphertext, key):
    # This function takes in a vigenere ciphertext and it's key as the parameters
    # The decrypted message will be returned
    
    LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    decryption = ''
    return decryption

def vigenereKeySolver(ciphertext: str, keylength: int):
    """
    return a list of the ten most likely keys
    """
    # Remove non characters in ciphertext
    ciphertext = re.compile('[^A-Z]').sub('',ciphertext.upper())


    raise NotImplementedError()

def hackVigenere(ciphertext: str):
    """
    return a string containing the key to the cipher
    """
    raise NotImplementedError()

def crackPassword():
    """
    hack password_protected.txt and write it to a new file
    """
    raise NotImplementedError()

def test():
    
    # vigenereKeySolver Tests
    ciphertext = "QPWKALVRXCQZIKGRBPFAEOMFLJMSDZVDHXCXJYEBIMTRQWNMEAIZRVKCVKVLXNEICFZPZCZZHKMLVZVZIZRRQWDKECHOSNYXXLSPMYKVQXJTDCIOMEEXDQVSRXLRLKZHOV"
    best_keys = vigenereKeySolver(ciphertext, 5)
    assert best_keys[0] == "EVERY"

    ciphertext = "VYCFNWEBZGHKPWMMCIOGQDOSTKFTEOBPBDZGUFUWXBJVDXGONCWRTAGYMBXVGUCRBRGURWTHGEMJZVYRQTGCWXF"
    best_keys = vigenereKeySolver(ciphertext, 6)
    assert best_keys[0] == "CRYPTO"
    
    # hackVigenere Tests
    ciphertext = "ANNMTVOAZPQYYPGYEZQPFEXMUFITOCZISINELOSGMMOAETIKDQGSYXTUTKIYUSKWYXATLCBLGGHGLLWZPEYXKFELIEUNMKJMLRMPSEYIPPOHAVMCRMUQVKTAZKKXVSOOVIEHKKNUMHMFYOAVVMITACZDIZQESKLHARKAVEUTBKXSNMHUNGTNKRKIETEJBJQGGZFQNUNFDEGUU"
    key = hackVigenere(ciphertext)
    assert key == "MAGIC"

    ciphertext = "AQNRXXXSTNSKCEPUQRUETZWGLAQIOBFKUFMGWIFKSYARFJSFWSPVXHLEMVQXLSYFVDVMPFWTMVUSIVSQGVBMAREKEOWVACSGYXKDITYSKTEGLINCMMKLKDFRLLGNERZIUGITCWJVGHMPFEXLDIGGFXUEWJIHXXJVRHAWGFYMKMFVLBKAKEHHO"
    key = hackVigenere(ciphertext)
    assert key == "SECRET"

    ciphertext = "JDMJBQQHSEZNYAGVHDUJKCBQXPIOMUYPLEHQFWGVLRXWXZTKHWRUHKBUXPIGDCKFHBZKFZYWEQAVKCQXPVMMIKPMXRXEWFGCJDIIXQJKJKAGIPIOMRXWXZTKJUTZGEYOKFBLWPSSXLEJWVGQUOSUHLEPFFMFUNVVTBYJKZMUXARNBJBUSLZCJXETDFEIIJTGTPLVFMJDIIPFUJWTAMEHWKTPJOEXTGDSMCEUUOXZEJXWZVXLEQKYMGCAXFPYJYLKACIPEILKOLIKWMWXSLZFJWRVPRUHIMBQYKRUNPYJKTAPYOXDTQ"
    key = hackVigenere(ciphertext)
    assert key == "QWERTY"

if __name__ == '__main__' and not flags.interactive:
    test()