//bài 2 tổng bình phương
//tổng s(n) = 1^2 + 2^2 + 3^2 + ... + n^2
//giới hạn 1<=n<=10^5

#include <iostream>
#include <cmath>

using namespace std;

int main(){
	int n; cin >> n;
	long long sum = 1;
	for(int i = 1;i<=n;i++){
		sum += int(pow(i,2));
//		hoặc
//		sum += 1ll * i * i;
	}
	cout << sum << endl;
}