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
Assignment 9 Problem 1
"""

from sys import flags
from typing import Tuple
import time

# Cracking Code with Python p192
def modInverse(A, M):
    u1, u2, u3 = 1, 0, A
    v1, v2, v3 = 0, 1, M
    while (v3 != 0):
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % M

def finitePrimeHack(t: int, n: int, e: int) -> Tuple[int, int, int]:
    """
    Hack RSA assuming there are no primes larger than t
    """
    # find all prime
    primeList = []
    for i in range(1, t):
        if n % i == 0:
            primeList.append(i)

    # to find the two prime that their product equals to n
    p = 0
    q = 0
    for possP in primeList:
        possQ = n / possP
        if possQ in primeList:
            p = int(possP)
            q = int(possQ)

    # order p and q   
    if p > q:
        temp = p
        p = q
        q = temp

    # find mod and inverse of mod
    mod = (p-1) * (q-1)
    d = modInverse(e, mod)

    return (p, q, d)


def test():
    "Run tests"
    assert finitePrimeHack(100, 493, 5) == (17, 29, 269)
    # TODO: test thoroughly by writing your own regression tests
    # This function is ignored in our marking

    msg = ""
    files = ["1_pubkey.txt", "2_pubkey.txt", "3_pubkey.txt", "4_pubkey.txt", "5_pubkey.txt"]
    for file in files:
        numList = open(file, 'r').read().split(',')
        tup = finitePrimeHack(2**int(numList[0]), int(numList[1]), int(numList[2]))
        
        msg += str(tup)
        msg += "\n"

    open('a9.txt', 'w').write(msg)

# Invoke test() if called via `python3 a9p1.py`
# but not if `python3 -i a9p1.py` or `from a9p1 import *`
if __name__ == '__main__' and not flags.interactive:
    test()
