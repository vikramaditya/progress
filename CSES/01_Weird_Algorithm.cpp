/**
  * Author  :   veep
  * Date    :   Thursday 13 January 2022 01:41:31 AM IST
  * URL     :   https://cses.fi/problemset/task/1068
*/
 
#include <bits/stdc++.h>
using namespace std;

int main()
{
    long long n;
    cin >> n;
    
    cout << n << " ";
    
    while (n != 1) {
        if (n % 2 == 0) {
            n = n / 2;
            cout << n << " ";
        } else {
            n = (n * 3 ) +1;
            cout << n << " ";
        }
    }
    return 0;
}
    
    
