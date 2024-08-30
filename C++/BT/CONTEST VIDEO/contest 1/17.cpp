#include <bits/stdc++.h>

using namespace std;

int main(){
	float a,b,c,d;cin >> a >> b >> c >> d;
	float dtb = (a + b + (c*2) + (d*3)) / 7;
	if(dtb <=10 && dtb >=8) cout << "GIOI" << endl;
	else if(dtb >= 6.5) cout << "KHA" << endl;
	else if(dtb >= 5) cout << "TRUNG BINH" << endl;
	else cout << "YEU" << endl;
}