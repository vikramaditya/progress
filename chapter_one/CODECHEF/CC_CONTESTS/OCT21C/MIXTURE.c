/**
Author: valisport
Date: Friday 01 October 2021 10:35:36 PM IST
*/

#include "stdio.h"

int main()
{
  int t, i = 0;
  scanf("%d", &t);
  while (i < t) {
    int A, B;
    scanf("%d %d", &A, &B);
    if (A > 0 && B > 0) {
      printf("Solution\n");
    } else if (B == 0) {
      printf("Solid\n");
    } else if (A == 0) {
      printf("Liquid\n");
    }
    i++;
  }
  return 0;
}

