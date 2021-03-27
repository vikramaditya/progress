# https://www.codechef.com/LTIME94C/problems/MKSMEVN
"""
Make the Sum Even
"""

T = int(input())

for f in range(T):
    N = int(input())
    S = [int(c) for c in input().split()]

    if sum(S) % 2 == 0:
        print(0)
    elif 2 in S:
        print(1)
    else:
        print(-1)
