#include <iostream>

using namespace std;

int main(){
    char c;
    cin >> c;
    if(c>=65&&c<=90){
        cout << "UPPER" << endl;
    }
    else if(c>=97&&c<=122){
        cout << "LOWER" << endl;
    }
    else if(c>=48&&c<=57){
        cout << "DIGIT" << endl;
    }
    else{
        cout << "SPECIAL" << endl;
    }
}