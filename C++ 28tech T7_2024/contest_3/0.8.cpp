#include <bits/stdc++.h>
using namespace std;
 
using ll = long long;
using db = double;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    ll n;cin >> n;
    ll ln = n %10;
    while(n>=10){
        int r = n % 10;
        // if(r > ln) r = ln;
        ln = max(ln,n%10);
        n/=10;
    }
    if(n >= ln) cout << "YES" << endl;
    else cout << "NO" << endl;
}