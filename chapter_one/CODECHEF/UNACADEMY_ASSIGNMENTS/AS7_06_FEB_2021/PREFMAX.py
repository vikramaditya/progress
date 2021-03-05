# https://www.codechef.com/PEC2021C/problems/PREFMAX

def prefmax(n):
    f = []
    y = []
    go = 1
    for h in range(0,n):
        g = int(input())
        f.append(g)

    y.append(f[0])

    for h in range(1,n-1):
        y.append(max(f[h], y[h-1]))

    for h in range(0, n-1):
        if f[h+1] > y[h]:
            go += 1
    return go

n = int(input())
print(2)
print(prefmax(n))
