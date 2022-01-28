/**
 * Author	:	veep
 * Date	    :	Sat Jan 29 03:08:43 IST 2022
 *
 * Codeforces practise session.
 * Problem Code	:	71A
 */
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
	cin >> n;

	while (n) {
		string str;
		cin >> str;
		long k;
		k = str.length();
		if (k > 10) {
			cout << str[0] << k - 2 << str[k - 1] << endl;
		} else {
			cout << str << endl;
		}
		n--;
	}
    return 0;
}
