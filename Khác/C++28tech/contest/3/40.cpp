#include <bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    int n;cin >> n;
    // ll n = 3;
    for(int i = 1;i<=n;i++){
        for(int j = 1;j<=10;j++){
            cout << i << " " << "x" << " " << j << " = " << i*j<<endl;
        }
        cout << endl;
    }
}