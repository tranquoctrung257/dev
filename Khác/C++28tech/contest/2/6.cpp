#include <bits/stdc++.h>

using namespace std;

int main(){
    int n;cin >> n;
    if(n % 2 == 0) cout << "YES\n";
    else cout << "NO\n";

    if(n % 3 == 0 && n % 5 == 0) cout << "YES\n";
    else cout << "NO\n";

    if(n % 3 == 0 && n % 7 != 0) cout << "YES\n";
    else cout << "NO\n";     

    if(n % 3 == 0 || n % 7 == 0) cout << "YES\n";
    else cout << "NO\n";   

    if(n > 30 && n < 50 ) cout << "YES\n";
    else cout << "NO\n"; 

    if(n >= 30 && (n % 2 == 0 or n % 3 == 0 or n % 5 == 0) ) cout << "YES\n";
    else cout << "NO\n";

    if (n >= 10 && n <= 99 && (n % 10 == 2 || n % 10 == 3 || n % 10 == 5 || n % 10 == 7)) cout << "YES\n";
    else cout << "NO\n";

    if ( n <= 100 && n % 23 == 0)cout << "YES\n";
    else cout << "NO\n";

    if(n < 10 || n > 20) cout << "YES\n";
    else cout << "NO\n";

    if(n % 10 % 3 == 0)cout << "YES\n";
    else cout << "NO\n";
}