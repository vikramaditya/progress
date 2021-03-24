// https://www.codechef.com/problems/INTEST

#include <stdio.h>

int main()
{
  int n;
  int k;
  int c;
  int j;

  scanf("%d %d", &n, &k);
  c = 0;
  for(n; n>0; n--){
    scanf("%d", &j);
    if (j%k == 0){
      c++;
    }
  }
  printf("%d", c);
  return 0;
}
