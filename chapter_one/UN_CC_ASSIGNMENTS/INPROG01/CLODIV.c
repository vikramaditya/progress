// https://www.codechef.com/INPRG01/problems/CLODIV

#include <stdio.h>

int main()
{
  int j;
  int k;
  int x;

  scanf("%d %d", &j, &k);
  x = j/k;
  x = x * k;

  printf("%d", x);

  return 0;
}
