#include <iostream>
#include <iomanip>

using namespace std;

int main(){
    int a,b; cin >> a >> b;
    cout << 1ll *a+b << endl;
    cout << a-b << endl;
    cout << 1ll*a*b << endl;
    if (a==0 || b == 0){
        cout << "INVALID" << endl;
    }
    else cout << setprecision(4) << fixed << 1.0*a / b << endl;
}