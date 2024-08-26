#include <bits/stdc++.h>
using namespace std;

int main(){
	long long a,b; cin >> a >> b;
	long long tong = a + b;
	long long hieu = a - b;
	long long tich = a * b;
	cout << tong << endl;
	cout << hieu << endl;
	cout << tich << endl;
	if(a == 0 || b == 0) cout << "INVALID";
	else{
		double thuong = 1.0*a / b;
		cout<< fixed << setprecision(2) << thuong << endl;
	}
}