j = int(input())

while j > 0:
    s = 0
    y = int(input())
    while y > 0:
        s = s + (y % 10)
        y = y // 10
    print(s)
    j = j -1
    
# (c) 2021, Vikramaditya V. Vajire
# https://github.com/vikramaditya
# This source code is licensed under the MIT License
