"""
PROBLEM URL: https://codeforces.com/problemset/problem/110/A
PROBLEM NAME: Nearly Lucky Number

AUTHOR: valisport
DATE: Thursday 27 May 2021 11:08:57 PM IST
LANGUAGE: Python 3

REPOSITORY ADDRESS: https://github.com/vikramaditya/progress
"""

n = input()
ct = 0

for ele in n:
    if ele == "7" or  ele == "4":
        ct += 1

ct = str(ct)

res = 'YES'

for ele in ct:
    if ele != "7" and ele != "4":
        res = 'NO'

print(res)
