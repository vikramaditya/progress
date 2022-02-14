/**
 * Author    : veep
 * Date      : Wednesday 02 February 2022 01:32:55 AM IST
 *
 * Code      : 1626B
 *
 * Codeforces practise session.
 */

#include <bits/stdc++.h>
using namespace std;

/*
for _ in range(int(input())):
  x = [ord(c) - ord('0') for c in input()]
  n = len(x)
  for i in range(n - 2, -1, -1):
    if x[i] + x[i + 1] >= 10:
      x[i + 1] += x[i] - 10
      x[i] = 1
      break
  else:
    x[1] += x[0]
    x.pop(0)
  print(''.join([chr(c + ord('0')) for c in x]))

The above python solution is from tutorial 
Think bruh, think vro, think!
*/
