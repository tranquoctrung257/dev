#include <iostream>

using namespace std;

int main(){
	int a1,a2,a3,b1,b2,b3;cin >> a1 >> a2 >> a3 >> b1 >> b2 >> b3;
	int n; cin >> n;

	int tc = a1+a2+a3;
	int kecup = tc / 5;
	if(tc % 5 != 0) kecup +=1;

	int thc = b1 + b2 +b3;
	int kehc = thc/10;
	if(thc % 10 != 0) kehc +=1;

	if(kecup+kehc <= n)cout << "YES" << endl;
	else cout << "NO" << endl;
}