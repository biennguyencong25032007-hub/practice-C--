#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int main() {
    string str;
    
    cout << "Nhap chuoi: ";
    getline(cin, str);
    
    // Loai bo khoang trang va chuyen thanh chu thuong
    string cleaned = "";
    for (char c : str) {
        if (!isspace(c)) {
            cleaned += tolower(c);
        }
    }
    
    // Kiem tra palindrome
    bool isPalindrome = true;
    int n = cleaned.length();
    for (int i = 0; i < n / 2; i++) {
        if (cleaned[i] != cleaned[n - 1 - i]) {
            isPalindrome = false;
            break;
        }
    }
    
    // In ket qua
    if (isPalindrome) {
        cout << "\"" << str << "\" la mot palindrome!" << endl;
    } else {
        cout << "\"" << str << "\" khong phai la palindrome." << endl;
    }
    
    return 0;
}
