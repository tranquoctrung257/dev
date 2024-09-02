//Bài 10: Tam giác hợp lệ.
// cho 3 cạnh a,b,c là độ dài 3 cạnh của tam giác, kiểm tra a,b,c có thể tạo thành một tam giác hợp lệ hay không?
//đầu vào 
//1 dòng chứa 2 số a,b,c

//giới hạn
//-10^6<=a,b,c<=10^6

//Đầu ra 
//in ra YES nếu a,b,c là 3 cạnh của 1 tam giác hợp lệ, ngược lại in ra NO

//ví dụ
//input1
//3 4 5

//output1
//YES
#include <iostream>

using namespace std;

int main(){
	long long a,b,c;cin >> a >> b >> c;
	if(a > 0 && b > 0 && c > 0 && a+b > c && b+c  > a && a + c > b){
		cout << "YES" << endl;
	}
	else cout << "NO" << endl;
}