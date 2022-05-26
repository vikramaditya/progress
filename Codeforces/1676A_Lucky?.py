"""
/**
 * Author   : veep
 * Date     : Tuesday 10 May 2022 08:14:33 PM IST
 */
"""

t = int(input())

for i in range(t):
    a = input()

    if ((int(a[0])+int(a[1])+int(a[2])) == (int(a[3])+int(a[4])+int(a[5]))):
        print("YES")
    else:
        print("NO")

