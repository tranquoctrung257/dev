#include <iostream>

using namespace std;

int main(){
	long long a,b,c,d; cin >> a >> b >> c >> d;
	if(b % a == 0){
		int r = b / a;
		if(b * r == c && c * r == d){
			cout << "YES" << endl;
		}
		else cout << "NO" << endl;
	}
	else cout << "NO" << endl;
}