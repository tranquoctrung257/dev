#include <iostream>
#include <iomanip>
using namespace std;

int main(){
	const double PI = 3.14;
	int r; cin >> r;
	double chu_vi{2*PI*r};
	double dien_tich{PI * r * r};
	cout << fixed << setprecision(4) << chu_vi << " " << fixed << setprecision(4) << dien_tich << endl;
}