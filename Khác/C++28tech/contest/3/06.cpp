#include <bits/stdc++.h>
using namespace std;

int main(){
    long long n;cin >> n;
    long long t = 0;
    int z = n % 10;
    n/=10;
    while (n>0){
        int r = n % 10;
        long long chenhlech = abs(r-z);
        t += chenhlech;
        z = r;
        n/=10;
    }
    cout << t;
    
}