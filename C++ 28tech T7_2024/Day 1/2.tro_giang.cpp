#include <iostream>
// #include <math.h> // thư viện này nằm trong ngôn ngữ c
// #include <cmath> // thư viện này có nhiều ưu điểm hơn hàm math.h
using namespace std;

int main(){
	int x,y,z,t;cin >> x >> y >> z >> t;
	cout << x + y + z + t << endl; // nếu 4 số đều là 10^9 sẽ tràn nên phải ép kiểu
	cout << long long(x + y + z + t); // như thế này cũng không được vì nó cộng trước rồi nhưng sẽ lấy bộ nhớ của kiểu dữ liệu lớn nhất trong 4 số cộng lại rồi với ép kiểu long long nên đây vẫn sai
	cout << (long long)x + y + z + t; // như thế này với là đáp án chính xác	
	cout << x + y + z + (long long)t; // vẫn bị tràn vì trong c++ sẽ chạy từ trên xuống dưới từ trái qua phải nên đầu x+y mà nếu nó là 10^9 thì sẽ bị tràn rồi | tiếp theo sẽ lấy kq của (x+y) + với z và cứ như thế cộng đến cuối
	// vậy nên phải ép kiểu ở đầu 
}

// mặc định pow trả về số thực.
// sqrt trả về số thực
// cbrt trả về số thực
// ceil trả về số thực 
// floor trả về số thực
// round trả về số thực

// khi nào sử dụng số thực thì dùng double vì double có độ chính xác cao hơn thằng float
// n % 10^k ==> k chữ số cuối cùng 

// dsa viết tắt của data structures and algorithms | cấu trúc dữ liệu và giải thuật

// hàm max và hàm min của thư viện cmath chỉ sử dụng được 2 số thôi
// nhưng hàm max và min trong thư viện algorithm sẽ sử dụng được nhiều số 
// khi tìm max min của 3 số trở lên thì phải có ngoặc nhọn
// cout << max({1,423,44});
// 2 số thì ko cần dấu ngoặc nhọn

// Cú pháp để in ra 1 số nguyên n với độ rộng K, điền đầy ký tự C vào đầu nếu không đủ K chữ số
// setw(K) << setfill(C) phải thêm thư viện iomanip