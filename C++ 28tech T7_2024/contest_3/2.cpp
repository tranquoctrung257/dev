#include <bits/stdc++.h>
using namespace std;
 
using ll = long long;
using db = double;
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;cin >> n;
    for(int i = 1;i<=n;i+=3){
    	cout << i << " ";
    }
    cout << endl;

    for(int i = 1;i<=n;i*=2){
    	cout << i << ' ';
    }
    cout << endl;

    for(int i = 1; ;i++){
    	if(i%17==0){
    		cout << i;
    		break;
    	}
    }
    cout << endl;

    for(int i = n; ;i--){
    	if(i%7==0){
    		cout << i;
    		break;
    	}
    }
    cout << endl;

    int kc = 0;
    for(int i = 1;i<=n;i+=kc){
    	cout << i << " ";
    	kc++;
    }
    
    cout << endl;

}