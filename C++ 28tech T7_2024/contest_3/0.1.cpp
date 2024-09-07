// bài 1 tổng tự nhiên liên tiếp

//tính tổng s(n) = 1 + 2 + 3 + ... + n
//giới hạn 1<=n<=10^6
#include <iostream>
using namespace std;
int main(){
	int n;cin >> n;
	long long sum = 0;
	for(int i = 1;i<=n;i++){
		sum+=i;
	}
	cout << sum << endl;
}