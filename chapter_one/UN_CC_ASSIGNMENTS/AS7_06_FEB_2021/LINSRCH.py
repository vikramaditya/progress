# https://www.codechef.com/PEC2021C/problems/LINSRCH

n = int(input())
co = set()
for g in range(0,n):
    c = int(input())
    co.add(c)

q = int(input())
print(1)
for g in range(0,q):
    c = int(input())

    if c in co:
        print('yes')
    else:
        print('no')
