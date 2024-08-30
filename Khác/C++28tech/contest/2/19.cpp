#include <bits/stdc++.h>
using namespace std;

int main(){
    long long m,n;
    cin >> m >> n;
    if(n%2 == 0) cout << n / 2 * m;
    // ap dung trong python
    else cout << (n-1)/2 * m + m / 2 ;

}

// hoac
#include <bits/stdc++.h>
using namespace std;

int main(){
    long long n,m;cin >> n >> m;
    if(n%2 == 0){
        cout << n / 2 * m;
    }
    else {
        cout << (n / 2 * m + (m/2));
    }

}