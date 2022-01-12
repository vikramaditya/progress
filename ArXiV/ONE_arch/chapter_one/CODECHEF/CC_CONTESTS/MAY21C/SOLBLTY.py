"""
May Challenge 2021 Division 3
https://www.codechef.com/MAY21C/SOLBLTY

Problem Code: SOLBLTY > Solubility
Author: valisport
Date: Fri May  7 16:53:57 IST 2021

[https://github.com/vikramaditya/progress]
"""

T = int(input())
for f in range(T):
    X, A, B = [int(c) for c in input().split()]

    if A > 100:
        temp = 100
    else:
        temp = A

    res = (A + (temp - X) * B) * 10

    print(res)
