"""
Author: valisport
Date: Thursday 10 June 2021 08:00:34 PM IST
"""

t = int(input())

for f in range(t):
    n = int(input())
    stones = [int(c) for c in input().split()]
    
    low = min(stones)
    high = max(stones)

    #print(low, high)

    ct = 0
    go = stones
    while True:

        one = stones.index(low)
        two = stones.index(high)
        
        if one > two:
            go.pop(0)
            ct += 1
        newct = go.count(high)
        if newct == 0:
            break
        
        if two > one:
            go.pop(-1)
            ct += 1
        
        newct = go.count(low)
        if newct == 0:
            break
            
    print(ct)

