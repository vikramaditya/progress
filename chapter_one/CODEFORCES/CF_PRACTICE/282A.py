# https://codeforces.com/problemset/problem/282/A

cl = int(input())
ct = 0
while cl > 0:
    gh = input()
    if gh == "X++" or gh == "++X":
        ct +=1
    if gh == "--X" or gh == "X--":
        ct -= 1
    cl -= 1
print(ct)

# (c) 2021, Vikramaditya V. Vajire
# https://github.com/vikramaditya
# This source code is licensed under the MIT License
