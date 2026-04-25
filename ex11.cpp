#include <iostream>
#include <string>
using namespace std;

string reverseString(string s) {
    string result = "";
    for (int i = s.length() - 1; i >= 0; i--) {
        result += s[i];
    }
    return result;
}

int main (){
    string s;
    cout << "Nhap vao chuoi: ";
    getline(cin, s);
    
    string reversed = reverseString(s);
    cout << "Chuoi dao nguoc: " << reversed << endl;
    
    return 0;
}