# https://codeforces.com/problemset/problem/231/A

clara = int(input())
co = 0
while clara > 0:
    N, V, J = [int(N) for N in input().split()]

    if (N and V) or (N and J) or (V and J):
        co += 1

    clara = clara - 1

print(co)

# (c) 2021, Vikramaditya V. Vajire
# https://github.com/vikramaditya
# This source code is licensed under the MIT License
