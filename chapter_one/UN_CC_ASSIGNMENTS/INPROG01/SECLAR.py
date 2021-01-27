# https://www.codechef.com/INPRG01/problems/SECLAR
A = int(input())
B = int(input())
C = int(input())

if (B >= A) and (A >= C) and (B >= C):
    ln = A
if (C >= A) and (A >= B) and (C >= B):
    ln = A

if (A >= B) and (B >= C) and (A >= C):
    ln = B
if (C >= B) and (B >= A) and (C >= A):
    ln = B

if (A >= C) and (C >= B) and (A >= B):
    ln = C
if (B >= C) and (C >= A) and (B >= A):
    ln = C


print(ln)

# (c) 2021, Vikramaditya V. Vajire
# https://github.com/vikramaditya
# This source code is licensed under the MIT License
