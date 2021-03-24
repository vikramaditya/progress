T = int(input())

for c in range(0, T):
    case = input().split("0")
    case = list(filter(None,case))
    print(len(case))
