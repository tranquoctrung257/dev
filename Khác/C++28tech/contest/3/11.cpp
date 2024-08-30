#include<bits/stdc++.h>
using namespace std;

int main(){
    long long s,t=0;
    cin >> s;
    for(int i = 1;i<=s;i++){
        // luu y khi muon pow tra ve so nguyen phai ep pow sang so nguyen vi pow no co the ra so thu
        t += (int)pow(-1,i)*i;
       
    }
    cout << t << endl;    
}
