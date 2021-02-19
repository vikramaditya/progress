// # https://www.codechef.com/INPRG01/problems/CATSDOGS
#include <stdio.h> // visit again for 100% working solution. this one works only 60%

long long int main()
{
  int T;

  scanf("%lu", &T);
  while (T > 0) {
    int C, D, L;
    scanf("%lu %lu %lu", &C, &D, &L);
    int M;
    if (C > 2 * D){
      
      M = (C - 2 * D) * 4 + D * 4;
    }
    else {
      M = D * 4;
    }

    int N;
    N = (C+D)*4;

    if (L >= M && L <= N && L % 4 == 0){
      printf("%s", "yes\n" );
    }
    else {
      printf("%s", "no\n" );
    }
    T--;
    
  }
  return 0;
}

//  (c) 2021, Vikramaditya V. Vajire
//  https://github.com/vikramaditya
//  This source code is licensed under the MIT License
