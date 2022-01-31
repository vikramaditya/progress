/**
 * Author   : veep
 * Date     : Mon Jan 31 21:07:42 IST 2022
 *
 * Code     : 158A
 *
 * Codeforces practise session.
 */

#include <bits/stdc++.h>
using namespace std;

int main(){
    int n, k, ct;
    cin >> n >> k;
    ct = n;
    int arr[n];

    for (int i = 0; i < n; i++) {
        int x;
        cin >> x;
        arr[i] = x;
    }

    int res = 0;
    int i = 0;
    while (i != k) {
        if (arr[i] > 0) {
            res += 1;
        }
        i++;
    }

    i = k;

    while (i != ct) {
        if (arr[i] == arr[k-1] && arr[i] > 0) {
            res += 1;
        }
        i++;
    }

    cout << res << endl;
    return 0;
}
