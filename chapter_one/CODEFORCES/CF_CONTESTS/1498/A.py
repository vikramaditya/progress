# https://codeforces.com/contest/1498/problem/A
"""
GCD Sum
"""
def gcd(a,b):
    if b == 0:
        return a
    return gcd(b, a%b)

def sum(n):
    sum = 0
    while n != 0:
        sum = sum + n % 10
        n = n // 10
    return sum

t = int(input())

for f in range(t):
    n = int(input())
    some = sum(n)
    res = gcd(n,some)

    while res == 1:
        n += 1
        some = sum(n)
        res = gcd(n,some)

    print(n)
