# https://www.codechef.com/problems/LUCKFOUR

d = int(input())
while d > 0:
    s = 0
    sf = input()
    jd = [int(d) for d in str(sf)]
    i = len(jd) - 1
    while i >= 0:
        if sf[i] == '4':
            s = s + 1
        i = i - 1

    print(s)
    d = d - 1
    
# (c) 2021, Vikramaditya V. Vajire
# https://github.com/vikramaditya
# This source code is licensed under the MIT License
