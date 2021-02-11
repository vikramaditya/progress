# https://www.codechef.com/PEC2021C/problems/CNTDIST

def cntdist(n):
    co = set()
    for d in range(0,n):
        g = int(input())
        co.add(g)
    return(len(co))

n = int(input())
print(2)
print(cntdist(n))
