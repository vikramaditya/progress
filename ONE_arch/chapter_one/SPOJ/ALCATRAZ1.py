N = int(input())

for d in range(0, N):
    T = map(int, input())
    T = list(T)
    some = 0
    for x in range(0, len(T)):
        some += T[x]
    print(some)
