#include <bits/stdc++.h>
using namespace std;

int main(){
    int a,b,c; cin >> a >> b >> c;
    long long min_abc = min({a,b,c});
    long long max_abc = max({a,b,c});
    if(a == max_abc && b == min_abc)cout << b << " " << c << " " << a ;
    else if(a == min_abc && b == max_abc) cout << a << " " << c << " " << b ;
    else if(b == min_abc && a == max_abc) cout << b << " " << c << " " << a ;
    else if(c == min_abc && a == max_abc) cout << c << " " << b << " " << a ;
    else if(a == min_abc && c == max_abc) cout << a << " " << b << " " << c ;
    else if(c == min_abc && b == max_abc) cout << c << " " << a << " " << b ;
    else if(b == min_abc && c == max_abc) cout << b << " " << a << " " << c ;
}