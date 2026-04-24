#include <iostream>
using namespace std;

int main(){
    int n;
    cout << "nhap vao so n: ";
    cin >> n;
    
    int sum = 0;
    for (int i = 1; i <= n; i++) {
        sum += i;
    }
    
    cout << "Tong tu 1 den " << n << " la: " << sum << endl;
    
    return 0;
}