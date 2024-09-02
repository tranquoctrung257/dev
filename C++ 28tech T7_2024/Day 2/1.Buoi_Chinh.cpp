#include <iostream>
using namespace std;

//int main(){
////	int n = 10;
////	n = n+2;
////	n+=2;// cách này sử dụng nhiều hơn
////	n = n*2;
////	n*=2;
//	
//}

// kiến thức toán cần nhớ 

//- từ 1 đến 7 có bao nhiêu số chia hết cho 7
// lấy n/7 sẽ ra những số chia hết cho 7

// toán tử so sánh 
//> lớn hơn
//>= lớn hơn hoặc bằng
//< bé hơn
//<= bé hơn hoặc bằng
//!= so sánh khác
//== so sánh bằng

// toán tử logic
//and &&
//or || 
//not !

//and điều kiện của nó phải đúng tất cả với đúng
//0 and 0 = 0
//0 and 1 = 0 
//1 and 0 = 0
//0 and 0 = 0

// or điều kiện để đúng là một trong các điều kiện đúng là đúng
//0 or 0 = 0
//0 or 1 = 1
//1 or 0 = 1
//1 or 1 = 1

//toán tử tăng giảm
//++n | toán tử tăng trước
//n++ tăng n lên 1 đơn vị | toán tử tăng sau

//--n
//n-- giảm n 1 đơn vị

//int main(){
//	int n = 423;
//	cout << n++ << endl;// in ra n rồi mới tăng | in ra n sau đó mới cộng n lên 424
//	cout << n << endl; // n sau khi tăng   
//	cout << --n << endl; // trừ n 1 đơn vị | rồi in ra 
//	cout << n << endl;
//}

//int main(){
//	int a = 100; //100
//	int b = a++; //100
//	int c = ++a; //102
//	cout << a << " " << b << " " << c << endl; // 102 100 102
//}

//toán tử 3 ngôi
//[biểu thức so sánh] >[giá trị trả về biểu thức đúng] : [giá trị trả về biểu thức sai]
//
//int main(){
////	int x = 10 < 20 ? 5 : 10;
////	cout << x << endl;
//	int a = 100,b = 432;
//	int x = a > b ? b : a;
//	cout << x << endl;
//}

// cấu trúc rẽ nhánh

//if(condition){
//	//code
//}

//ví dụ kiểm tra n có thuộc đoạn 10-50 không
//int main(){
//	int n = 20;
//	if((n>=10)&&(n<=50)){
//		cout << "PHP" << endl;
//		cout << "C++" << endl;
//	}
//	cout << "endl" << endl;
//}

// kiểm tra n là số nguyên dương: if(n>0)
// kiểm tra n là số chẵn: if(n%2==0)
// kiểm tra n là số lẻ: if(n%2 != 0)
// kiểu tra n thuộc đoạn [x:y]: if((n >= x) && (n <= y))
// kiểm tra n chia hết cho k: if(n%k==0)
// kiểm tra n không chia hết cho k: if(n%k!=0)
// kiểm tra n chia hết cho a hoặc b: if((n%a == 0) || (n % b == 0))
// kiểm tra n là số nguyên tố có 1 chữ số:if( n == 2 || n == 3 || n == 5 || n == 7)
// kiểm tra n là số có k chữ số: if((n >= pow(10,k-1)) && (n < pow(10,k+1)))  

 
//if(condition){
////	code if
//}
//else {
//	// code else
//}


//if(codition){
//	// code 
//}
//else if(condition 1){
//	// code
//}
//else if(condition 2){
//	// code
//}
//else if(condition n){
//	// code
//}
//else{
//	//code
//}

//A-Z = 65-90
//a-z = 97-122
//0-9 = 48-57
//int main(){
//	char c = 'a';
//	cout << (int)c << endl;
//}




