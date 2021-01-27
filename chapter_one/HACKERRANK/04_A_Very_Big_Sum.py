# https://www.hackerrank.com/challenges/a-very-big-sum/problem

clara = int(input())

jane = input().split()
jane = list(jane)

sum = 0
i = 0
while i < clara:
    jane[i] = int(jane[i])

    sum =  sum + jane[i]
    i +=1
print(sum)


# (c) 2021, Vikramaditya V. Vajire
# https://github.com/vikramaditya
# This source code is licensed under the MIT License
