#include <iostream>

using namespace std;

int main(){
    long long n,s;cin >> n >> s;
    if(n%s==0){
        cout << s/n << endl;
    }
    else{
        cout << s/n+1 << endl;
    }
}