#include <stdio.h>

int main()
{
    int x, y;

    scanf("%d", &x);

    y = x / 5;

    if (x % 5 > 0){
        y++;
    }

    

    printf("%d", y);

    return 0;
}