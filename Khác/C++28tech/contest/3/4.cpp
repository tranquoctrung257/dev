#include<bits/stdc++.h>
using namespace std;

int main(){
    long long n;
    cin >> n;
    double sum = 0.0;
    for(int i = 1;i<=n;i++){
        sum +=1.0/i;
        }
        
    cout << fixed <<setprecision(3)<< sum << endl;
    }