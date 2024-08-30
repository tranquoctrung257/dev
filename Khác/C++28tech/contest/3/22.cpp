#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    int n;cin >> n ;
    // int n = 5;

    // hinh 1
    for(int i = 1;i<=n;i++){//in ra hang
        for(int j = 1;j <= i;j++){//in ra cot
            cout << "*";
        }
        cout << endl;
    }
    cout << endl;
    // hinh 2
        for(int i = n;i>=1;i--){
        for(int j = 1;j <= i;j++){
            cout << "*";
        }
        cout << endl;
    }
    cout << endl;
    // hoac
    // for(int i = 1;i<= n;i++){
    //     for(int j = 1;j<=n-i+1;j++){
    //         cout << "*";
    //     }
    //     cout << endl;
    
    // hinh 3
    for(int i = 1;i<=n;i++){
        for(int j = 1;j <=n ;j++){
            if(j <=n-i) cout << " ";
            else cout << "*";
        }
        cout << endl;
    }
    cout << endl;
    // hinh 4
    for(int i = 1;i<=n;i++){
        for(int j = 1;j <=n ;j++){
            if(j < i) cout << " ";
            else cout << "*";
        }
        cout << endl;
    }
    cout << endl;
    // hinh 5 
    for(int i = 1;i<= n;i++){
        for(int j = 1;j<=i;j++){
            if(i == 1|| i == n || j == 1|| i == j){cout << "*"; }
            else cout << " ";
        }
        cout << endl;
    }
}