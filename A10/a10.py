#!/usr/bin/env python3

# ---------------------------------------------------------------
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
# ---------------------------------------------------------------

"""
Assignment 10
"""

from sys import flags

def freqFileDict(fileContent: str):
    # given content, return frequency dictionary on percentage in text for each letter
    fileContent = fileContent.replace(' ', '').replace('\n', '').upper()
    freqDict = {}
    for eachChar in fileContent:
        if eachChar in freqDict:
            freqDict[eachChar] += 1
        else:
            freqDict[eachChar] = 1

    for eachKey in freqDict:
        freqDict[eachKey] = freqDict[eachKey] / len(fileContent)
    
    return freqDict


def cliSSD(ciphertext: str, files):
    """
    Args:
        ciphertext (str)
        files (list of str)
    Returns:
        dict
    """
    # find the language dict and the cipher text freq dict
    fileDict = {}
    for eachfile in files:
        fileContent = open(eachfile, encoding="utf8").read()
        freqDict = freqFileDict(fileContent)
        fileDict[eachfile] = sorted(freqDict.items(), key = lambda x:x[1], reverse=True)

    enDict = freqFileDict(ciphertext)
    enDict = sorted(enDict.items(), key = lambda  x:x[1], reverse=True)

    # given the ciphertext, check everysingle sample language file and calculate the difference
    ssdDict = {}
    for eachDict in fileDict:
        distance = 0
        
        # The comprison is used to prevent out of boundary situation
        if len(enDict) > len(fileDict[eachDict]):
            for i in range(len(enDict)):
                if i < len(fileDict[eachDict]):
                    distance += (enDict[i][1] - fileDict[eachDict][i][1]) ** 2
                else:
                    distance += (enDict[i][1]) ** 2
        else:
            for i in range(len(enDict)):
                if i < len(enDict):
                    distance += (enDict[i][1] - fileDict[eachDict][i][1]) ** 2
                else:
                    distance += (enDict[i][1]) ** 2
        ssdDict[eachDict] = distance
    
    return ssdDict

# given content, first output a dict with pattern and the number of time it appears
# then calculate percentage of pattern from for all word patterns
def freqWordDict(fileContent):
    fileContent = fileContent.replace('\n', ' ').upper().split()

    freqDict = {}
    for eachWord in fileContent:
        # find frequency of each letter in a word
        letterDict = {}
        for eachLetter in eachWord:
            if eachLetter in letterDict:
                letterDict[eachLetter] += 1
            else:
                letterDict[eachLetter] = 1
        
        wordPattern = tuple(sorted(list(letterDict.values()), reverse=True))

        if wordPattern in freqDict:
            freqDict[wordPattern] += 1
        else:
            freqDict[wordPattern] = 1
    
    # find fequency of each pattern 
    for eachPattern in freqDict:
        freqDict[eachPattern] = freqDict[eachPattern] / len(fileContent)
    
    return freqDict

def cliDPD(ciphertext: str, files):
    """
    Args:
        ciphertext (str)
        files (list of str)
    Returns:
        dict
    """
    # for each file, it will conduct a unqiue dict of dict
    fileDict = {}
    for eachfile in files:
        fileContent = open(eachfile, encoding="utf8").read()
        freqDict = freqWordDict(fileContent)
        fileDict[eachfile] = freqDict
    
    enDict = freqWordDict(ciphertext)

    # for each file dict find the distance between both dict
    dpdDict = {}
    for eachDict in fileDict:
        distance = 0 
        for eachPattern in enDict:
            if eachPattern in fileDict[eachDict]:
                distance += (enDict[eachPattern] - fileDict[eachDict][eachPattern]) ** 2
                fileDict[eachDict].pop(eachPattern)
            else:
                distance += (enDict[eachPattern]) ** 2

        # for any pattern in the file dict that is not included in the sample
        # also added into distance
        for patternLeft in fileDict[eachDict]:
            distance += (fileDict[eachDict][patternLeft]) ** 2
        
        dpdDict[eachDict] = distance
    
    return dpdDict

def cliSSDTest(ciphertext_files, sampletext_files):
    """
    Args:
        ciphertext_files (list of str)
        sampletext_files (list of str)
    Returns:
        dict
    """
    testDict = {}

    for eachEnMsg in ciphertext_files:
        enText = open(eachEnMsg, encoding="utf8").read()
        ssdDict = cliSSD(enText, sampletext_files)
        testDict[eachEnMsg] = sorted(ssdDict.items(), key = lambda x:x[1])[0][0]
    
    return testDict


def cliDPDTest(ciphertext_files, sampletext_files):
    """
    Args:
        ciphertext_files (list of str)
        sampletext_files (list of str)
    Returns:
        dict
    """
    testDict = {}

    for eachEnMsg in ciphertext_files:
        enText = open(eachEnMsg, encoding="utf8").read()
        dpdDict = cliDPD(enText, sampletext_files)
        testDict[eachEnMsg] = sorted(dpdDict.items(), key = lambda x:x[1])[0][0]
    
    return testDict


def test():

    # give sample file and the encoded file to the program
    sampleFile = ['sample_en.txt', 'sample_fr.txt', 'sample_it.txt', 'sample_bg.txt','sample_de.txt','sample_el.txt','sample_es.txt','sample_nl.txt','sample_pl.txt','sample_ru.txt']
    enFiles = open('text.txt', 'r').read().split()

    # ssd test and print out sample file and its corresponding detection
    ssd = cliSSDTest(enFiles, sampleFile)
    dic = {}
    for eachFile in enFiles:
        sampleLanguage = eachFile[11:13]
        detectedLanguage = ssd[eachFile][7:9]

        ts = sampleLanguage + '-' + detectedLanguage
        if ts in dic:
            dic[ts] += 1
        else:
            dic[ts] = 1      
    print(dic)

    # dpd test and print out sample file and its corresponding detection
    dpd = cliDPDTest(enFiles, sampleFile)
    dic2 = {}
    for eachFile in enFiles:
        sampleLanguage = eachFile[11:13]
        detectedLanguage = dpd[eachFile][7:9]

        ts = sampleLanguage + '-' + detectedLanguage
        if ts in dic2:
            dic2[ts] += 1
        else:
            dic2[ts] = 1
    print(dic2)


if __name__ == "__main__" and not flags.interactive:
    test()
