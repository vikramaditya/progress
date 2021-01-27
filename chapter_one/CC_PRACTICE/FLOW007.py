# https://www.codechef.com/problems/FLOW007

n = int(input())

while n>0:
    k = int(input())
    i = 0
    while k > 0:
        i = i*10 + (k%10)
        k = k//10
    n = n - 1
    print(i)
    
# (c) 2021, Vikramaditya V. Vajire
# https://github.com/vikramaditya
# This source code is licensed under the MIT License
