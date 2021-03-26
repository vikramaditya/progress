# https://acm.timus.ru/problem.aspx?space=1&num=1001
"""
1001. Reverse Root
"""

given = []
while True:
    try:
        line = [int(c) for c in input().split()]
    except EOFError:
        break
    for i in range(0,len(line)):
        given.append(line[i])

given = [x for x in given if x is not None]

for i in range(len(given)-1,-1,-1):
    a = given[i] ** 0.5
    a = round(a, 4)
    a = float(a)
    print(f'{a:.4f}')
