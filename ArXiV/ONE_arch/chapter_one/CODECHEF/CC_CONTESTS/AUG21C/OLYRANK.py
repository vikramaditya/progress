"""
Author: valisport
Date: Friday 06 August 2021 08:52:27 PM IST
"""

T = int(input())

for f in range(T):
    go = [int(c) for c in input().split()]
    first = second = 0
    for i in range(0,3):
        first += go[i]
    for i in range(3,6):
        second += go[i]

    if first > second:
        print(1)
    else:
        print(2)
