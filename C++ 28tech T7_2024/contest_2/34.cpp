#include <iostream>

using namespace std;

int main(){
	int c1,c2,c3,c4,c5; cin >> c1 >> c2 >> c3 >> c4 >> c5;
	int s = c1+c2+c3+c4+c5;

	if(s%5 ==0 && s != 0) cout << s/5 << endl;
	else cout << -1 << endl;
}