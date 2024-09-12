#include <bits/stdc++.h>
using namespace std;
 
using ll = long long;
using db = double;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n; cin >> n;
    int check = 0;
    for(int i = 1;i<=n;i++){
        int N;cin >> N;
        if(N == 2022)check =1; 
    }
    if(check) cout << "YES" << endl;
    else cout << "NO" << endl;
}