// https://www.codechef.com/INPRG01/problems/SECLAR

#include <stdio.h>
int main(){
  int A;
  int B;
  int C;
  int L;

  scanf("%d %d %d", &A, &B, &C);

  if (B >= A && A >= C && B >= C){
    L = A;
  }

  if (C >= A && A >= B && C >= B){
    L = A;
  }

  if (A >= B && B >= C && A >= C){
    L = B;
  }

  if (C >= B && B >= A && C >= A){
    L = B;
  }

  if (A >= C && C >= B && A >= B){
    L = C;
  }

  if (B >= C && C >= A && B >= A){
    L = C;
  }

  printf("%d", L);

  return 0 ;

}
