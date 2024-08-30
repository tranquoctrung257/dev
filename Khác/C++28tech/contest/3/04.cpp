#include <bits/stdc++.h>
using namespace std;

int main(){
    int n;cin >> n;
    // int n = 37;
    int i = 3;
    while (i <= n){
        cout << i << " " ;
        i+=3;
    }
    cout << endl;
    for(int i = 0;i<n;i++){
        if(i%3==0 && i%5==0){
            cout << i << " ";
        }
    }
    cout << endl;
    
    for(int i = n;;i++){ // lap vinh vien den khi nao tim dc so lon hon n ma chia het cho 7 thi dung
        if(i%7 == 0 ){
            cout << i << " ";
            break;
        }}
    cout << endl;
    for(int i = n;i>=0;i--){
        if(i%9==0){
            cout << i << endl;
            break;
        }
    }
    for(int i = 1;i<=n;i++){
        cout << 2*i-1 << " ";
    }
}