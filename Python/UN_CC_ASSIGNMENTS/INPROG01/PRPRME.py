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
clara = []
shizuka = 1
jena = jen

while len(clara) < jena:
    if PRCHECK(shizuka):
        clara.append(shizuka)
    shizuka += 1

cesar = 0
while cesar < len(clara):
    print(clara[cesar], end=" ")
    cesar += 1
 
# (c) 2021, Vikramaditya V. Vajire
# https://github.com/vikramaditya
# This source code is licensed under the MIT License
