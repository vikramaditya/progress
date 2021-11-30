/**
Author: valisport
Date: Friday 05 November 2021 07:48:39 PM IST
*/

#include <stdio.h>

int main(void)
{
    int t;
    scanf("%d", &t);

    for (int i = 0; i < t; ++i) {
        int x, y, a, b, k;
        scanf("%d %d %d %d %d", &x, &y, &a, &b, &k);

        // printf("%d %d %d %d %d", x, y, a, b, k);

        int petrol = x;
        int diesel = y;

        for (int j = 0; j < k; ++j) {
            petrol += a;
            diesel += b;
        }

        if (petrol == diesel)
            printf("SAME PRICE\n");
        else if (petrol < diesel)
            printf("PETROL\n");
        else
            printf("DIESEL\n");
    }

    return 0;
}
