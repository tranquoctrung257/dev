#include <iostream>
#include <iomanip>

using namespace std;

int main(){
	int c;cin >> c;
	double f = (c* (9.0 /5)) + 32;
	cout << fixed << setprecision(2) << f << endl; 
}