#include <bits/stdc++.h>
using namespace std;

// khai bao mac dinh
const double PI = 3.14;

int main(){
    int x1,y1,x2,y2;
    cin >> x1 >> y1 >> x2 >> y2;
    double kq = sqrt(pow(x1-x2,2) + pow(y1-y2,2));
    cout << fixed << setprecision(2) << kq <<endl;
    
}