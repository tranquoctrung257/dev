#include <bits/stdc++.h>
using namespace std;
 
using ll = long long;
using db = double;

// vong l while
//while([điều kiện lặp true]){
//	// các câu lệnh của vòng lặp
//}
//int main(){ 
//	int x = 1;
//	while(x<4){
//		cout << x << endl;
//		x++;
//	}
//	cout << x << endl;
//	   
//}

//n = 5442324323423
//1.đếm n có bao nhiêu chữ số ?
int main(){
	ll n = 23423423;
	int dem = 0;
	while(n!=0){ // hoặc while(n) ; while(n>0)
		dem++;
		n/=10;
	}
	cout << dem << endl;
}
