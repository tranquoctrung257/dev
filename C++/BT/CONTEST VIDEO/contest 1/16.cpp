#include <bits/stdc++.h>

using namespace std;

int main(){
	char c;cin >> c;
	if(c=='z' || c=='Z') cout << 'a' << endl;
	else if(c>='a'&&c<='z')cout << char(c+1)<< endl;
	else if(c>='A'&&c<='Z') cout << char(c+33) << endl;
}