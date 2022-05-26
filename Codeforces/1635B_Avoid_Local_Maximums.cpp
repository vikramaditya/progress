/**
 * Author   : veep
 * Date     :Monday 21 February 2022 03:30:09 PM IST
 * Codeforces Practise Session
 * Code     : 1635B
 */

#include "bits/stdc++.h"
using namespace std;

#define int long long

int32_t main() {
    int n; cin >> n;
    int x; x = n;
    while (x--) {
        int c; cin >> c;
        int arr[c];
        for (int i = 0; i < c; i++) {
            int j; cin >> j; arr[i] = j;
        }
        int ct = 0;
        for (int k = 1; k < c - 2; k++) {
            if (arr[k] > arr[k+1] && arr[k] > arr[k-1]) {
                arr[k+1] = max(arr[k], arr[k+2]);
                ct++;
            }
        }
        if (arr[c-2] > arr[c-1] && arr[c-2] > arr[c-3]) {
            arr[c-2] = arr[c-3];
            ct++;
        }
        if (c == 3) {
            if (arr[1] > arr[0] && arr[1] > arr[2]) {
                arr[1] = arr[2];
                ct = 1;
            } 
        }
        cout << ct << '\n';
        for (int l = 0; l < c; l++) {
            cout << arr[l];
            if (l != c-1) {
                cout << " ";
            }
        }
        cout << '\n';
    }
    return 0;
}

