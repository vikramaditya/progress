# https://www.codechef.com/PEC2021B/problems/REPLME

n = int(input())
j = []

for n in range(n):
    c = int(input())
    j.append(c)

def one(n):
    if len(j) == 1:
        return j[0]
    elif len(j) > 1:
        d = min(j)
        j.remove(d)

        e = min(j)
        j.remove(e)

        j.append((3 * d + 2 * e) % 100)

        return one(n - 1)

print(one(n))
