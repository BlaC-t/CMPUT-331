#!/usr/bin/python3

#---------------------------------------------------------------
#
# CMPUT 331 Student Submission License
# Version 1.0
# Copyright 2023  Zhiyu Li (Titus)
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
CMPUT 331 Assignment 3 Student Solution
September 2023
Author:  Zhiyu Li (Titus)
"""

# R(i+2) =(aR(i+1)+bR(i)+c) (mod m) i≥0
# Equation 1: R4 = (aR3 + bR2 + c) (mod m)
# Equation 2: R5 = (aR4 + bR3 + c) (mod m)
# Equation 3: R6 = (aR5 + bR4 + c) (mod m)

def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b

# Cracking Code with Python p192
def modInverse(A, M):
    u1, u2, u3 = 1, 0, A
    v1, v2, v3 = 0, 1, M
    while (v3 != 0):
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % M


def crack_rng(m, sequence):
    r2, r3, r4, r5, r6 = tuple(sequence)
    
    # Erase c 
    # Equation 1 - 2
    eq_12_a = r3 - r4
    eq_12_b = r2 - r3
    eq_12_rem = r4 - r5
    if(eq_12_rem < 0):
        eq_12_rem = m + eq_12_rem

    # Equation 1 - 3
    eq_13_a = r3 - r5
    eq_13_b = r2 - r4
    eq_13_rem = r4 - r6
    if(eq_13_rem < 0):
        eq_13_rem = m + eq_13_rem

    # Erase b
    eq_a = eq_12_a * eq_13_b - eq_13_a*eq_12_b
    eq_rem = eq_12_rem * eq_13_b - eq_13_rem * eq_12_b

    # Check co-prime
    if(gcd(abs(eq_a), m) != 1):
        return
    
    # Find invMod
    if(modInverse(eq_a, m) == -1):
        return

    # Find a use invMod
    invMod = modInverse(eq_a, m)
    a = (invMod * eq_rem) % m

    # Plug it back to equation 12 to find b
    eq_b_rem = eq_12_rem - a * eq_12_a 
    if(eq_b_rem < 0):
        eq_b_rem = m - abs(eq_b_rem) % m

    if(gcd(abs(eq_12_b), m) != 1):
        return

    if(modInverse(eq_12_b, m) == -1):
        return
    
    invMod_b = modInverse(eq_12_b, m)
    b = (invMod_b * eq_b_rem) % m

    # Plug a and b back to equation find c
    c = m - abs(r4 - a*r3 - b*r2) % m

    return [a, b, c]


def test():
    assert crack_rng(17, [14, 13, 16, 3, 13]) == [3, 5, 9]
    assert crack_rng(9672485827, [4674207334, 3722211255, 3589660660, 1628254817, 8758883504]) == [22695477, 77557187, 259336153]
    assert crack_rng(101, [0, 91, 84, 16, 7]) == [29, 37, 71]
    assert crack_rng(222334565193649,[438447297,50289200612813,17962583104439,47361932650166,159841610077391]) == [1128889, 1023, 511]
from sys import flags

if __name__ == "__main__" and not flags.interactive:
    test()
