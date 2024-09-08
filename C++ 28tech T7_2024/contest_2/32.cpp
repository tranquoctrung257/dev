#include <iostream>
#include <algorithm>
using namespace std;

int main(){
	int k2,k3,k5,k6;cin >> k2 >> k3 >> k5 >> k6;
	int sl256 = min({k2,k5,k6});
	k2-=sl256;
	int sl32 = min({k2,k3});
	
	cout << 1ll * sl256 * 256 + sl32 * 32 << endl;
}