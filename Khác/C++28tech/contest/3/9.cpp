#include<bits/stdc++.h>
using namespace std;

int main(){
    long long n;
    cin >> n;
    long long sum=1;
    for(int i = 1;i<=n;i++){
        if(n%i==0){
            sum*=i;
        }}
    cout << sum << endl;
    }