# https://www.codechef.com/PEC2021/problems/REVMEE

x = int(input())
inp = list(input().split())
inp.reverse()
i = 0
while x > 0:

    while i < len(inp):
        print(inp[i], end=" ")
        i += 1
    x -= 1

# (c) 2021, Vikramaditya V. Vajire
# https://github.com/vikramaditya
# This source code is licensed under the MIT License
