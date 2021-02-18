// https://www.codechef.com/INPRG01/problems/EOMUL

#include <stdio.h>

int main()
{
  int j;
  scanf("%d", &j);

  if (j % 3 != 0){
    printf("%d", -1);
  }

  if (j % 3 == 0 && j % 2 != 0){
    printf("%d", 1);
  }

  if (j % 3 == 0 && j % 2 == 0){
    printf("%d", 0);
  }

}
