#include <bits/stdc++.h>
using namespace std;

int main(){
    int a,b;
    cin >> a >> b;
    cout << a / b * b << endl;

    if(a%b == 0) cout<< a;
    else cout << (a/b +1)*b;

    // hoac
    // cout << (a+b-1)/b *b;
}