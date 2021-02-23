#include <stdio.h>

int main()
{
    int k, n, w, i, j, c, m;
    scanf("%d %d %d", &k, &n, &w);
    i = 1;
    j = 0;
    c = 0;
    for (i = 1; i <= w; i++){
        c = i * k;
        j += c;
    }    
    m = j - n;
    if (m < 0){
        printf("%d", 0);
    }
    else{
        printf("%d", m);
    }
    return 0;
}