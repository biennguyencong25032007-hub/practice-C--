#include <iostream>
#include <string>
#include <cctype>
using namespace std;

string bai_14(string s) {
    for (int i = 0; i < s.length(); i++) {
        if (isupper(s[i])) {
            s[i] = tolower(s[i]);
        } else if (islower(s[i])) {
            s[i] = toupper(s[i]);
        }
    }
    return s;
}

int main() {
    string s = "Hello World 123";
    string result = bai_14(s);
    cout << "Original: " << s << endl;
    cout << "Converted: " << result << endl;
    return 0;
}