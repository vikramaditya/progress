"""
Author: valisport
Date: Thursday 12 August 2021 10:26:11 PM IST

Remove the appropriate comments before reusing.
"""


"""#!/bin/python3

import math
import os
import random
import re
import sys
""""
# Complete the solve function below.
def solve(s):
    indx = []
    res = ""
    for i in range(len(s)):
        if s[i] == " ":
            indx.append(i)
    tmpstr = [c for c in s.split()]
    go = []
    for ele in tmpstr:
        go.append(ele[0].upper()+ele[1:].lower())
    j = 0
    i = 0
    while i <= len(s):
        if i in indx:
            res += " "
        else:
            res += go[j] + " "
            i += len(go[j])
            j += 1
        i += 1
    return res

"""
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
"""
