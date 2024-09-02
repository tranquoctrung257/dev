// Bài 9.kiểm tra năm nhuận
//năm nhuận là năm chia hết cho 400 hoặc (chia hết cho 4 và không chia hết cho 100). nhập vào n là một năm và kiểm tra xem N có ải là năm nhuận hay không?

//Đầu vào 
//số nguyên dương N

// giới hạn
//1<=N<=5000

//đầu vào 
//In ra YES nếu n là năm nhuận, ngược lại in ra NO
//Ví dụ:
//input1
//2020

//output1
//YES
#include <iostream>
using namespace std;
int main(){
	int n; cin >> n;
	if((n % 400 == 0) || ( n % 4 == 0  && n % 100 != 0)){
		cout << "YES" << endl;
	}
	else cout << "NO" << endl;
	
	
}