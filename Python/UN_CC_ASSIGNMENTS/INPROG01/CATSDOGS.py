# https://www.codechef.com/INPRG01/problems/CATSDOGS

T = int(input())

while T > 0:
    C, D, L = [int(C) for C in input().split()]

    if C > 2 * D:
        ml = (C - 2 * D) * 4 + D * 4
    else:
        ml = D * 4

    mx = (C + D) * 4

    if L >= ml and L <= mx and L % 4 == 0:
        r = "yes"
    else:
        r = "no"

    T = T - 1
    print(r)

# (c) 2021, Vikramaditya V. Vajire
# https://github.com/vikramaditya
# This source code is licensed under the MIT License
