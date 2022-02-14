/**
 * Author   : veep
 * Date     : Monday, 14-Feb-22 05:23:16 UTC
 *
 * Code     : 112A
 *
 * Codeforces practise session.
 */

#include <bits/stdc++.h>
using namespace std;

int main(){
    string str1, str2;
    cin >> str1;
    cin >> str2;
    
    int res = 0;
     
    transform(str1.begin(), str1.end(), str1.begin(), ::tolower);
    transform(str2.begin(), str2.end(), str2.begin(), ::tolower);

    //cout << str1 << endl;
    //cout << str2 << endl;
    
    if (str1 == str2) {
        res = 0; 
        
    }
    else {
        if (str1 > str2) {
            res = 1;
        } else {
            res = -1;
        }
    }
    
    cout << res << endl;
    return 0;
}
