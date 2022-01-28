/**
 * Author   : veep
 * Date     : Sat Jan 29 03:40:31 IST 2022
 * Codeforces practise session.
 * Problem Code	:	231A
 */

#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;

    int res = 0;

    while (n) {
        int a, b ,c;
        cin >> a >> b >> c;
        if (a + b + c >= 2) {
            res += 1;
        }
        n--;
    }
    cout << res << endl;
    return 0;
}
