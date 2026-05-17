#include <iostream> 
using namespace std;

int main(){
    int n;
    cout << "nhap vao so n: ";
    cin >> n;

    if (n >= 0){
        cout << "gia tri tuyet doi cua n la: " << n << endl;

    }
    else{
        cout << "gia tri tuyet doi cua n la:" << n * -1 << endl;

    }
    return 0;

}