'''
April Lunchtime 2021 Division 3
[https://www.codechef.com/LTIME95C]

Problem Code: CCHEAVEN > Chef in Heaven

Author: valisport
Date: Sat May  1 03:19:13 IST 2021

[https://github.com/vikramaditya/progress]
'''

t = int(input())

for f in range(t):
    L = int(input())
    S = input()

    res = "NO"

    good = 0
    bad = 0

    for ele in S:
        if ele == '1':
            good += 1
        else:
            bad += 1

        if good >= bad:
            res = "YES"
            break
    print(res)
