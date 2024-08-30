#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    // int n;cin >> n ;
    ll n = 5;

    for(int i = 97;i<=96+n;i++){
        int ktao = i;
        for(int j = 1;j<=n;j++){
            cout << char(ktao);ktao++;
        }
    cout << endl;
    }

    // hoac
    for(int i = 1;i<=n;i++){
        int ktao = 96+i;
        for(int j = 1;j<=n;j++){
            cout << char(ktao);ktao++;
        }
    cout << endl;
    }
        
}