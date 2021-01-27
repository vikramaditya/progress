# https://www.codechef.com/PEC2021/problems/FINDMELI

n, k = [n for n in input().split()]
inp = list(input().split())

i = 0
result = -1
j = 1
while j <= len(inp) - 1:

    if inp[i] == k:
        result = 1
    i = i + 1
    j = j + 1

print(result)

# (c) 2021, Vikramaditya V. Vajire
# https://github.com/vikramaditya
# This source code is licensed under the MIT License
