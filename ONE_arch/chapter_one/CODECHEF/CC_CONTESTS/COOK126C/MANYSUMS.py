# https://www.codechef.com/COOK126C/problems/MANYSUMS

clara = int(input())

while clara > 0:
    a,b = [int(C) for C in input().split()]

    print(2 * (b-a) + 1)

    clara -= 1

# (c) 2021, Vikramaditya V. Vajire
# https://github.com/vikramaditya
# This source code is licensed under the MIT License
