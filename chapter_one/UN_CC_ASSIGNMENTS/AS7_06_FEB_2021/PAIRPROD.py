# https://www.codechef.com/PEC2021C/problems/PAIRPROD
def jen(n):
    A = []
    B = []
    go = 0
    for i in range(0,n):
        f = int(input())
        A.append(f)
    B.append(A[n-1])

    for j in range(1,n-1):
        B.append(B[j-1]+ A[n-j-1])

    for k in range(0,n-1):
        go += A[k] * B[n-2-k]
    return go
print(2)
n = int(input())
print(jen(n))
