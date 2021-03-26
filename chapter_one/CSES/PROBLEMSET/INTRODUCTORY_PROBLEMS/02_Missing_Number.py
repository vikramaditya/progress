# https://cses.fi/problemset/task/1083/
"""
Introductory Problems : Missing Number
"""

n = int(input())
given = [int(c) for c in input().split()]
given.sort()
all = [int(c) for c in range(1,n+1)]
res = -1
for i in range(len(given)):
    if given[i] != all[i]:
        res = all[i]
        break

if res != -1:
    print(res)
else:
    print(n)
