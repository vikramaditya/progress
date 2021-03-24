n = int(input())
given = [int(c) for c in input().split()]
ele = [i for i in range(1, n+1) if i not in given]
print(ele[0])
