#include <bits/stdc++.h>

using namespace std;

int main(){
	long long n,a,b; cin >> n >> a >> b ;
	if(2*a > b) cout << n/2 * b + (n%2)*a << endl;
	else cout << n*a << endl;

}