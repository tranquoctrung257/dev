#include<bits/stdc++.h>
using namespace std;

int main(){
    long long n;
    cin >> n;
    long long sum = 0;
    for(int i = 1;i<=n;i++){
        sum += pow(i,2);
    }
    cout << sum << endl;
}