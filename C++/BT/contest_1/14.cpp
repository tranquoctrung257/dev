#include <bits/stdc++.h>
using namespace std;

int main(){
	long long a,b;cin >> a >> b;
	// c1
	// if(a%b==0)cout << a << endl;
	// else cout << (a / b + 1) * b;

	// c2
	long long c = (a+b-1)/b * b;
	cout << c; 
}