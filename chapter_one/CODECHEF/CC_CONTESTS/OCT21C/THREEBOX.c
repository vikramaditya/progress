/**
Author: valisport
Date: Friday 01 October 2021 11:25:27 PM IST
*/

#include "stdio.h"

int main()
{
  int t, i = 0;
  scanf("%d", &t);

  while (i < t) {
    int A, B, C, D, res;
    scanf("%d %d %d %d", &A, &B, &C, &D);
    if ((A+B+C) <= D)
      res = 1;
    else if ((A + B) <= D ||(A + C) <= D || (C + B) <= D)
      res = 2;
    else
      res = 3;
    printf("%d\n", res);
    i++;
  }
  return 0;
}

