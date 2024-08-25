#include <bits/stdc++.h>
using namespace std;

int main(){
	long long a,b,c; cin >> a >> b >> c;
	// long long s = a*(b+c)+b*(a+c);
	long long s = (long long)a*(b+c)+(long long)b*(a+c);
	cout << s << endl;
}