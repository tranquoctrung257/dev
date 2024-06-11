#include <iostream>
using namespace std;

int main() {
	// biến và kiểu dữ liệu 
	// biết: variable
	// khai báo biến variable declaration
	
	// - quy tac dat bien
	// + các biến không được trùng với nhau 
	// + tên biến chỉ có thể chứa kí tự, kí tự số và _
	// + tên biến không được bắt đầu bằng số
	// + biến phân biệt chữ hoa và chữ thường
	// + tên biến không được chứa keyword (từ khóa)
	
	// - kiểu dữ liệu
	// + int: số nguyên 4byte
	// + float: số thực 4byte
	// + char: kí tự 'A' 1byte (lưu ý đặt trong dấu nháy đơn,kiểu char chỉ lưu 1 kí tự, char ở đàng sau nó là một mã ASCII)
	
	// để in ra mã ascii của một kí tự nào đó
	cout << int('a') << endl;

	// string: kí tự (nếu không có using namespace; , thì cần phải #include <string>)
	// bool : đúng/sai (false là 0, true khác 0)
	// void : kiểu dữ liệu không có giá trị	
	// hàm sizeof() trả về giá trị biết đó lưu được bao nhêu byte
	
	// biến hằng số (nó không thể thay đổi giá trị của biến
	const float PI = 3.14;
	// ví dụ
	int tuoi = 30; // khởi tạo giá trị tuoi bằng 30

	cout << "Toi nam nay " << tuoi << " tuoi \n";
	cout << sizeof(int) << " byte\n";
	cout << INT_MAX << endl;
}