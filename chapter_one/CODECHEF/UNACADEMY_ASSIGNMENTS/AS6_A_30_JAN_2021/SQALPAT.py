# https://www.codechef.com/PEC2021B/problems/SQALPAT

n = int(input())
i = int(1)

while n>0:
    k = int(5)
    while k>0:
        print(i, end=" ")
        i += 1
        k -= 1
    i += 4
    n -= 1
    if n == 0:
        quit()
    print(" ")
    k = int(5)
    while k>0:
        print(i, end=" ")
        i -= 1
        k -= 1
    i += 6
    n -= 1
    if n == 0:
        quit()
    print(" ")
