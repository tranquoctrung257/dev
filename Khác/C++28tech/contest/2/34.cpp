#include<bits/stdc++.h>
using namespace std;

int main(){
    long long c1,c2,c3,c4,c5;cin >> c1 >> c2 >> c3 >> c4 >> c5;
    long long tong = c1 + c2 + c3 + c4 + c5;
    if (tong % 5 == 0){
        long long b = tong / 5;
        if(b!=0)cout << b;
        else cout << -1;
    }
    else cout << -1;

}