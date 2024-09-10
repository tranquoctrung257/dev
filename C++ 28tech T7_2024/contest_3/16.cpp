#include <bits/stdc++.h>
using namespace std;
 
using ll = long long;
using db = double;
int main(){
	ll n;cin >> n;
	int dem = 0;
	if(n == 0){
		cout << 1 << endl;
	}
	else{
		while(n != 0){
			dem++;
			n/=10;
		}
		cout << dem << endl;		
	}

}