#include <iostream>

using namespace std;

int main(){
	long long n; cin >> n;
	cout << n + n * (n - 1) / 2<< endl;
	cout << n * (n+1) * (2*n + 1) / 6 << endl;
	cout << n/3 << endl;
	long long u1 = 3,d = 3,n = n /3;
	cout << n * u1 + n*(n-1)*d /2;

}