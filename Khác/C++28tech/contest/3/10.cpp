#include<bits/stdc++.h>
using namespace std;

int main(){
    long long n;
    cin >> n;
    bool check = false;
    for(int i = 1;i<=n;i++){
        int tmp;cin >> tmp;
        if(tmp == 2022){
            check = true;
        }
    }
    if(check){
        cout << "YES";
    }
    else cout << "NO";

}