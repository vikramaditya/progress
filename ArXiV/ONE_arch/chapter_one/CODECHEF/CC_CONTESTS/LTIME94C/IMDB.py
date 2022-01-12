# https://www.codechef.com/LTIME94C/problems/IMDB
"""
Motivation
"""

T = int(input())

for f in range(T):
    N, X = [int(c) for c in input().split()]

    space = []
    rating = []

    for c in range(N):
        S, R = [int(c) for c in input().split()]

        if S <= X:
            space.append(S)
            rating.append(R)
        else:
            pass

    H = max(rating)
    print(H)
