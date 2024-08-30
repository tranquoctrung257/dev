#include <bits/stdc++.h>
using namespace std;
int main(){
    long long n; cin >> n;
    // long long n = 9888811237 ;
    long long temp = n;
    while (temp>=10)
    {

       temp/=10;
    }
    long long temp1 = n;
    long long t;
    while (temp1!=0)
    {
        long long r = temp1%10;
        if(r>temp) t = r;
        else t = temp;
        temp1/=10;
    }
    if(t == temp){
        cout << "YES";
    } 
    else cout << "NO";
    
}22