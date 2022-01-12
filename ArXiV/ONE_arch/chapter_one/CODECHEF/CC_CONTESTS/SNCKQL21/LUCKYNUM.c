/**
Author: valisport
Date: Sunday 17 October 2021 12:07:27 AM IST
*/


#include <stdio.h>

int main(void)
{
    int t;
    scanf("%d", &t);
    for (int i=0; i<t; ++i) {
        int go[3];
        scanf("%d %d %d", &go[0], &go[1], &go[2] );

        if (go[0] == 7 || go[1] == 7 || go[2] == 7)
            printf("YES\n");
        else
        printf("NO\n");
}

    return 0;
}
