#include <bits/stdc++.h>
using namespace std;
#define ll long long


int main(){
	int n;cin >> n;
	int a[n];
	ll sum = 0;
	for(int i = 0;i<n;i++){
		cin >> a[i];
	}
	for(int i = 0;i<n;i++){
		if(a[i]%2 == 0){
			sum+=a[i];
		}
	}
	cout << sum;
}