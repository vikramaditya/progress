# https://www.codechef.com/PEC2021/problems/RNGEODD

l, r = [int(n) for n in input().split()]
od = []

while r >= l:

    if r%2 != 0:
        od.append(r)
    r = r - 1
od.reverse()

i = 0
while i < len(od):
    print(od[i], end=" ")
    i += 1
    
# (c) 2021, Vikramaditya V. Vajire
# https://github.com/vikramaditya
# This source code is licensed under the MIT License
