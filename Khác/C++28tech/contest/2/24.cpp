#include<bits/stdc++.h>
using namespace std;

int main(){
    long long d1,d2,d3;cin >> d1 >> d2 >> d3 ;
    long long c1 = d1 + d2 + d3; 
    long long c2 = 2*(d1+d2);
    long long c3 = 2*(d1+d3);
    long long c4 = 2*(d2+d3);
    cout << min({c1,c2,c3,c4});
}