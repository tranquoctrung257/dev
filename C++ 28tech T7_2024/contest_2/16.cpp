#include <iostream>

using namespace std;

int main(){
	char c;cin >> c;
	if(c == 'z' || c == 'Z'){
		cout << 'a' << endl;
	}

	else if(c >= 65 && c <= 90){
		cout << char(c+33) << endl;
	}
	else {
		cout << char(c+1) << endl;
	}
}