/**

Author: valisport
Date: Monday 11 October 2021 08:50:10 PM IST

*/

#include <stdio.h>

int max(int a, int b);

int main(void)
{
	int t;
	scanf("%d", &t);

	while (t) {
		int n, res;
		scanf("%d", &n);

		if (n == 1) {
			res = 1;
		}
		else {
			int tmp = 1;
			while (tmp * 2 <= n) {
				tmp *= 2;
			}
			int ct;
			ct = n - tmp + 1;

			if (n == tmp) {
				res = tmp/2;
			}
			else {
				res = max(ct, tmp/2);
			}
		}
		printf("%d\n", res);
		t--;
	}
}

int max(int a, int b)
{
	if (a >= b)
		return a;
	else
		return b;
}

