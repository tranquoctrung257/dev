#include <iostream>

using namespace std;

int main() {
    int N;
    cin >> N;

    for(int i = 1;i<=N;i++){
        cout << i << " ";
    }
    cout << endl;
    // 2
    for(int i = N;i >=0 ;i--){
        cout << i << " ";
    }
    cout << endl;

    // 3
    for(int i = 0;i<=N;i+=2){
        cout << i << " ";
    }
    cout << endl;

    // 4
    for(int i = 1;i<=N;i+=2){
        cout << i << " ";
    }
    cout << endl;
    // 5
    for(int i = 0;i < N;i+=4){cout << i << " ";}
    cout << endl;

    for (int i = 0; i < N; i++) {
        cout << char('a' + i) << " ";
    }
    cout << endl;

    for (int i = N - 1; i >= 0; i--) {
        cout << char('z' - i) << " ";
    }
    cout << endl;

    return 0;
}
