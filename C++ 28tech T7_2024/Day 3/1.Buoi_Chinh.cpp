#include <iostream>
using namespace std;

//int main(){
//    // cấu trúc rẽ nhánh swithch case 
//    // switch (val)
//    // {
//    // case 1:
//    //     /* code */
//    //     break;
//    // case 2:
//    //     code 
//    //     break;
//    // default:
//    //     break;
//    // }
//    // code của switch case sẽ chạy case đúng và chạy hét những case dưới đó
//    int n = 3;
//    switch (n)
//    {
//    case 1:
//        cout << "CHU NHAT" << endl;
//        break;
//    case 2:
//        cout << "THU HAI" << endl;
//        break;
//    case 3:
//        cout << "THU BA" << endl;
//        break;
//    case 4:
//        cout << "THU TU" << endl;
//        break;
//    default:
//        cout << "!12345!" << endl;
//    }
//}

// ví dụ tìm số ngày của tháng
//int main(){
//	int t = 13;
//	switch(t){
//		case 1 : case 3 : case 5 : case 7 : case 8 : case 10 : case 12:
//			cout << 31 << endl;
//			break;
//		case 4 : case 6 : case 9 : case 11:
//			cout << 30 << endl;
//			break;
//		default:
//			cout << "nhap sai" << endl;
//	}
//
//}

// có thể check được số nằm trong 1 đoạn

//int main(){
//	int t = 123;
//	switch(t){
//		case 1 ... 100:
//			cout << "1==> 100" << endl;
//			break;
//		case 101 ... 201:
//			cout << "101 ==> 201" << endl;
//			break;
//		default:
//			cout << "số không nằm trong đoạn" << endl;
//	}
//}

// có thể không cần dấu {} khi sử dụng if else elseif

//int main(){
//	int n = 1110;
//	if(n%2==0) 
//		cout << "so chan" << endl;
//	else 
//		cout << "so le" << endl;
//}

// chương trình đang chạy mà gặp return 0 sẽ dừng luôn
//int main(){
//	cout << "abc" << endl;
//	return 0;
//}


// vòng lặp

//cú pháp
//for([câu lệnh khởi tạo];[điều kiện lặp];[câu lệnh cập nhật]){
////	code bên trong vòng for
//}

//int main(){
//	for(int i = 1;i<=3;i++){
//		cout << i << endl;
//	}
//}

//// vòng for có thể thiếu điều kiện nào đó
//int main(){
//	for(int i = 1;;i++){
//		cout << i << endl;
//	}
//}
//// vòng for này sẽ chạy vĩnh viễn vì ko có điều kiện lặp


//int main(){
//	for(int i = 0;i<=50;i++){
//		if(i%2==0) cout << i << endl;
//	}
//}

// dự đoán kết quả của bài này

//int main(){
//	for(int i = 1;i < 14;i+=2){
//		cout << i << endl;
//		i++;
//	}
//}

// các vòng lặp thường gặp
//1. vòng lặp n lần: for(int i = 1;i<=n;i++)
//2. vòng lặp n lần: for(int i = 0;i<=n-1;i++)
//3. vòng lặp n lần: for(int i = 0;i<n;i++)
//4. vòng lặp n lần: for(int i = 0;i>=n;i--)
//5. vòng lặp từ a đến b: for(int i = a; i<= b;i++)
//6. vòng lặp từ b đến a: for(int i = b; i<= a;i++)
//7. vòng lặp duyệt các bộ của k mà <= n: for(int i = 0;i <=n;i+=k)

//int main(){
//	// tìm số lớn >= min và <= max chia hết cho 7
//	int min = 23,max = 50;
//	for(int i = min;i<=max;i++){
//		if(i%7==0){
//			cout << i << endl;
//			break;
//		}
//	}
//}

// break dừng vòng for khi gặp đc nó
//continue là bỏ qua các câu lệnh ở dưới chạy vòng for tiếp theo

int main(){
	for(int i = 1;i<=10;i++){
		cout << i<< endl;
		continue;
		cout << "endl" << endl;
	}
}

