V, T, S, D = [int(c) for c in input().split()]


if V * T > D or D > V * S:
    print("Yes")
else:
    print("No")
