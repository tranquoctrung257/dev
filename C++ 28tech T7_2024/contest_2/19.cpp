#include <iostream>
using namespace std;

int main()
{
    long long n, m;
    cin >> n >> m;
    if (n % 2 == 0){
        cout << (n/2)*m << endl;
    }
    else cout << (n/2)*m + m/2 << endl;
}