#include<bits/stdc++.h>
using namespace std;
using ll = long long;

int main(){
    // int n;cin >> n ;
    int n = 5;

    // hinh 1
    for(int i = 1;i<=n;i++){//in ra dong
        for(int j = 1;j <= n;j++){//in ra dong
            cout << "*";//in ra dau sao
        }
        cout << endl;
    }
    cout << endl;
    // hinh 2
    for(int i = 1;i<=n;i++){
        for(int j = 1;j<=n;j++){
            if(i == 1 || i == n || j == 1 || j == n)cout << "*";
            else cout << " ";           
        }
        cout << endl;
    }
    cout << endl;
    // hinh 3
    for(int i = 1;i<=n;i++){
        for(int j = 1;j<=n;j++){
            if(i == 1 || i == n || j == 1 || j == n)cout << "*";
            else cout << "#";           
        }
        cout << endl;
    }
    cout << endl;
    // hinh 4
    for(int i = 1;i<=n;i++){
        for(int j = 1;j<=n;j++){
            if(i == 1 || i == n || j == 1 || j == n)cout << i << " ";
            else cout << "  ";           
        }
        cout << endl;
    }

}