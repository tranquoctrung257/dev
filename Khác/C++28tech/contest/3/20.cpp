#include <bits/stdc++.h>
using namespace std;
#define ll long long


int main(){
	int n ;cin >> n;
	if(n==1){cout << -1;}
	else if(n%2==0){
		cout << n/2 << endl;
		for(int i = 1;i<=n/2;i++){
			cout << 2 << " ";
		}
	}
	else {cout << n/2 << endl;
	for(int i = 1;i<=n/2-1;i++){
		cout << 2 << " ";
	}
	cout << 3;
	}

}