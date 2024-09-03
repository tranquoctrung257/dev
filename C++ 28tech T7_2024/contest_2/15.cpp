#include <iostream>

using namespace std;

int main()
{
    long long n, a, b;
    cin >> n >> a >> b;

    // a giá tiền chai 1 lít
    // b giá tiền chai 2 lít
    if (b >= 2 * a)
    {
        cout << n * a << endl;
    }
    else
    {
        if (n % 2 == 0)
        {
            cout << n / 2 * b << endl;
        }
        else
        {
            cout << (n - 1) / 2 * b + a << endl;
        }
    }
}