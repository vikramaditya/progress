/**
 * Author	: veep
 * Date  	: Wednesday 02 February 2022 01:00:49 AM IST
 *
 * Code     : 158A
 *
 * Codeforces practise session.
 */

#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
	cin >> n;

	while (n) {
		int c;
        cin >> c;
        int res = 0;
        
        if (c % 7 == 0){
        	res = c;
        } else {
        	res = -1;
        	for (int i = 0; i < 10; i++) {
        		if ((c - c % 10 + i) % 7 == 0) {
        			res = c - c % 10 + i;
        		}
        	}
        }

        cout << res << endl;

		n--;
	}
    return 0;
}

