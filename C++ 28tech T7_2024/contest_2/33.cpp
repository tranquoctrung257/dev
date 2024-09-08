#include <iostream>

using namespace std;

int main(){
	int a,b,c,n;cin >> a >> b >> c >> n;
	int s = a + b + c + n ;

	if(s % 3 == 0){
		int m = s / 3;
		if(m >= a && m >= b && m >= c) cout << "YES" << endl;
		else cout << "NO" << endl;
	}
	else cout << "NO" << endl;
}