#include <iostream>

using namespace std;

int main(){
	long long s;cin >> s;
	long long gio = s / 3600;
	s%= 3600;
	long long phut = s/60;
	s%=60;
	cout << gio << "h" << " : " << phut << "m" << " : " << s << "s" << endl;
}