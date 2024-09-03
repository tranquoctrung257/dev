// bài 1 tính toán giá trị biểu thức.

//cho biểu thức A(x) = X^3 + 3X^2 + x + 1. với giá trị của x được nhập từ bàn phím,tính và in ra giá trị của biểu thức trên 

//Đầu Vào:
//Số nguyên x

//Rằng Buộc
//-10^5 <= n <= 10^5

// Đầu ra 
//in ra kết quả của biểu thức

//ví dụ 
//input1
//2
//output1
//23
#include <iostream> 
using namespace std;

int main(){
	int n;cin >> n;
	
	long long result = (long long)n * n * n + (long long) 3 * n * n + n + 1;
	cout << result << endl;
	
}