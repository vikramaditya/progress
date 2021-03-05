# https://www.codechef.com/PEC2021D/problems/SRTCHK

t = int(input())

for g in range(0,t):
    n = int(input())

    A = [int(c) for c in input().split()]

    B = [int(c) for c in input().split()]

    A.sort()

    if A == B:
        print("yes")
    else:
        print("no")
