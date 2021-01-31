j = int(input())


while j > 0:
    f = int(input())
    l = []
    g = input().split()
    l = list(g)

    i = 0

    while i < len(l):
        l[i] = int(l[i])
        i += 1
    i = 0
    count = 0
    while i < len(l):
        if l[i] % 2 == 0:
            count += 1
        i += 1
    odd = len(l) - count

    print(min(odd, count))
    j -= 1
