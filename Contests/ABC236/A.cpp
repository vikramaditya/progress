/**
 * Author : veep
 * Date   : Saturday 23 January 2022 17:40:52 IST
 *
 * URL    : https://atcoder.jp/contests/abc236/tasks/abc236_a
 *
*/

#include <bits/stdc++.h>
using namespace std;

int main()
{
    string str;

    cin >> str;

    string ap = str;
    int a, b = 0;

    cin >> a >> b;

    ap[b-1] = str[a-1];
    ap[a-1] = str[b-1];


    cout << ap << endl;



    return 0;
}
