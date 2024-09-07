// tổng bội 3 
//nhập vào n không quá 10^6, tính tổng các số nguyên dương không vượt quá n và chia hết cho 3

#include <iostream>
using namespace std;

int main(){
	int n;cin >> n;
	long long sum = 0;
	for(int i = 1;i<=n;i++){
		if(i%3==0){
			sum +=i;
		}
	}
	cout << sum << endl;
}