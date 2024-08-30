#include <bits/stdc++.h>

using namespace std;

int main(){
    long long n; cin >> n;
    int a,b,c,d,e;
    e = n /100;
    d = (n%100) / 20;
    c = ((n%100)%20) /10;
    b = (((n%100)%20)%10)/5;
    a = ((((n%100)%20)%10)%5)/1;

    cout << a+b+c+d+e;
}

// hoac
int main(){
    int n,a,b,c,d,e;
    cin >> n;
    e = n/100;
    d = (n-(e*100))/20;
    c = (n-(e*100+d*20))/10;
    b = (n-(e*100+d*20+c*10))/5;
    a = n -(e*100+d*20+c*10+b*5);
    cout << a+b+c+d+e;

}