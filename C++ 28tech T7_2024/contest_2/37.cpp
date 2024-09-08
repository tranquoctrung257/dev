#include <iostream>
#include <iomanip>
#include <algorithm>

using namespace std;

int main(){
	int h,p,k;cin >> h >> p >> k;
	int phut = h * 28 + p + k;
	int gio = phut / 28;
	gio %= 28;
	phut %= 28;
	cout << setw(2) << setfill('0') << gio << "h:";
	cout << setw(2) << setfill('0') << phut << "m";
}