/**
 * Author : veep
 * Date   : Saturday 15 January 2022 05:12:18 PM IST
 *
 * URL    : https://www.codechef.com/JAN222C/problems/MINFD
 *
 */

#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        int n, x = 0;

        cin >> n >> x;

        vector<int> fd;

        for (int j = 0; j < n; j++) {
            int y = 0;
            cin >> y;
            fd.push_back(y);
        }

        int balance = 0;

        sort(fd.begin(), fd.end(), greater<int>());
        for (int c = 0; c < fd.size(); c++) {
            balance += fd[c];

            if (balance >= x) {
                cout <<  c+1;
                break;
            }
        }
        if (balance < x) {
            cout << -1;
        }
        cout << endl;
    }
    return 0;
}
