#include <bits/stdc++.h>
using namespace std;

int main(){
    long long n;cin >> n;
    long long h = n / 3600;
    long long m = (n % 3600) / 60;
    long long s = (n % 3600 % 60) ;
    cout << h << "h" << " : " << m << "m" << " : " << s << "s";

}