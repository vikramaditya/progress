'''
Educational Codeforces Round 108 (Rated for Div. 2)
[https://codeforces.com/contest/1519/problem/B]

B. The Cake Is a Lie

Author: valisport
Date: Thu Apr 29 21:57:04 IST 2021

[https://github.com/vikramaditya/progress]
'''

t = int(input())

for q in range(t):
    n, m , k = [int(c) for c in input().split()]
    ct = 0
    while True:
        if n == 1 and m == 1:
            break
        if m > 1:
            m -= 1
            ct += n
        if n == 1 and m == 1:
            break
        if n > 1:
            n -= 1
            ct += m
    res = "NO"
    if ct == k:
        res = "YES"
    print(res)
