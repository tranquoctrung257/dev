#include <iostream>

using namespace std;

int main()
{
    int a, b, c;
    cin >> a >> b >> c;
    if (a > 0 && b > 0 && c > 0 && a + b > c && b + c > a && a + c > b)
    {
        // kiểm tra tam giác đều
        if (a == b && b == c)
        {
            cout << 1 << endl;
        }
        else if (a == b || b == c || c == a)
        {
            cout << 2 << endl;
        }
        else if ((a * a == b * b + c * c) || (b * b == a * a + c * c) || (c * c == b * b + a * a))
        {
            cout << 3 << endl;
        }
    }
    else
    {
        cout << "INVALID" << endl;
    }
}