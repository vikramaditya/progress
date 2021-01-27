# https://www.codechef.com/problems/INTEST

n, k = map(int, input().split())
c = 0
while n > 0:
    j = int(input())
    if j % k == 0:
        c = c + 1
    n = n - 1
print(c)

# (c) 2021, Vikramaditya V. Vajire
# https://github.com/vikramaditya
# This source code is licensed under the MIT License
