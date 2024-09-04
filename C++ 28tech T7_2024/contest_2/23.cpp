#include <iostream>

using namespace std;

int main()
{
    int n, m;
    cin >> n >> m;
    int min, max = n;
    if (n % 2 == 0)
    {
        min = n / 2;
    }
    else
    {
        min = n / 2 + 1;
    }
    int res;
    if (min % m == 0)
    {
        res = min;
    }
    else
    {
        res = (min / m + 1) * m;
    }
    if (res <= max)
    {
        cout << res << endl;
    }
    else
    {
        cout << "-1" << endl;
    }
}