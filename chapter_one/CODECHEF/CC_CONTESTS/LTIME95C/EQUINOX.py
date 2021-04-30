'''
April Lunchtime 2021 Division 3
[https://www.codechef.com/LTIME95C]

Problem Code: EQUINOX > Equinox Strings

Author: valisport
Date: Sat May  1 03:14:33 IST 2021

[https://github.com/vikramaditya/progress]
'''

t = int(input())

for f in range(t):
    N, A, B = [int(c) for c in input().split()]
    totals = []
    for g in range(N):
        string = input()
        totals.append(string)
        for ele in string:
            if ele.islower():
                exit()
    dict = 'EQUINOX'

    SART = 0
    ANUR = 0

    for ele in totals:
        if ele[0] in dict:
            SART += A
        else:
            ANUR += B
    res = ''
    if SART == ANUR:
        res = "DRAW"

    if ANUR > SART:
        res = 'ANURADHA'
    if SART > ANUR:
        res = 'SARTHAK'

    print(res)
