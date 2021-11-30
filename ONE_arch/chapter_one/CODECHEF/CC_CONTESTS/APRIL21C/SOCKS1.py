A, B, C = [int(c) for c in input().split()]

res = "NO"

hello = A == B or A == C or B == C

bye = (A >= 1 and A <= 10) and (B >= 1 and B <= 10) and (C >= 1 and C <= 10)

if bye:
    pass
else:
    exit()

if  hello and bye:
    res = "YES"

print(res)
