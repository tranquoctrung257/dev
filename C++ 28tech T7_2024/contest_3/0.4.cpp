#include <bits/stdc++.h>
using namespace std;
 
using ll = long long;
using db = double;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;cin >> n;
    int i = 3;
    while(i <= n){
        cout << i << " ";
        i+=3;
    }
    i = 0;
    while(i<=n){
        cout << i << " ";
        i+=15;
    }

    i = n;
    while(true){
        if(i % 7 == 0){
            cout << i << endl;
            break;
        }
        ++i;
    }
    while(true){
        if(i % 9 == 0){
            cout << i << endl;
            break;
        }
        ++i;
    }
    i = 1;
    while(i <= 2*n-1){
        cout << i << " ";
        i+=2;
    }
}