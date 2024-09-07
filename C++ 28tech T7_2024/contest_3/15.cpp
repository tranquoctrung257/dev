//bài 15 giai thừa
//n không âm không vượt quá 15, tính và in ra n!

#include <iostream>
using namespace std;

int main(){
	long long n;cin >> n;
	long long giaithua = 1;
	for(int i = 1;i<=n;i++){
		giaithua *=i;
	}
	cout << giaithua << endl;
}