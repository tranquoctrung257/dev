#include<bits/stdc++.h>
using namespace std;

int main(){
    long long n,tong=0;
    cin >> n;
    while (n!=0){
        int r = n%10;
        tong +=r;
        n/=10;
    }
    cout << tong << endl;
    
}