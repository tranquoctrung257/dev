#include <iostream>
#include <cmath>
using namespace std;

// công thức tính tạo độ là 
//căn bậc 2 của (x*2 + y*2)
int main(){
	int x,y;cin >> x >> y;
	long long x_binh = x * x;
	long long y_binh = y * y;
	cout << sqrt(x_binh + y_binh) << endl;
}