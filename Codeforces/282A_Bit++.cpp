/**
 * Author   : veep
 * Date     : Thursday, 24 February 2022 00:48:53 IST
 *
 * Codeforces practise session
 * Code     : 282A
 */

#include "bits/stdc++.h"
using namespace std;

void solve(){
    
    /* Code here */

    return ;
}


int32_t main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    
    int test_cases = 1;
    cin >> test_cases;
    
    int res = 0;

    for(int i = 1; i <= test_cases; i++){
        string str;
        cin >> str;

        if (str == "++X" || str == "X++") {
            res++;
        } else {
            res--;
        }
    }
    cout << res << "\n";
    
    return 0;
}

