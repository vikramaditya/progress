# https://www.codechef.com/LTIME94C/problems/NFS
"""
Turn It
"""

T = int(input())

for f in range(T):
    U, V, A, S = [int(c) for c in input().split()]

    if (U * U - 2 * A * S) < 0:
        G = 0
    else:
        G = (U * U - 2 * A * S) ** 0.5

    if U == V:
        print("YES")
    elif G <= V:
        print("YES")
    else:
        print("NO")
