#include <iostream>

using namespace std;

int main(){
	int n; cin >> n;
	int alpha = 0,digit = 0;
	for(int i = 0; i < n;i++){
		char kitu;cin >> kitu;
		if((kitu >= 'A' && kitu <= 'Z' )|| (kitu >= 'a'&& kitu <= 'z')) ++ alpha;
		else if(kitu >= '0' && kitu <= '9'){
			digit += (kitu-'0');
		}
	}
	cout << alpha << endl << digit << endl;
}