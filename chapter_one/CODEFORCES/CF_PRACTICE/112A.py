# https://codeforces.com/problemset/problem/112/A

clara = input()
clara = clara.lower()
jane = input()
jane = jane.lower()

if (clara < jane):
    print(-1)
elif (jane < clara):
    print(1)
elif (jane == clara):
    print(0)

# (c) 2021, Vikramaditya V. Vajire
# https://github.com/vikramaditya
# This source code is licensed under the MIT License
