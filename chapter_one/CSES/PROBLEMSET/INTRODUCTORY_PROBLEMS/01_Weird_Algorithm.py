"""
# https://cses.fi/problemset/task/1068
CSES Problem Set : Weird Algorithm
Time limit: 1.00 s : Memory limit: 512 MB 
"""
n = int(input())
print(n, end=" ")
while True:
    if n == 1:
        break

    if n % 2 == 0 and n != 1:
        n = n//2
        print(n, end=" ")

    if n == 1:
        break

    if n % 2 != 0 and n!= 0:
        n = (n * 3) + 1
        print(n, end=" ")
