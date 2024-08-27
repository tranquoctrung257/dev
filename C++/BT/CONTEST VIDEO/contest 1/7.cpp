#include <bits/stdc++.h>

using namespace std;

int main(){
	long long a,b; cin >> a >> b;
	cout << (a / b) * b;
	if(a%b==0){
		cout << a << endl;
	}
	else{
		cout << (a / b + 1) * b;
	}
	// cout << (a+b-1)/b *b;
}