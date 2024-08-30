#include <bits/stdc++.h>
using namespace std;

int main(){
    long long n;cin>> n;
    int m = 0;
    while (n!=0){
        int r = n%10;
        if(r > m){m=r;}
        n/=10;
    }
    cout << m ;
}