// https://www.codechef.com/INPRG01/problems/VALTRI

#include <stdio.h>

int main()
{
  int j;
  scanf("%d", &j);

  if (j % 5 == 0 || j % 6 == 0){
    printf("YES");
  }
  else{
    printf("NO");
  }

}
