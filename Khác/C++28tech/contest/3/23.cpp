#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    // int n;cin >> n ;
    ll n = 5;
    // hinh 1
    int dem = 1;
    for(int i = 1;i<=n;i++){
        for(int j = 1;j<=n;j++){
            cout << dem << " ";++dem;
        }
        cout << endl; 
    }
    cout << endl;
    // hinh 2
    for(int i = 1;i<=n;i++){
        int khoitao = i;
        for(int j = 1;j<=n;j++){
            cout << khoitao << " ";++khoitao; 
        }
        cout << endl;
    }
    cout << endl;
    // hinh 3
    for(int i = 1;i<=n;i++){
        for(int j = 1;j<=n;j++){
            if(j<=n-i){cout << "~";}
            else cout << i;
        }
        cout << endl;
    }
    cout << endl;
    // hinh 4
    for(int i = 1;i<=n;i++){
        int ktao = i;
        int dem = n -1;
        for(int j = 1;j <=i;j++){
            cout << ktao << " ";
            ktao +=dem;
            --dem;
        }
        cout << endl;
    }
}