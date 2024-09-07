#include <iostream>

using namespace std;

int main(){
	long long n,u,d;cin >> n >> u >> d;
	cout << n * u + (n * (n-1) * d ) / 2 << endl;
}