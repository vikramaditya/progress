/**
 * Author : veep
 * Date   : Saturday 23 January 2022 19:20:17 IST
 *
 * URL    : https://atcoder.jp/contests/abc236/tasks/abc236_b
 * Upsolved.
 *
*/

#include <bits/stdc++.h>
using namespace std;

int main()
{
    long long n = 0;
    cin >> n;

    long long v = (4 * n) - 1;

    vector<long long> arr(n + 1);

    long long i = 0;

    while (i < v) {
        int x = 0;
        cin >> x;
        arr[x] += 1;
        i++;
    }

    for (int i = 0; i <= n; i++) {
        if (arr[i] == 3) {
            cout << i << "\n";
            break;
        }
    }


    return 0;
}
