jen = int(input())
if jen > 5:
    quit()

for x in range(jen):
    A, B, C = [int(A) for A in input().split()]

    if A + B == C or B + C == A or A + C ==B:
        print('YES')
    else:
        print("NO")
