"""
Author: valisport
Date: Friday 03 September 2021 03:16:31 PM IST
"""

T = int(input())

for f in range(T):
    N, A, B = [int(c) for c in input().split()]
    string = input()

    total_time = 0

    for ele in string:
        if ele == "0":
            total_time += A
        if ele == "1":
            total_time += B
    print(total_time)

