# https://www.hackerrank.com/challenges/compare-the-triplets/problem

clara = input().split()
clara = list(clara)

jane = input().split()
jane = list(jane)

man = 3
i = 0
bob = 0
alice = 0
while man > 0:
    clara[i] = int(clara[i])
    jane[i] = int(jane[i])
    if clara[i] < jane[i]:
        bob = bob + 1
    if jane[i] < clara[i]:
        alice = alice + 1
    i += 1
    man -= 1
print(alice, bob)

# (c) 2021, Vikramaditya V. Vajire
# https://github.com/vikramaditya
# This source code is licensed under the MIT License
