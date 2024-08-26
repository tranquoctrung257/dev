#include <bits/stdc++.h>
using namespace std;

int main(){
	char c;cin >> c;
	if(c == 'z' || c == 'Z'){
		cout << 'a' << endl;
	}
	else if(c>=65 && c<=90) 
		cout << char(c+33) << endl;
	else if(c>= 97 && c<= 122){
		cout << char(c+1);
	}	
	else cout << "INVALID" << endl;
}