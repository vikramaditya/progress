"""
/**
 * Author   : veep
 * Date     : Tuesday 10 May 2022 08:14:33 PM IST
 */
"""

t = int(input())

for i in range(t):
    a = int(input())
    arr = [int(c) for c in input().split()]

    minx = min(arr)
    res = 0

    for ele in arr:
        if ele > minx:
            res += (ele - minx)

    print(res)

