"""
Author: valisport
Date: Tuesday 16 November 2021 11:29:24 PM IST
"""

go = [int(c) for c in input().split("+")]

go.sort()
res = ""
for i in range(len(go)):
    res += str(go[i])+"+"

print(res[:-1])
