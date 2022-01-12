"""
Author: valisport
Date: Friday 04 June 2021 10:03:26 PM IST
"""
t = int(input())

for f in range(t):
    xa, xb, Xa, Xb = [int(c) for c in input().split()]

    a = Xa // xa
    b = Xb // xb

    res = a + b

    print(res)
