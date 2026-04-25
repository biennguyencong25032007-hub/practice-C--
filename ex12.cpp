#include <iostream>
#include <string>
#include <sstream>
using namespace std;

int main() {
    string line;
    
    cout << "Nhap chuoi: ";
    getline(cin, line);
    
    // Dem so tu bang cach su dung stringstream
    stringstream ss(line);
    string word;
    int count = 0;
    
    while (ss >> word) {
        count++;
    }
    
    // In ket qua
    cout << "So tu trong chuoi: " << count << endl;
    
    return 0;
}