#include <iostream>

using namespace std;

int main(){
	int n; cin >> n;
	
	// 1.N có chẵn hay không
	if (n%2==0) {
		cout << "YES" << endl;
	}
	else cout << "NO" << endl;
	
	// 2.N có phải số chia hết cho 3, vừa chia hết cho 5?
	if ( n % 3 == 0 && n % 5 == 0){
		cout << "YES" << endl;
	}
	else cout << "NO" << endl;
	
	// 3.N có phải số chia hết cho 3 nhưng không chia hết cho 7? || nhưng and
	if (n % 3 == 0 && n % 7 != 0){
		cout << "YES" << endl;
	} 
	else cout << "NO" << endl;
	
	// 4.N có phải số chia hết cho 3 hoặc 7?
	if (n % 3 == 0 || n % 7 == 0){
		cout << "YES" << endl;
	}
	else cout << "NO" << endl;
	
	// hoặc sử dụng toán tử 3 ngôi.
//	(n % 3 == 0 || n % 7 == 0 ) ? cout << "YES" << endl : cout << "NO" << endl; 

	// 5. lớn hơn 30 và nhỏ hơn 50 || lớn hơn và nhỏ hơn là không có bằng
	if(n > 30 && n < 50){
		cout << "YES"<< endl;
	}
	else cout << "NO" << endl;
	
	//6. số không nhỏ hơn 30 và chia hết cho ít nhất 1 trong 3 số 2,3,5? // không nhỏ hơn là lớn hơn hoặc bằng
	if(n >= 30 && (n % 2 == 0 || n % 3 == 0 || n % 4 == 0)){
		cout << "YES" << endl;
	}
	else cout << "NO" << endl;
	
	//7. N có phải là số có 2 chữ số có tận cùng là số nguyên tố
	int lastdigit = n % 10;
	if((n >= 10 && n <= 99) && (lastdigit == 2 || lastdigit == 3 || lastdigit == 5 || lastdigit == 7)){
		cout << "YES" << endl;
	} 
	else cout << "NO" << endl;
	
	//8. N có phải số không vượt quá 100 và chia hết cho 23 | không vượt quá là <= 
	if(n <= 100 && n % 23 == 0 ){
		cout << "YES" << endl;
	} 
	else cout << "NO" << endl;
	
	
	//9.N không thuộc đoạn [10:20]
	if(n < 10 || n > 20){
		cout << "YES" << endl;
	} 
	else cout << "NO" << endl;
	
	//10.N có chữ số tận cùng là bội của 3.
	if (lastdigit % 3 == 0){
		cout << "YES" << endl;
	} 
	else cout << "NO" << endl;
}
