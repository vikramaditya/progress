k, n, w = [int(c) for c in input().split()]

i = 1
j = 0
while i <= w:
    c = i * k
    j += c
    i += 1

if (j-n) < 0:
    print(0)
else:
    print(j - n)
