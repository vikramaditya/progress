# https://codeforces.com/contest/59/problem/A

stringer = str(input())
upper = 0
lower = 0

for ele in stringer:
    if ele.islower():
        lower += 1
    if ele.isupper():
        upper += 1

if lower == upper or upper < lower:
    stringer = stringer.lower()

if lower < upper:
    stringer = stringer.upper()

print(stringer)
