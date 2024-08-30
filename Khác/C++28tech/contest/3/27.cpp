#include <bits/stdc++.h>
using namespace std;
#define ll long long


int main(){
	ll n ;cin >> n;
	while(n>=10){
		ll t = 0;
		while(n>0){
			t += n%10;
			n/=10;
		}
		n = t;
	}
	cout << n;
}