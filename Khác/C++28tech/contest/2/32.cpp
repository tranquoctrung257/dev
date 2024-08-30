#include<bits/stdc++.h>
using namespace std;

int main(){
    long long k2,k3,k5,k6;cin >> k2 >> k3  >> k5 >> k6;
    // lay toi da so luong so 256
    long long k256 = min({k2,k5,k6});
    // lay min(thua 2 so luong 3)
    long long k32 = min({k3,k2-k256});
    long long sum = k256*256 + k32*32;
    cout << sum << endl;
}