#include <bits/stdc++.h>
using namespace std;

int main(){
    float a,b,c,d; cin >> a >> b >> c >> d;
    float DTB = (a * 1 + b * 1 + c * 2 + d * 3 ) / 7;
    if (DTB >= 8 ) cout << "GIOI";
    else if (DTB < 8 && DTB >= 6.5) cout << "KHA";
    else if (DTB < 6.5 && DTB >= 5) cout << "TRUNG BINH";
    else if (DTB < 5) cout << "YEU";
}