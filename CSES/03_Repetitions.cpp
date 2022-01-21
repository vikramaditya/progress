/**
  * Author  :  veep
  * Date    :  Saturday 22 January 2022 01:57:33 AM IST
  * URL     :  https://cses.fi/problemset/task/1069
*/

#include <bits/stdc++.h>
using namespace std;

int main()
{
    string str;

    cin >> str;

    int res = 0;
    int k = 0;

    k = str.length();

    vector<int> arr;

    for (int i = 0; i < k; i++) {
        if (str[i] == str[i+1]) {
            res ++;
        } else {
            arr.push_back(res);
            res = 0;
        }
    }

    cout << *max_element(arr.begin(), arr.end()) + 1 << "\n";



    return 0;
}
