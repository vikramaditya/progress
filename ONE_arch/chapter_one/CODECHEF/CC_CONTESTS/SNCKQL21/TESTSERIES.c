/**
Author: valisport
Sunday 17 October 2021 02:00:35 AM IST
*/

#include <stdio.h>

int main(void)
{
    int t;
    scanf("%d", &t);

    for (int i = 0 ; i < t; ++i) {
        int go[5];
        scanf("%d %d %d %d %d", &go[0], &go[1], &go[2], &go[3], &go[4]);
        int India = 0;
        int Looters = 0;
        int Draw = 0;
        for (int i = 0; i < 5; i++) {
            if (go[i] == 1) {
                India++;
            } else if (go[i] == 2) {
                Looters++;
            } else if (go[i] == 0) {
                Draw++;
            }
        }
        if (India == Looters) {
            printf("DRAW\n");
        } else if (India > Looters) {
            printf("INDIA\n");
        } else {
            printf("ENGLAND\n");
        }
    }

    return 0;
}
