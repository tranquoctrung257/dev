#include <bits/stdc++.h>

using namespace std;

int main(){
	int n; cin >> n;
	if( n%100==0 || (n % 4 == 0 && n % 100 != 0)){
		cout << "YES" << endl;
	}
	else cout << "NO" << endl;
}