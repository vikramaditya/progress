#include <stdio.h>

int main()
{
    int n, in, out, passno;

    scanf("%d", &n);
    passno = 0;
    for(n; n>1; n--){
        scanf("%d %d", &in, &out);
        passno += in;
        passno -= out;
        
    }
    scanf("%d %d", &in, &out);
    passno += in;
    printf("%d", passno);

    return 0;

}