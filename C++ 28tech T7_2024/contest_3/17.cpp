#include <bits/stdc++.h>
using namespace std;
 
using ll = long long;
using db = double;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    ll n;cin >> n;
    ll tong = 0;
    while(n!=0){
        tong += n%10;
        n/=10;
    }
    cout << tong << endl;
}