/**
  * Author  :  veep
  * Date    :  Saturday 22 January 2022 01:18:49 AM IST
  * URL     :  https://cses.fi/problemset/task/1083/
*/

#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;
    vector<int> fd;
    int j = 0;

    while (j < n-1) {
        int x = 0;
        cin >> x;
        fd.push_back(x);
        j++;
        }

        sort(fd.begin(), fd.end());

        int i = 0;

        int res = 0;
        while (i < n-1) {
            if (fd[i] != i+1) {
                res = i+1;
                break;
            }
            i++;
        }

        if (res != 0) {
            cout << res << "\n";
        } else {
            cout << n << "\n";
        }
    return 0;
}
