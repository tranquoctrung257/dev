#include<bits/stdc++.h>
using namespace std;

int main(){
    long long n;
    cin >> n;
    long long sum = 0;
    for(int i = 1;i<=n;i++){
        if(i%3==0){
            sum += pow(i,2);
        }
        
    }
    cout << sum << endl;
    // hoac
    // long long kq = 1;
    // for(int i = 3;i<=n;i+=3){
    //     kq+=i;
    // }
    
    // cong thuc tinh nhanh
    int m = n / 3;
    long long kq = 3ll * m * (m+1) / 2;  
    cout << kq;
    
}