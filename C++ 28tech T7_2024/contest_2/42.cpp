#include <iostream>
using namespace std;

int main(){
	double w,h;cin >> w >> h;
	double bmi = w /pow(h/100,2);
	if(bmi >= 40) cout << "Extreme obesity";
	else if(bmi >= 35) cout << "Obesity 2";
	else if(bmi >= 30) cout << "Obesity 1";
	else if(bmi >= 25) cout << "Over weight";
	else if(bmi >= 18.5) cout << "Normal";
	else if(bmi < 18.5 ) cout << "Under weight";
}