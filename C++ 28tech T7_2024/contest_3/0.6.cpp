#include <bits/stdc++.h>
using namespace std;
 
using ll = long long;
using db = double;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    ll n;cin >> n;
    int tong = 0,r = n % 10;
    while(n!=0){
        tong+= abs(n%10-r);
        n/=10;
    }
    cout << tong << endl;

}