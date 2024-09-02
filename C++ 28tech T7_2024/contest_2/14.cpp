// Bài 14: xếp loại học sinh
// cho biêt điểm kiểm tra tin học của 1 em là a,b,c(2 điểm a,b hệ số 1,c là hệ số 2,d là hệ số 3)
// in ra kết quả học tập môn tin học của em đó. nếu điểm tổng kết >= 8 đạt kết quả giỏi, <8 và >= 6.5 đạt được kết quả khá, và >= 5 đạt kết quả trung bình,<5 đạt kêt quả yếu

// điểm trung bình được tính bằng tổng hệ số nhan với điểm chia cho tổng hệ số

// đầu vào 
// một dòng chưa 4 số điểm của học sinh 

// giới hạn
// điểm là số thực từ 0 đến 10

// đầu ra 
// kết quả học tập môn tin hcoj của em học sinh ở dạng in hoa không dấu 
// ví dụ 
// input1
// 9 8 7 8.5
// output1
// GIOI

//input2
//5 7 6.5 5
//output2
//TRUNG BINH

#include <iostream>
using namespace std;

int main(){
	double a,b,c,d;cin >> a >> b >> c >> d;
	double dtb = ((a+b)+(2*c)+(3*d)) / 7;
	if(dtb <= 10 && dtb >=8 ){
		cout << "GIOI" << endl;
	}
	else if (dtb >= 6.5 && dtb < 8){
		cout << "KHA" << endl;
	}
	else if(dtb >= 5 && dtb < 6.5){
		cout << "TRUNG BINH" << endl;
	}
	else{
		cout << "YEU" << endl;
	}
	
	
	
	
	
	
	
	
	
	
	
	
	
	
}