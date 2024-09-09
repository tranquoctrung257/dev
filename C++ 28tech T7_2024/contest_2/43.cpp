#include <iostream>
#include <iomanip>
using namespace std;

int main(){
	int a,b; char x;cin >> a >> b >> x;
	switch(x){
		case '+':
			cout << a << " " << x << " " << b << " = " << a + b << endl;
			break; 
		case '-':
			cout << a << " " << x << " " << b << " = " << a - b << endl;
			break; 
		case '*':
			cout << a << " " << x << " " << b << " = " << a * b << endl;
			break;
		case '/':
			cout << a << " " << x << " " << b << " = " << fixed <<setprecision(2)<< (1.0*a) / b << endl;
			break; 
		case '%':
			cout << a << " " << x << " " << b << " = " << a % b << endl;
			break; 
	}
}