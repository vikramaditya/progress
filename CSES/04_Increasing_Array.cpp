/**
  * Author  :  veep
  * Date    :  Saturday 22 January 2022 03:42:39 AM IST
  * URL     :  https://cses.fi/problemset/task/1094
*/

#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;

    int i = 0;
    long long res = 0;
    long long count = 0;
    cin >> count;
    while (i < n-1){
        int c = 0;
        cin >> c;

        if (c < count) {
            while (c < count) {
                res += count - c;
                c = count;
            }
            // cout << res << endl;
        }
        count = c;
        i++;
    }

    cout << res << "\n";
    return 0;
}
