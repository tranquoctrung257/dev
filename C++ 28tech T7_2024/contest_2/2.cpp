#include <iostream>

using namespace std;

int main() {
	int a,b,c;cin >> a >> b >> c;
	long long s = (long long) a * ( b + c ) + (long long) b * ( a + c );
	cout << s << endl;
	return 0;
}