/**
 * Author : veep
 * Date   : Saturday 15 January 2022 03:47:08 PM IST
 *
 * URL    : https://www.codechef.com/JAN222C/problems/EXAMTIME
 *
 */

#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;

    for (int i = 0; i < n; i++) {
        int dDSA, dTOC, dDM = 0;
        int sDSA, sTOC, sDM = 0;

        cin >> dDSA >> dTOC >> dDM;
        cin >> sDSA >> sTOC >> sDM;

        int sloth_total, dragon_total = 0;

        sloth_total = sDSA + sTOC + sDM;
        dragon_total = dDSA + dTOC + dDM;

        string res = "";

        if (sloth_total > dragon_total) {
            res = "SLOTH";
        } else if (sloth_total < dragon_total) {
            res = "DRAGON";
        } else if (dDSA > sDSA) {
            res = "DRAGON";
        } else if (dDSA < sDSA) {
            res = "SLOTH";
        } else if (dTOC > sTOC) {
            res = "DRAGON";
        } else if (dTOC < sTOC) {
            res = "SLOTH";
        } else {
            res = "TIE";
        }

        cout << res << endl;
    }
    return 0;
}
