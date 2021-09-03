"""
Author: valisport
Date: Friday 03 September 2021 03:25:09 PM IST
"""

T = int(input())

for f in range(T):
    N = int(input())
    case = [int(c) for c in input().split()]

    odd = even = 0

    for ele in case:
        if ele % 2 == 0:
            even += 1
        else:
            odd += 1
    res = min(N // 2, odd) + min(N - N // 2, even)

    print(res)

