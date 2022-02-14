/**
 * Author   : veep
 * Date     : Monday, 14 Feb 2022, 11:09 IST
 *
 * Code     : 339A
 *
 * Codeforces practise session.
 */

#include <bits/stdc++.h>
using namespace std;

int main(){
    string str1;
    cin >> str1;
    
    vector<int> arr;
    
    for (int i = 0; i < str1.size(); i++) {
        if (str1[i] != '+') {
            arr.push_back(str1[i]-'0');
        }
    }
    sort(arr.begin(), arr.end());
    
    for (int i = 0; i < arr.size(); i++) {
        cout << arr[i];
        if (i != arr.size()-1) {
            cout << '+';
        }
    }
    return 0;
}
