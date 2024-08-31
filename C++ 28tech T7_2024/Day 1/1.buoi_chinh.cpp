#include <iostream> // khai báo thư viện cần thiết 
#include <iomanip> // thư viện sử dụng fixed << setprecision
#include <math.h> // thư viện toán học
// hoặc #include <cmath> 
using namespace std; // thêm namespace

// int main(){ // hàm main: là nơi bắt đầu thực thi của chương trình
// 	cout << "Toi Hoc Lap trinh!";
// 	return 0;
// }

// kiểu dữ liệu trong c++

// số nguyên 
// int: 4byte:32bit -2.10^9 ==> 2.10^9 (10 chữ số)
// long long: 8byte:64bit -9.10^18 ==> 9.10^18 (19 chữ số)

// số thực
// float: 4byte:32bit | 7 chữ số đàng sau dấu phẩy
// long long: 8byte:64bit | 15 chữ số đằng sau đấu phẩy

// bool | đúng hoặc sai
// true 1
// false 0

// kiểu kí tự 
// char 1byte vd 'a','b','1','$',...


// biến: biến được sử dụng để lưu các giá trị trong quá trình tính toán của chương trình. tùy theo kiểu dữ liệu của biến,mỗi ô trong bộ nhớ sẽ được cấp pahts để lưu trữ giá trị của biến này.
// cú pháp:
// (kiểu dữ liệu)(tên biến);

// int main(){
// 	// ví  dụ 
// 	int a;
// 	long long b;
// 	float c;
// 	// hoặc khai báo nhiều biến trên 1 dòng.
// 	double x,y,z;
// 	return 0;
// }

// - quy tắc đặt biến
// + không đặt tên biến bắt đầu bằng chữ số
// + tên biến không đươc chứa dấu cách và các kí tự đặc biệt
// + tên biến không được trùng với từ khóa trong c++ 
// + tên biến trong c++ phân biệt chữ hoa thường
// + có thể dùng dấu _
// + không được đặt 2 tên biến có cùng tên trong cùng một phạm vi

// chú thích trong c++
// chú thích 1 dòng
/* 
chú thích nhiều dòng
*/

// in nội dung ra nàm hình bằng câu lệnh cout 
// int main(){
// 	// \n và endl là kí tự xuống dòng
// 	cout << "Toi Hoc Lap Trinh" << endl;
// 	cout << "abc" << " " << "xyz" << endl;
// 	int a = 100,b = 200, c = 300;
// 	cout << a << " " << b << " " << c << endl;
// 	bool x = true;
// 	cout << x << endl; //1
// 	char kitu = '$';
// 	cout << kitu << endl;

// 	// để hiện thị các số các đàng sau dấu phẩy
// 	double n = 412.42839462387423;
// 	cout << fixed << setprecision(5) << n << endl; // lấy 5 số đằng sau dấu phẩy
// 	return 0; 
// }

// nhập dữ liệu từ bàn phím 
// int main(){
// 	int a,b,c;
// 	// cin >> a;
// 	cin >> a >> b >> c;
// 	cout << a << " " << b << " " << c << endl;
// }

// một số lỗi trên trang chấm bài
// wa:đáp án sai
// ce:lỗi biên dịch
// ac:code đúng

// toán tử gán.
// int main(){
// 	int n = 100; // gán 100 cho biến n
// }

// trong c++ số nguyên chia cho nhau sẽ ra số nguyên
// một trong 2 số bị chia là số thực sẽ ra kq là số thực

// toán tử toán học
// + công 
// - trừ 
// * nhân 
// / chia trả về nguyên | nếu 1 trong 2 số là số thực sẽ trả về số thực
// % chia lấy phần dư
// 1.0 * 10 = 10.00000 / 3 = 3.333333
// int * int = int 
// long long * int = long long 
// nếu biểu thức có số thực tham gia ==> kq sẽ là số thực
// nếu biểu thức có toàn số nguyên ==< kq bao giờ xũng là số nguyên

// int main(){
// 	int a = 1000000,b = 3000000;
// 	long long tich = (long long)a * b << endl;
// 	cout << tich << endl;
// 	return 0; 
// }

// ép kiểu
// (kiểu)biến
// int main(){
// 	int a = 5345.534534;
// 	cout << (long long)a << endl; 
// 	int b = 43242;
// 	cout << 1.0 * a / b;

// }

// hàm toán học
// abs: trị tuyệt đối
// max: số lớn nhất trong 2 số
// min: số bé nhất trong 2 số 

// sqrt: tính căn bậc 2
// pow(a,b): tính a^b
// cbrt: tính căn bậc 3
// floor: làm tròn lên số nguyên gần nhất
// round: làm tròn xuống số nguyên gần nhất
// ceil: làm tròn số nguyên phụ thuộc vào phần thập phân.
int main(){
	cout << abs(-432) << endl;
	cout << max(534,2312) << endl;
	cout << min(2423,5345) << endl;
	cout << sqrt(25) << endl;
	cout << pow(2,2) << endl;

	return 0;
}