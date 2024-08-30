#include <bits/stdc++.h>
using namespace std;

int main(){
    int x,y,z,t;
    cin >> x >> y >> z >>t;
    cout << y << "," << z << "," << x << "," << t << endl;
    long long tong = (long long)x+y+z+t ;
    cout << tong << endl;
    long long d3 = x-y+ (long long)z*t;
    cout << d3 << endl;
}