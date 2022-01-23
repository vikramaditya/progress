/**
  * Author  : veep
  * Date    : 23-01-2022 21:01:36
  *
  * URL     : https://www.codechef.com/COOK137C/problems/PIZZA_BURGER
*/

#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;

    while (n) {
        int x, y, z;
        x = 0;
        y = 0;
        z = 0;

        cin >> x >> y >> z;

        string res;

        if (y <= x) {
            res = "PIZZA";
        } else if (z <= x) {
            res = "BURGER";
        } else {
            res = "NOTHING";
        }
        cout << res << endl;
        n--;
    }


    return 0;
}
