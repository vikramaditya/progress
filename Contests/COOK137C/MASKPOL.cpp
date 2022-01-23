/**
  * Author  : veep
  * Date    : 23-01-2022 21:06:47
  *
  * URL     : https://www.codechef.com/COOK137C/problems/MASKPOL
*/

#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;

    while (n) {
        int x, y;
        x = 0;
        y = 0;

        cin >> x >> y;

        int non_infected = 0;

        non_infected = x - y;

        cout << min(y, non_infected) << endl;
        n--;
    }


    return 0;
}
