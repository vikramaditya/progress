/**
 * Author   : veep
 * Date     : Tuesday, 22 February 2022 20:06:33 IST
 *
 * Fancy new template!
 */

#include "bits/stdc++.h"
using namespace std;

void solve(){
    string str;
    cin >> str;
    
    vector<char> all;
    bool flag = true;
    for (int i = 0; i < str.length(); i++) {
        char tmp;
        tmp  = str[i];
        all.push_back(tmp);
        if (tmp == 'r' || tmp == 'g' || tmp == 'b') {
            
        } else {
            char x;
            x = tolower(tmp);
            auto ok = find(all.begin(), all.end(), x);
            if (ok != all.end()) {
                all.erase(ok);
            } else {
                flag = false;            
            }
        }
    
    }

    if (flag == true) {
        cout << "YES\n";
    } else {
        cout << "NO\n";
    }
    return;
}


int32_t main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);
    
    int test_cases = 1;
    cin >> test_cases;
    
    for(int i = 1; i <= test_cases; i++){
        solve();
    }
    
    return 0;
}

