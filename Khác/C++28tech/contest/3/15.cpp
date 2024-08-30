#include<bits/stdc++.h>
using namespace std;

int main(){
    long long s,gt=1;
    cin >> s;
    for(int i = 1;i<=s;i++){
        gt *= i;
       
    }
    cout << gt << endl;    
}
