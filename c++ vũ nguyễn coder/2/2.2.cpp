#include <iostream>
#include <string>
using namespace std;
int main() {
	// nhập dữ kiệu từ bàn phím 
	// cin charater out 
	int tuoi;
	string ho_ten = "";

	cout << "nhap ten: ";

	// cin coi dấu cách là kêt thúc một luồng
	// getline(cin, ho_ten);

	cin >> ho_ten;

	cout << "Nhap tuoi: ";
	cin >> tuoi;
	
	cout << ho_ten << " nam nay " << tuoi << " tuoi" << endl;


}