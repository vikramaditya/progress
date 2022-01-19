"""
 * Author : veep
 * Date   : Saturday 15 January 2022 17:42:48 IST
 *
 * URL    : https://atcoder.jp/contests/abc235/tasks/abc235_a
 *
"""

a = input()

c = a[1]+a[2]+a[0]
d = a[2]+a[0]+a[1]

e = int(a) + int(c) + int(d)
print(e)
