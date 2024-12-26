from string import ascii_uppercase
import itertools

def ngramsFreqsFromFile(textFile: "file", n: int) -> dict:
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


