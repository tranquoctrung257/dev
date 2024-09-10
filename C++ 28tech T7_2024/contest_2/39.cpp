#include <iostream>
#include <algorithm>

using namespace std;
int main(){
	int a,b,c; cin >> a >> b >> c;
	int max_abc = max({a,b,c});
	int min_abc = min({a,b,c});
	cout << min_abc << " " << a+b+c-max_abc-min_abc << " " << max_abc << endl;
}