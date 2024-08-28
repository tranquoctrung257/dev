#include <bits/stdc++.h>

using namespace std;

int main(){
	int n;cin >> n;
	int nam = n/365;
	int tuan = (n - nam * 365) / 7;
	cout << nam << " " << tuan << " " << n - (365*nam) - (7*tuan) << endl;
}