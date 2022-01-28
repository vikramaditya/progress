/**
 * Author	:	veep
 * Date	    :	Sat Jan 29 02:40:52 IST 2022
 *
 * Codeforces practise session.
 * Problem Code	:	4A
 */
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
	cin >> n;

	string res;

	if (n % 2 == 0 & n!= 2) {
		res = "YES";
	} else {
		res = "NO";
	}
	cout << res << endl;

    return 0;
}
