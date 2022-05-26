/**
 * Author   : veep
 * Date     : Thursday 26 May 2022 12:30:36 AM IST
 */

#include "bits/stdc++.h"
using namespace std;
#define endl "\n";
#define space " "

void solve(){
    int row, col = 0;
    int i, j = 0;

    for (row = 1; row < 6; row++) {
        for (col = 1; col < 6; col++) {
            int x; cin >> x;
            if (x == 1) {
                i = row;
                j = col;
            }
        }
    }

    // cout << "i = " << i << space << "j = " << j << endl;

    int res = 0;
   
    res = abs(3-i) + abs(3-j);

    cout << res << endl;
        
    return;
}

int32_t main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    int test_cases = 1;
    // cin >> test_cases;

    for(int i = 1; i <= test_cases; i++){
        solve();
    }

    return 0;
}

