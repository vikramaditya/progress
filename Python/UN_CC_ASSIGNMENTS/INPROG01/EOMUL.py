# https://www.codechef.com/INPRG01/problems/EOMUL

j = int(input())

if (j % 3 != 0):
    print(-1)

if (j % 3 == 0) and (j % 2 != 0):
    print(1)

if (j % 3 == 0) and (j % 2 == 0):
    print(0)

# (c) 2021, Vikramaditya V. Vajire
# https://github.com/vikramaditya
# This source code is licensed under the MIT License
