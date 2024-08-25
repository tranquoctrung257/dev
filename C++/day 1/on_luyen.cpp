#include <bits/stdc++.h>
using namespace std;
// kiểu dữ kiệu 
// - số nguyên int,long long
// - số thực float,double


int main(){
	// int a = 5, b = 2;
	// int c = a/b;// chia lấy phần nguyên
	// int d = a%b;// lấy phần dư
	// // double e = 1.0*a/b; // trả về số có phần thập phân
	// double e = double(a) /b;
	// cout << e << endl;

	// int a = 1000000,b = 10000000;
	// long long s = (long long)a*b;
	// cout << s << endl;

	// nhập điểm x.
	// nếu x <= 9 <= 10 giỏi
	// nếu 6.5 <= x < 9 khá
	// nếu 5 <= x < 6.5 trung bình

	// double x; cin >> x;

	// if(x>5){
	// 	cout << "trên 5" << endl;
	// }

	// if(x >= 9 && x <= 10){
	// 	cout << "giỏi!" << endl;
	// }
	// else if(x >= 6.5 && x < 9){
	// 	cout << "khá" << endl;
	// }
	// else if(x >= 5 &&  x <= 6.5){
	// 	cout << "trung bình" << endl;
	// }
	// else{
	// 	cout << "yếu" << endl;
	// }

	// bảng mã ascii
	// char c;cin >> c;
	// cout << int(c) << endl; // kiểm tra bảng mã vị trí của kí tự trong bảng mã ascii

	// kiểm tra c là chữ hoa hay chữ thường	
	
	// char c;cin >> c;
	
	// if(c >= 65 && c <= 90){
	// 	cout << "chữ hoa" << endl;
	// }
	// else if(c >= 97 && c <= 122){
	// 	cout << "chữ thường" << endl;
	// }
	// else{
	// 	cout << "không phải chữ cái" << endl;
	// }

	// cách khác
	// if(c >= 'A' && c <= 'Z'){
	// 	cout << "chữ hoa" << endl;
	// }
	// else if(c >= 'a' && c <= 'z'){
	// 	cout << "chữ thường" << endl;
	// }
	// else{
	// 	cout << "không phải chữ cái" << endl;
	// }

	// chuyển đổi chữ thường thành chữ hoa
	// if(c >= 'a' && c <= 'z'){
	// 	cout << (char)(c-32) << endl;
	// }
		

	// chuyển đổi chữ hoa thành chữ thường
	// if(c >= 'A' && c <= 'Z'){
	// 	cout << (char)(c+32) << endl;
	// }

	// để in khoảng cách giữa a và A
	// cout << 'a' - 'A' << endl;

	// nếu là chữ hoa in ra chữ thường và ngược lại.
	// if(c >= 'a' && c <= 'z'){
	// 	cout << (char)(c-32) << endl;
	// }
	// else if(c >= 'A' && c <= 'Z'){
	// 	cout << (char)(c+32) << endl;
	// }

	// nhập x và in ra chữ cái liên sau đối với chữ z thì in a.
	// char x; cin >> x;
	// if(c >= 'a' && c <= 'z'){
	// 	cout << (char)(c+1) << endl;
	// }
	// else if(c >= 'A' && c <= 'Z'){
	// 	cout << (char)(c+1) << endl;
	// }
	// else if(c == 'z'){
	// 	cout << "a";
	// }
	// else if(c == 'Z'){
	// 	cout << "A";
	// }

	// nhập vào chữ in kí tự chữ hoa hoặc chữ thường và in ra chữ thường tiếp theo và kí tự z hoặc Z thì in ra a
	// char x; cin >> x;
	// if(c >= 'a' && c <= 'z'){
	// 	cout << (char)(c+1) << endl;
	// }
	// else if(c >= 'A' && c <= 'Z'){
	// 	cout << (char)(c+33) << endl;
	// }
	// else if(c == 'z'|| c == 'Z'){
	// 	cout << "a";
	// }

	// int a,b,c; cin >> a >> b >> c;
	// if(a == b && a == c && b == c){
	// 	cout << "3";
	// }
	// else if((a == b) || b==c || a == c){
	// 	cout << "2";
	// }
	// else{
	// 	cout << "1";
	// }
}