# https://www.codechef.com/INPRG01/problems/SNAKPROC
R = int(input())

while R > 0:
    L = int(input())
    snk = input()

    snk = snk.replace(".", "")
    snk = snk.replace("HT", "")
    
    if len(snk) > 0:
        print("Invalid")
    else:
        print("Valid")
    R = R - 1

# (c) 2021, Vikramaditya V. Vajire
# https://github.com/vikramaditya
# This source code is licensed under the MIT License
