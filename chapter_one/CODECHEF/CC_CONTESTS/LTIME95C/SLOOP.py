'''
April Lunchtime 2021 Division 3
[https://www.codechef.com/LTIME95C]

Problem Code: SLOOP > Coldplay

Author: valisport
Date: Sat May  1 03:15:28 IST 2021

[https://github.com/vikramaditya/progress]
'''
t = int(input())

for f in range(t):
    M, S = [int(c) for c in input().split()]

    print(M//S)
