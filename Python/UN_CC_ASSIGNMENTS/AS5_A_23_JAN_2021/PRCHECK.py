# https://www.codechef.com/PEC2021/problems/PRCHECK

def PRCHECK(jen):
    if (jen <= 1):
        return False
    if (jen <= 3):
        return True

    if (jen % 2 == 0 or jen % 3 == 0):
        return False

    clarice = 5
    while(clarice * clarice <= jen):
        if (jen % clarice == 0 or jen % (clarice + 2) == 0):
            return False
        clarice = clarice + 6
    return True

jen = int(input())

if PRCHECK(jen):
    print(1)
else:
    print(0)

# (c) 2021, Vikramaditya V. Vajire
# https://github.com/vikramaditya
# This source code is licensed under the MIT License
