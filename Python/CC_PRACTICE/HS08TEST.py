# https://www.codechef.com/problems/HS08TEST

x, y = map(float, input().split())

if x % 5 == 0 and x + 0.50 <= y:
    bal = (y - x) - 0.50
    print(bal)
else:
    print(y)
    
# (c) 2021, Vikramaditya V. Vajire
# https://github.com/vikramaditya
# This source code is licensed under the MIT License
