# Pair of Primes
'''
Given an integer n (between 1 and 104) find two prime numbers (possibly same) p1,p2 such that p1+p2=n.
In case there are multiple solutions, you can output any of them.
If there is no solution, then print -1 -1 instead.
'''
"""
Sample Input
3
4
5
1
Sample Output
2 2
2 3
-1 -1
"""
def floor(n): # Defining floor beacuse importing the math library was increasing time.
    res = int(n)
    return res if res == n or n >= 0 else res-1
def PRCHECK(n): # checking if the number is prime is not
    if n <= 1:
        return False

    max_div = floor(n ** 0.5)
    for i in range(2, 1 + max_div):
        if n % i == 0:
            return False
    return True

def PAIRPR1(arr, lenarr, sd): # checking the sum, i.e answer by hashing
    some = set()
    n = -1
    x = -1
    for i in range(0, lenarr):
        go = sd-arr[i] # substracting the number in the set from the given number and checking the answer
        if go in some:
            n = arr[i]
            x = go
            break
        some.add(arr[i])
    print(n, x)

T = int(input())
for c in range(0, T):
    sd = int(input())
    arr = []
    for i in range(1,sd+1): # fail safe
        if i == 2 or i == 3: # all even numbers were giving wrong answer. So, declared them at the start.
            arr.append(i)
        if PRCHECK(i):
            arr.append(i)
        i += 1
    PAIRPR1(arr, len(arr), sd)

"""
(c) 2021, Vikramaditya V. Vajire
https://github.com/vikramaditya
This source code is licensed under the MIT License
"""
