def dice(n):
    stacks = n // 4
    elem = n % 4

    res = 0

    if n == 1:
        res = 20
    elif n == 2:
        res = n * (18)
    elif n == 3:
        res = 2 * (18) + 18 - n
    elif n >= 4:
        if elem == 0:
            res += 4 * (11) * stacks
            res += 16
        elif elem == 1:
            res += 4 * 11 * stacks
            res += 12
            res += 20
        elif elem == 2:
            res += 4 * (11) * stacks
            res += elem * 4
            res += elem * (18)
        elif elem == 3:
            res += 4 * (11) * stacks
            res += 4
            res += 2 * (18) + 15
    return res

t = int(input())

for f in range(t):
    n = int(input())
    print(dice(n))
