#include<bits/stdc++.h>
using namespace std;

int main(){
    long long n,dem=0;
    cin >> n;
    if(n==0){
        cout << 1 << endl;return 0;//ket thuc chuong trinh luon
    }
    // while (n!=0){
    //     n/=10;
    //     dem++;
    // }
    // cout << dem << endl;
    // hoac
    while (n){
        n/=10;
        dem++;
    }
    cout << dem << endl;
}

