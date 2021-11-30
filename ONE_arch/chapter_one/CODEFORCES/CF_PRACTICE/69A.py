"""
https://codeforces.com/problemset/problem/69/A

Problem : Young Physicist
Author: valisport
Date: Thursday 03 June 2021 01:23:50 AM IST

[https://github.com/vikramaditya/progress]
"""

n = int(input())
X = []
Y = []
Z = []
for f in range(n):
    x, y, z = [int(c) for c in input().split()]
    X.append(x)
    Y.append(y)
    Z.append(z)

one = 0

for ele in X:
    one += ele

two = 0

for ele in Y:
    two += ele

three = 0

for ele in Z:
    three += ele

res = "NO"

if one == 0 and two == 0 and three == 0:
    res = "YES"

print(res)
