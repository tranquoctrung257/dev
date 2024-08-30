#include<bits/stdc++.h>
using namespace std;

int main(){
    long long n,dem=0;
    cin >> n;
    while (n!=0){
        int r = n%10;
        if(r == 2 || r == 3 || r ==5 || r == 7){
            dem++;
        }
        n/=10;
    }
    cout << dem << endl;
    
}