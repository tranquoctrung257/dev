#include<bits/stdc++.h>
using namespace std;

int main(){
    long long n;cin >> n;
    // long long n = 28282828;
    long long d;
    long long tmp = n;
    while (tmp!=0){
        d = tmp;
        tmp/=10;
    }
    cout << d << " " << n%10;
}