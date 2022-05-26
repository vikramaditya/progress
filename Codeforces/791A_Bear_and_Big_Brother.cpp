/**
 * Author   : veep
 * Date     : Tuesday 15 February 2022 03:28:39 PM IST
 *
 * Code     : 791A
 *
 * Codeforces practise session.
 */

#include "bits/stdc++.h"
using namespace std;

int main() {
    int limak, bob;
    cin >> limak >> bob;

    int cnt = 0;

    while(limak <= bob){
        cnt++;
        limak *= 3;
        bob *= 2;
    }

    cout << cnt << "\n";

}
