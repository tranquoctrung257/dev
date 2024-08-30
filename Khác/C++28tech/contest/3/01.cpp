#include <bits/stdc++.h>
using namespace std;

int main(){
    int n; cin >> n;
    for(int i = 0;i<n;i++){
        cout <<"Hello 28tech" << endl;
    }
    for(int i = 1;i<=n;i++){
        cout << i << " ";
    }
    cout << endl;
    for(int i = 0;i<n;i++){
        cout << i << " ";
    }
    int tmp = n;
    cout << endl;
    for(int i = 1;tmp>=i;tmp--){
        cout << tmp << " ";
    }
    cout << endl;
    int temp1 = n-1;
    for(int i = 0;temp1>=i;temp1--){
        cout << temp1 << " ";
    }
    cout << endl;
}