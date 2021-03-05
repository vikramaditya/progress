# https://www.codechef.com/PEC2021B/problems/NTSMPAT

n = int(input())
i = int(1)

for i in range(1, n+1):
    count = int(2*i-1)
    maxn = count
    first = i
    while count>0 and first <= maxn:
        print (first, end= " ")
        first += 1
        count -= 1
    first -= 2
    while count>0:
        print (first , end= " ")
        first -= 1
        count -= 1
    print (" ")
