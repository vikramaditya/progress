/**
Author: valisport
Date: Sunday 17 October 2021 12:07:27 AM IST
*/

#include <iostream>
using namespace std;
int main(void)
{
    int t;
    cin >> t;

    for (int i = 0 ; i < t; ++i) {
        int go[5];
        cin >> go[0] >> go[1] >> go[2] >> go[3] >> go[4];
        int India = 0;
        int Looters = 0;
        int Draw = 0;
        for (int i = 0; i < 5; i++) {
            if (go[i] == 1) {
                India++;
            } else if (go[i] == 2) {
                Looters++;
            } else if (go[i] == 0) {
                Draw++;
            }
        }
        if (India == Looters) {
            cout << "DRAW" << endl;
        } else if (India > Looters) {
            cout << "INDIA" << endl;
        } else {
            cout << "ENGLAND" << endl;
        }
    }
    
    return 0;
}
