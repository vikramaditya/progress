# https://codeforces.com/problemset/problem/71/A

clara = int(input())
lana = input()
if len(lana) <= 10:
    print(lana)
else:
    print(lana[0],len(lana)-2,lana[-1], sep='')
while clara > 1:
    j = input()
    if len(j) <= (len(lana) and 10):
        print(j)
    else:
        print(j[0],len(j)-2,j[-1], sep='')
    clara = clara - 1

# (c) 2021, Vikramaditya V. Vajire
# https://github.com/vikramaditya
# This source code is licensed under the MIT License
