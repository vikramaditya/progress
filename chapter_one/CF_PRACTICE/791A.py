# https://codeforces.com/problemset/problem/791/A

a,b = [int(f) for f in input().split()]

x = 0

while True:
    if a > b:
        break
    else:
        a = a * 3
        b = b * 2
        x += 1
print(x)
