#include <bits/stdc++.h>
using namespace std;
 
using ll = long long;
using db = double;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int n;cin >> n;
    for(int i=1;i<=n;i++){
        cout << "Hello 28tech" << endl;
    }
    for(int i=1;i<=n;i++){
        cout << i << ' ';
    }
    cout << endl;
    for(int i=0;i<=n-1;i++){
        cout << i << ' ';
    }
    cout << endl;
    for(int i=n;i>=1;i--){
        cout << i << ' ';
    }
    cout << endl;
    for(int i=n-1;i>=0;i--){
        cout << i << ' ';
    }
    cout << endl;
}