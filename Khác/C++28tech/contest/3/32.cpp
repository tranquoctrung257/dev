#include <bits/stdc++.h>
using namespace std;
#define ll long long 

int main(){
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    int n; cin >> n;
    int so = 65;
    for(int i = 1;i<=n;i++){
        for(int j = 1;j<=i;j++){
            cout << (char)so << " ";
            
        }
        so++;
        cout << endl;
    }
}