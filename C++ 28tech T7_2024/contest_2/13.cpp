#include <iostream>

using namespace std;

int main(){
    int n;cin >> n;
    int nam = n/365;
    // int tuan = (n - n*365)/7;
    int tuan = n % 365 / 7;
    int ngay = n % 365 % 7;
    cout << nam << " " << tuan << " " << n - (n*365) - (tuan*7) << endl;
}