/**
 * Author   : veep
 * Date     : Friday, 27 May 2022 23:20:44 IST
 */

#include "bits/stdc++.h"
using namespace std;
#define endl "\n";
#define space " "

void solve(){
    string str; cin >> str;

    int upper = 0;
    int lower = 0;

    for (int i = 0; i < str.length(); i++) {
        char a = str[i];
        //cout << a << space;
        if (isupper(a)) {
            upper++;
        } else {
            lower++;
        }
    }

    if (upper > lower) {
        for (int i = 0; i < str.length(); i++) {
            char a = toupper(str[i]);
            cout << a;
        
        }
    } else {
        for (int i = 0; i < str.length(); i++) {
            char a = tolower(str[i]);
            cout << a;
        
        }
    }

    //cout << upper << space << lower << str.length() << endl;

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

