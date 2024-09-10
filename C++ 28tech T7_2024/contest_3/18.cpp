#include <bits/stdc++.h>
using namespace std;
 
using ll = long long;
using db = double;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    ll n;cin >> n;
    int ans = 0;
    while(n){
        int dv = n%10;
        if(dv == 2 || dv == 3 || dv == 5 || dv == 7){
            ans++;
        }
        n/=10;
    }
    cout << ans << endl;
}