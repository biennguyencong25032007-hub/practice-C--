#include <iostream>
#include <string>
#include <cctype>
using namespace std;

// Bài 15: Xóa khoảng trắng thừa
// Xóa các khoảng trắng thừa ở đầu, cuối và giữa chuỗi
string bai_15(string s) {
    string result = "";
    bool inSpace = false;
    
    // Duyệt qua từng ký tự
    for (int i = 0; i < s.length(); i++) {
        if (isspace(s[i])) {
            // Nếu gặp khoảng trắng và chưa có khoảng trắng nào trong result
            if (!inSpace && !result.empty()) {
                result += ' ';
                inSpace = true;
            }
        } else {
            // Ký tự không phải khoảng trắng
            result += s[i];
            inSpace = false;
        }
    }
    
    // Xóa khoảng trắng ở cuối nếu có
    if (!result.empty() && isspace(result.back())) {
        result.pop_back();
    }
    
    return result;
}

int main() {
    string s1 = "  hello   world  ";
    string s2 = "   abc    def    ghi   ";
    string s3 = "no extra spaces";
    
    cout << "Original: '" << s1 << "'" << endl;
    cout << "Converted: '" << bai_15(s1) << "'" << endl << endl;
    
    cout << "Original: '" << s2 << "'" << endl;
    cout << "Converted: '" << bai_15(s2) << "'" << endl << endl;
    
    cout << "Original: '" << s3 << "'" << endl;
    cout << "Converted: '" << bai_15(s3) << "'" << endl;
    
    return 0;
}

