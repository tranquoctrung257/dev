#include <bits/stdc++.h>
using namespace std;
#define ll long long 

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int n; cin >> n;
    double tong = 0;
    for(int i = 0;i<n;i++){
        int gt = 1;
        for(int j = 1;j<=i;j++){
        gt*=j;
        }
        tong += 1.0/gt;
    }
    cout << fixed << setprecision(4) << tong << endl;
    
        
}