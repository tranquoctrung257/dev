#include<bits/stdc++.h>
using namespace std;
int main(){
    long long n ;cin >> n;
    int even_count = 0,odd_count = 0;
    while (n!=0){
        int r = abs(n%10);
        if(r%2==0)even_count ++;
        else odd_count ++; 
        n/=10;
    }
    if(even_count >odd_count )
    {
        cout << "28tech";
    }
    else {
        cout << "29tech";
    }

}