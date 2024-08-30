#include<bits/stdc++.h>
using namespace std;

int main(){
    long long n,u1,d;cin >> n >> u1 >> d;
    long long un = u1 + (n-1) * d ;
    long long sn = (n * (u1+un)) / 2;
    cout << sn ;
    // hoac
    cout << n * u1 + (n*(n-1)) / 2 * d;

}