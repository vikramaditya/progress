"""
# https://cses.fi/problemset/task/1068
CSES Problem Set : Weird Algorithm
"""
n = int(input())
arr = []
while n!= 1:
    arr.append(n)
    if n % 2 == 0:
        n = n // 2
    else:
        n = n * 3 + 1

arr.append(1)
print(*arr)
