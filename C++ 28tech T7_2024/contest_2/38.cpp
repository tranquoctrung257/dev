#include <iostream>

using namespace std;

int main(){
	int n; cin >> n;
	int ans = 0,res = 0;
	for(int i = 1; i <= n; i++){
		char c;cin >> c;
		if(c == 'C') ++ans;
		if(c == '+') ++res;
	}
	if(ans >= 1 && res >= 2) cout << "YES" << endl;
	else cout << "NO" << endl;
}