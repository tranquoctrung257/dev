# include <bits/stdc++.h>
using namespace std;

int main(){
    double x;
    cin >> x;
    double smaller = floor(x);
    cout << (int)smaller<< endl;

    double larger = ceil(x);
    cout << (int)larger << endl;
    
    double nearest = round(x);
    cout << (int)nearest << endl;
    
}