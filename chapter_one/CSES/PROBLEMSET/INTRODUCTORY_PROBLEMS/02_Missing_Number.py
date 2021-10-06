# https://cses.fi/problemset/task/1083/
"""
Introductory Problems : Missing Number
"""
n = int(input())
arr = [int(c) for c in input().split()]
arr.sort()

artwo = [int(c) for c in range(1, n+1)]
Found = False
for i in range(n-1):
    if arr[i] != artwo[i]:
        print(artwo[i])
        Found = True
        break
if Found == False:
    print(n)
