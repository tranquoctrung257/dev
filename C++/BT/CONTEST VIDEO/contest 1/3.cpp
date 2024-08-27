#include <bits/stdc++.h>
using namespace std;

int main(){
	long long a,b; cin >> a >> b;
	long long tong = a+b;
	cout << tong << endl;

	long long hieu = a-b;
	cout << hieu << endl;
	
	long long tich = a*b;
	cout << tich << endl;

	if(a == 0 || b == 0){
		cout << "INVALID" << endl;
	}
	else cout << fixed << setprecision(4)<< 1.0*a /b << endl;
}