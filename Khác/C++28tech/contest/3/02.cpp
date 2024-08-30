#include<bits/stdc++.h>

using namespace std;

int main(){
    long long n;cin >> n;
    for(int i = 0;i<=n;i+=3){
        cout << i << " ";
    }
    cout << endl;
    for(int i = 1;i<=n;i*=2){
        cout << i << " ";
    }
    cout << endl;
    for(int i = n;i>=1;i--){
        if (i%17){
            cout << ((i+16)/17)*17;
            cout << endl;
            break;}
    }
    for(int i = n;i>=1;i--){
        if (i%7){
            cout << ((i/7)*7) << endl;
            break;}
    }
    long long num = 1 ;
    long long step = 1;
    while(num<=n){
        cout << num << " ";
        num += step;
        step +=1;
    }
}