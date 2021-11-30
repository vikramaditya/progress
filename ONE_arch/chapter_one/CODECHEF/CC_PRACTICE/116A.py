"""
Author: valisport
Date: Tuesday 16 November 2021 11:30:08 PM IST
"""

t = int(input())

pas = []
tmp = 0
for i in range(t):
    a,b = [int(c) for c in input().split()]
    tmp += b
    tmp -= a
    pas.append(tmp)

print(max(pas))
