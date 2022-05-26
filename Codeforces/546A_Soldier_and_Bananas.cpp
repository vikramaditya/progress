/**
 * Author   : veep
 * Date     : Thursday 26 May 2022 16:36:03 IST
 */

#include "bits/stdc++.h"
using namespace std;
#define endl "\n";
#define space " "

void solve(){
    int k, n ,w; cin >> k >> n >> w;

    int tmp = 0;

    for (int i = 1; i <= w; i++) {
        tmp += i*k;
    }

    int res = tmp - n;

    if (res < 0) {
        cout << 0 << endl;
    } else {
        cout << res << endl;
    }

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

