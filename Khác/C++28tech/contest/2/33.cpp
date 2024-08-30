#include<bits/stdc++.h>
using namespace std;

int main(){
    long long a,b,c,n,tmp; cin >> a >> b >> c >> n;
    if((a + b + c + n) % 3 ==0){
        tmp = (n + a + b + c) /3;
        if(tmp >= a && tmp >= b && tmp >= c)
        cout << "YES";
        else cout << "NO";
    }
    else cout << "NO";

}