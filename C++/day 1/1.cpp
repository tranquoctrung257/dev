#include <iostream>
#include <bits/stdc++.h>
#include <math.h>

#include <iomanip> // thư viện << fixed << setprecision(3)
using namespace std;

// int main(){
// 	cout << "Hello world" << endl;
// }

// cac kieu du lieu trong c++: data_type

// kiểu dữ liệu
// - số nguyên: int,long long | không thể lưu số thực
// int: 4byte = 32bit ==> -2^31 ->2^31 -1 [-2.10^9 ==> 2.10^9]
// long long: 8byte = 64bit ==> -2^63 -> 2^63-1 [-9.10^18 =>9.10^18 ]

// - số thực: float,doube
// float: 4byte = 32bit ==> lưu được 6 số phần thập phân
// doube: 8byte = 64bit ==> lưu được 15 số phần thập phân
// - kí tự:char: character: 1byte 
// neu qua so tren se tra ve gia tri rac

// so thuc
// float 4byte = 32bit: 6 so thap phan
// double 8byte = 64bit: 15 so thap phan


// int main(){
// 	// để in ra giá trị lớn nhất của các kiểu dữ liệu
// 	cout << INT_MIN << " " << INT_MAX << endl;
// 	cout << LLONG_MIN << " " << LLONG_MAX << endl;

// 	return 0;
// }

// variable: biến trong c++
// int main(){
// 	// để khai báo 1 biến trong c++
// 	// [data_type] [ten bien];
// 	int banKinh;
// 	long long dientich;
// 	float chuvi;
// 	double duongkinh;
// 	char kitu;

// 	// quy tắc đặt tên biến:
// 	// - không được đặt tên biến có số ở đầu.
// 	// - không được chứa dấu cách và các kí tự đặc biệt.
// 	// - không được đặt trùng với từ khóa (keyword) : int,main,using,for,while,...
// 	// - kí tự _ sẽ hợp lệ.
// 	// - Không được đặt tên biến có dấu

// 	// có thể khai báo nhiều biến trên 1 dòng.
// 	// long long x,y,z; // khai báo giá trị này sẽ trả về giá trị rác
// 	// cout << x << endl;

// 	// int a = 54; // khai báo + khởi tạo giá trị
// 	// cout << a << endl;

// 	// long long b = 2312,c = 432423;
// 	// cout << a << " " << " " << b << " " << c << endl;

// 	// in ra câu dẫn ở đàng trước
// 	// cout << "gia tri cua bien a,b,c là: "<< a << " " << " " << b << " " << c << endl;

// 	// cout << " " << endl; // xâu kí tự
// 	// cout << ' ' << endl; // kí tự

// 	// int n = 1000000000000; // tràn số nên trả về giá trị rác
// 	// cout << n << endl;

// 	// float x = 3.14000;
// 	// cout << x << endl;

// 	// float z = 3.123456; 
// 	// cout << fixed << setprecision(3) << z << endl; // in ra 3 số với 3 số đằng sau dấu phẩy

// 	// char c = "z"; // Đây là xâu kí tự z
// 	// char c = 'z'; // đây là kí tự z
// 	// cout << c << endl;

// 	// để nhập 1 giá trị từ bàn phím
// 	// int a;
// 	// cin >> a;
// 	// cout << a;

// 	// nhập giá trị cho nhiều biến
// 	// int a,b,c;
// 	// cin >> a >> b >> c;
// 	// cout << a << " " << b << " " << c;

// 	// có thể sửa đổi giá trị của 1 biến trong khi thay code
// 	int n = 100;
// 	n = 200;
// 	n = 300;
// 	cout << n << endl;

// 	// = toán tử gán
// 	// x = y ==> lấy y gán cho x.


// }


// int main(){
// 	// toán tử toán học

// 	// int chieudai = 20, chieurong = 10;
// 	// int dientich = chieudai * chieurong;
// 	// int nuachuvi = chieudai + chieurong;
// 	// cout << "Diện tích hình chữ nhật là: " << dientich << endl;
// 	// cout << "nửa chu vi của hình chữ nhật là: " << nuachuvi << endl; 
// 	// cout << "chiều dài gấp chiều rộng số lần là: " << chieudai / chieurong << endl;
// 	// cout << "Hiệu của chiều dài và chiều rộng là: " << chieudai - chieurong << endl;

// 	// ép kiểu trong c++ | (data_type)teb_bien ==> ép biến kiểu tên biến sang kiểu data_type

// 	// cho 2 biến a,b tính tổng hiệu tích thương của 2 biến và in ra màn hình.
// 	int a = 500,b = 200;
// 	int tong = a+b;
// 	int hieu = a-b;
// 	int tich = a*b;
	
// 	// int thuong = a/b; // nếu chia số nguyên cho số nguyên sẽ ra số nguyên ví dụ 5/2= 2| để ra phần thập phân thì phải có ít nhất 1 trong 2 số là số thực 

// 	// sử lại
// 	double thuong = (double)a / b;
	
// 	// ==> khi chia 2 số nguyên với nhau (int,long long) kết quả sẽ là số nguyên
// 	// ==> khi chia 2 số mà muốn giữ phần thập phân: ép kiểu số chia (hoặc số bị chia) sang float hoặc double

// 	// hoặc có thể áp dụng như thế này
// 	cout << a*1.0 / b << endl;
// 	int du = a%b;
// 	cout << tong << " " << hieu << " " << tich << " " << fixed << setprecision(3)<<thuong <<" " <<du << endl;
// }

// lưu ý:
// int main(){
// 	int a = 1000000;
// 	int b = 1000000;
// 	// int tich = a*b; // quá giới han của int nên sẽ trả về giá trị rác nên phải sử dụng long long
// 	// long long tich = a*b; //  nó vẫn sai vì khi nhân 2 số int thì nó sẽ lưu tạm ở vùng nhớ 4byte nên phải ép 1 trong 2 sang long long

// 	// long long tich = (long long)a * b; // cách 1 
// 	long long tich = 1ll * a * b; // 1ll là 1 long long 
// 	cout << tich << endl;
// }

// kiểu dữ liệu bool
// các số khác không được coi là true , chỉ có số 0 được coi là sai.
// int main(){
// 	bool check = true,check_2 = false;
// 	cout << check << " " << check_2 <<endl;
// }

// toán tử so sánh 
// > < >= <= != ==
// int main(){
// 	bool check = 10 > 1; // gán giá trị phép so sánh cho biến check.
// 	cout << check << endl;
// }

// toán tử 1 ngôi
// int main(){
// 	int n = 100;
// 	n++; // tăng n lên 1 đơn vị, đây gọi là n tăng sau | ++n ==> n tăng trước
// 	cout << n << endl;
// 	n--; // giảm n 1 đơn vị, đây gọi là n giảm sau | --n gọi là n tăng trước
// 	cout << n << endl;
// }

// bảng chân trị
// 1 and 1 ==> 1
// 1 and 0 ==> 0
// 0 and 0 ==> 0
// 0 and 1 ==> 0

// 1 or 1 ==> 1
// 1 or 0 ==> 1
// 0 or 1 ==> 1
// 0 or 0 ==> 0 

// not 1 ==> 0
// not 0 ==> 1

// 0: false
// 1: true

// and kí hiêu &&
// or kí hiệu ||
// not !

// cấu trúc rẽ nhánh

// int main(){
	// if(dieu_kien){
	// 	code
	// }

	// if(true){
	// 	cout << "if đã được thực hiện!" << endl;
	// }

	// int n = 500;
	// if(n < 1000){
	// 	cout << "n là số bé hơn 1000!" << endl;
	// }

	// kiểm tra số chia hết cho 5 ko
	// int n = 100;
	// if((n%5)==0){
	// 	cout << "n là số chia hết cho 5!" << endl;
	// }

	// kiểm tra n là số chẵn
	// int n = 300;
	// if(n%2==0){
	// 	cout << "n là số chẵn!" << endl;
	// }
	
	// kiểm tra n >= 500 và n <= 1000:
	// int n = 542;
	// if((n >= 500) && (n <=1000)){
	// 	cout << "n là số lớn hơn hoặc bằng 500 và bé hơn hoặc bằng 1000";
	// }


	// if(dieu kien){
	// 	// code
	// }
	// else{
	// 	// code
	// }
	
	// int n = 10000;
	// if (n < 200){
	// 	cout << "yes" << endl;
	// }
	// else{
	// 	cout << "no" << endl;
	// }

	// if(điều kiện 1){
	// 	code 
	// }
	// else if(điều kiện 2){
	// 	code
	// }
	// else if(điều kiện 3){
	// 	code
	// }
	// else if(điều kiện n){
	// 	code 
	// }
	// else{
	// 	code
	// }

	// nhập một số trong tuần in ra ngày tương ứng

	// int n; cin >> n;
	// if(n == 1){
	// 	cout << "chủ nhật!" << endl;
	// }
	// else if(n == 2){
	// 	cout << "thứ hai!" << endl;
	// }
	// else if(n == 3){
	// 	cout << "thứ ba!" << endl;
	// }
	// else if(n == 4){
	// 	cout << "thứ tư" << endl;
	// }
	// else if(n == 5){
	// 	cout << "thứ năm" << endl;
	// }
	// else if(n == 6){
	// 	cout << "thứ sáu" << endl;
	// }
	// else if(n == 7){
	// 	cout << "thứ bảy" << endl;
	// }
	// else{
	// 	cout << "dữ liệu sai!" << endl;
	// }


// }
	
// int main(){
// 	int x;cin >> x;
// 	long long res = (long long)x * x * x + 3 * (long long)x * x + x + 1;
// 	cout << res << endl;
// }


int main(){
	// pow(a,b) ==> a^b | [a^1/2 là căn bậc 2]
	// sqrt(a) ==> tính căn bậc 2 của a
	// 2 hàm pow và sqrt đều trả về double
}

