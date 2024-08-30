#include <bits/stdc++.h>
using namespace std;

int main(){
    long long a,b;
    cin >> a >> b;
    cout << a + b << endl;
    cout << a - b << endl;
    cout << a * b << endl;
    if(a==0 or b == 0)cout << "INVALID" <<endl;
    else cout << fixed << setprecision(4) << ((1.0*a)/b) << endl;
}