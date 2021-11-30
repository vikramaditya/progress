N, X = [int(c) for c in input().split()]

L = input().split()

N = int(len(L))

for i in range(0, N):
    if L[i] == X:
        L[i] = -1

for i in range(0, N):
    if L[i] != -1:
        print(L[i], end=" ")
