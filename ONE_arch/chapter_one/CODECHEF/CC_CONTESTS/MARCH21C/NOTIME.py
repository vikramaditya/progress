def NOTIME():
    N, H, x = [int(x) for x in input().split()]

    ls = [int(x) for x in input().split()]
    res = "NO"

    for g in ls:
        if g+x >= H:
            res = "YES"

    print(res)
NOTIME()