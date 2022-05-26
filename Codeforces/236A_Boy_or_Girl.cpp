/**
 * Author   : veep
 * Date     : Tuesday 15 February 2022 02:38:44 PM IST
 *
 * Code     : 236A
 *
 * Codeforces practise session.
 */

#include "bits/stdc++.h"
using namespace std;

int main() {
    string str;
    cin >> str;

    set<char> arr;
    int a;
    a = str.length();

    for (int i = 0; i < a; i++) {
        arr.insert(str[i]);
    }
    int b = arr.size();
    string res;

    if (b % 2 == 0) {
        res = "CHAT WITH HER!";
    } else {
        res = "IGNORE HIM!";
    }
    cout << res << endl;


}
