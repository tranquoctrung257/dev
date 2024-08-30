#include <bits/stdc++.h>
using namespace std;
int main(){
    double a;cin >> a;
    if(abs(a-(int)(a)) <= 0.5) cout << (int) a;
    else cout << (int)(a)+1;
    // hoac 
    // cout << round(a);

}