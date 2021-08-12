"""
Author: valisport
Date: Friday 06 August 2021 09:18:08 PM IST
"""

T = int(input())

for f in range(T):
    go = [int(c) for c in input().split()]
    res = 0

    if len(set(go)) == 1:
        res = 0
    elif len(set(go)) == 2:
        A1 = go[0]
        A2 = go[1]
        A3 = go[2]
        A4 = go[3]

        if A1 == A2 and A3 == A4:
            res = 2
        elif A1 == A4 and A2 == A3:
            res = 2
        elif A1 == A3 and A2 == A4:
            res = 2
        else:
            res = 1

    elif len(set(go)) == 3:
        res = 2
    elif len(set(go)) == 4:
        res = 2

    print(res)
