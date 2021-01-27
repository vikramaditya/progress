# https://www.codechef.com/problems/PASSWD
# WARNING - WRONG ANSWER - CHECK NEEDED

from re import search
import re
jen = input()

if not re.match("^[1 -20]*$", jen):
    quit()

jen = int(jen)

if type(jen) == int:
    pass
else:
    quit()

if jen <= 20:
    pass
else:
    quit()
while jen > 0:
    clara = input()
    if type(clara) == str:
        pass
    else:
        quit()
    sym = "@"
    sym2 = "#"
    sym3 = "&"
    sym4 = "?"
    if (any(x.isupper() for x in clara) and any(x.islower() for x in clara)
        and any(x.isdigit() for x in clara) and len(clara) >= 10 and (search(sym, clara) or search(sym2, clara) or search(sym3, clara) or search(sym4, clara)) and not(any(x.isdigit() for x in clara[0]) or any(x.isdigit() for x in clara[-1]))):
        print("YES")
    else:
        print("NO")

    jen = jen - 1

# (c) 2021, Vikramaditya V. Vajire
# https://github.com/vikramaditya
# This source code is licensed under the MIT License
