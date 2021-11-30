import re
t = int(input())
for f in range(t):
    N, K = [int(c) for c in input().split()]
    go = input()
    mine = 0
    res = max(re.findall('((?:' + re.escape('*') + ')*)', go), key = len)
    mine = len(res)
    final = "NO"
    if mine >= K:
        final = "YES"
    print(final)
