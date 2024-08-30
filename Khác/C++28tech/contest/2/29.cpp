#include<bits/stdc++.h>
using namespace std;

int main(){
    long long a,b,c,d;cin >> a >> b >> c >> d;
    long long q = b / a;
    if (b*q==c && c*q==d) cout << "YES";
    else cout << "NO";

}