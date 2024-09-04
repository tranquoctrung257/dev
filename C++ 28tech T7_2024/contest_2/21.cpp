#include <iostream>
using namespace std;

int main()
{
    long long a, b, k;
    long long k1, k2;
    cin >> a >> b >> k;
    if (k % 2 == 0)
    {
        k1 = k / 2;
        k2 = k / 2;
    }
    else
    {
        k1 = k / 2 + 1;
        k2 = k / 2;
    }
    cout << k1 * a - k2 * b << endl;
}