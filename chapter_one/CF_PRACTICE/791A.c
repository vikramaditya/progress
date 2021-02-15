// # https://codeforces.com/problemset/problem/791/

#include <stdio.h>

int main()
{
  int a;
  int b;
  int x;

  scanf("%d %d", &a, &b);

  for(x = 0; a <= b; x++){
    a = a * 3;
    b = b * 2;
  }
  printf("%d", x);

  return 0;
}
