# https://codeforces.com/problemset/problem/1475/A

clara = int(input())

for lana in range(clara):
    jane = int(input())

    while not (jane % 2):
        jane //= 2

    if jane > 1:
        print("YES")
    else:
        print("NO")

# (c) 2021, Vikramaditya V. Vajire
# https://github.com/vikramaditya
# This source code is licensed under the MIT License
