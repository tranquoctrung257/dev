#include <bits/stdc++.h>

using namespace std;

int main(){
	long long a,b,c ; cin >> a >> b >> c;
	if(a > 0 && b > 0 && c > 0 && a+b > c && a+c > b && b +c > a){
		cout << "YES" << endl;
	}
	else cout << "NO" << endl;
}