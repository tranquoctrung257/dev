#include<bits/stdc++.h>
using namespace std;

int main(){
    long long a1,a2,a3,b1,b2,b3,n; cin >> a1 >> a2 >> a3 >> b1 >> b2 >> b3 >> n;
    long long tong1 = a1 + a2 + a3;
    long long tong2 = b1 + b2 + b3;
    long long cach1 = 0 , cach2 = 0;
    if(tong1%5==0 ) cach1 = tong1/5;
    else cach1 = tong1/5+1;
    if(tong2%10==0 ) cach2 = tong2/10;
    else cach2 = tong2/10+1;

    if((cach1+cach2) <=n ) cout<< "YES";
    else cout << "NO"; 
}