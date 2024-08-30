#include<bits/stdc++.h>
using namespace std;

int main(){
    long long n;
    cin >> n;
    long long sum=0;
    for(int i = 1;i<=sqrt(n)+1;i++){
        if(n%i==0){
            sum+=1;
            if(i!=n/i){
                sum+=1;
            }
        }
    }
    cout << sum << endl;
    for(int i = 1;i<=n;i++){
        if(n%i==0){
            cout << i << " ";            
            }
        }
    }