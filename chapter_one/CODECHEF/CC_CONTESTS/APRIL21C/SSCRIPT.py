import re
t = int(input())

if t < 1 or t > 10:
    exit()

sum = 0
for f in range(t):
    N, K = [int(c) for c in input().split()]

    if N <= 10 ** 4:
        sum += N

    if sum > 10 ** 4:
        exit()

    if N > 10 ** 6:
        exit()

    if N <= 10 ** 6 and sum >= 10 ** 6:
        exit()
    if K > N:
        exit()

    if K < 1:
        exit()

    go = input()

    if len(go) != N:
        exit()

    mine = 0
    res = max(re.findall('((?:' + re.escape('*') + ')*)', go), key = len)

    mine = len(res)

    final = "NO"
    if mine >= K:
        final = "YES"

    print(final)
