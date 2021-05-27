"""
PROBLEM URL: https://codeforces.com/problemset/problem/41/A
PROBLEM NAME: Translation

AUTHOR: valisport
DATE: Thursday 27 May 2021 11:25:39 PM IST
LANGUAGE: Python 3

REPOSITORY ADDRESS: https://github.com/vikramaditya/progress
"""

s = input()
t = input()

go = "".join(reversed(s))

if go == t:
    print("YES")
else:
    print("NO")
