/**
 * Author   : veep
 * Date     : Thursday, 26 May 2022 18:38:11 IST
 */

#include "bits/stdc++.h"
using namespace std;
#define endl "\n";
#define space " "

void solve(){
    int x; cin >> x;
    int res = 0;

    res = x+4;
    res = res/5;

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

