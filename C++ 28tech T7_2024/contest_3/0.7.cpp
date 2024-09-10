#include <bits/stdc++.h>
using namespace std;
 
using ll = long long;
using db = double;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    ll n;cin >> n;
    int dv = n%10;
    while(n){
        if(n%10>dv){
            dv = n%10;
        }
        n/=10;
    }
    cout << dv << endl;
    
}