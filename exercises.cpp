// ========================================
// BÀI TẬP LUYỆN TẬP C++
// ========================================

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <fstream>
#include <cmath>

using namespace std;

// ========== PHẦN 1: CƠ BẢN (BASIC) ==========

// Bài 1: Hiển thị "Hello World"
// TODO: In ra màn hình "Hello C++"
void bai_1() {
    cout << "Hello World" << endl;
    cout << "Hello C++" << endl;
}

// Bài 2: Tính tổng hai số
// TODO: Viết hàm cộng hai số a và b
int bai_2(int a, int b) {
    cin >> a; 
    cin >> b;
    
    cout << "tong cua a va b la: " << a + b << endl;
    
}

// Bài 3: Kiểm tra số chẵn lẻ
// TODO: Hàm nhận vào một số, trả về true nếu chẵn, false nếu lẻ
bool bai_3(int n) {
    // TODO: Implement
    return false;
}

// Bài 4: Bình phương của một số
// TODO: Tính bình phương của số n
int bai_4(int n) {
    // TODO: Implement
    return 0;
}

// Bài 5: Tính giá trị tuyệt đối
// TODO: Viết hàm tính giá trị tuyệt đối (không dùng abs())
int bai_5(int n) {
    // TODO: Implement
    return 0;
}

// ========== PHẦN 2: VÒNG LẶP ==========

// Bài 6: In từ 1 đến 10
// TODO: In các số từ 1 đến 10 trên cùng một dòng
void bai_6() {
    // TODO: Implement
}

// Bài 7: Tính tổng từ 1 đến n
// TODO: Tính tổng: 1 + 2 + 3 + ... + n
int bai_7(int n) {
    // TODO: Implement
    return 0;
}

// Bài 8: Bảng cửu chương
// TODO: In bảng cửu chương từ 1 đến 9
void bai_8() {
    // TODO: Implement
}

// Bài 9: Kiểm tra số nguyên tố
// TODO: Hàm trả về true nếu n là số nguyên tố
bool bai_9(int n) {
    // TODO: Implement
    return false;
}

// Bài 10: In hình tam giác
// TODO: In ra hình tam giác bằng dấu *
// Ví dụ với n=4:
// *
// **
// ***
// ****
void bai_10(int n) {
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= i; j++) {
            cout << "*";
        }
        cout << endl;
    }
}

// ========== PHẦN 3: CHUỖI (STRING) ==========

// Bài 11: Đảo ngược chuỗi
// TODO: Viết hàm đảo ngược một chuỗi
string bai_11(string s) {
    // TODO: Implement
    return "";
}

// Bài 12: Đếm số từ trong chuỗi
// TODO: Đếm số lượng từ trong một chuỗi
int bai_12(string s) {
    // TODO: Implement
    return 0;
}

// Bài 13: Kiểm tra chuỗi palindrome
// TODO: Kiểm tra xem chuỗi có phải palindrome không (nó với nó như nhau)
bool bai_13(string s) {
    // TODO: Implement
    return false;
}

// Bài 14: Chuyển chữ hoa/thường
// TODO: Viết hàm đảo ngược uppercase/lowercase của chuỗi
string bai_14(string s) {
    // TODO: Implement
    return "";
}

// Bài 15: Xóa khoảng trắng thừa
// TODO: Xóa các khoảng trắng thừa ở đầu, cuối và giữa chuỗi
string bai_15(string s) {
    // TODO: Implement
    return "";
}

// ========== PHẦN 4: DANH SÁCH (VECTOR) ==========

// Bài 16: Tìm phần tử lớn nhất
// TODO: Tìm số lớn nhất trong danh sách (không dùng max())
int bai_16(vector<int> lst) {
    // TODO: Implement
    return 0;
}

// Bài 17: Sắp xếp danh sách
// TODO: Sắp xếp danh sách theo thứ tự tăng dần (không dùng sort())
vector<int> bai_17(vector<int> lst) {
    // TODO: Implement
    return lst;
}

// Bài 18: Lọc số chẵn
// TODO: Trả về danh sách chỉ chứa các số chẵn
vector<int> bai_18(vector<int> lst) {
    // TODO: Implement
    return vector<int>();
}

// Bài 19: Gộp hai danh sách
// TODO: Ghép hai danh sách lại thành một
vector<int> bai_19(vector<int> lst1, vector<int> lst2) {
    // TODO: Implement
    return vector<int>();
}

// Bài 20: Loại bỏ phần tử trùng lặp
// TODO: Trả về danh sách mà không có phần tử trùng lặp
vector<int> bai_20(vector<int> lst) {
    // TODO: Implement
    return vector<int>();
}

// ========== PHẦN 5: TỪ ĐIỂN (MAP) ==========

// Bài 21: Tạo từ điển
// TODO: Tạo từ điển chứa thông tin cá nhân
map<string, string> bai_21() {
    // TODO: Implement
    return map<string, string>();
}

// Bài 22: Truy cập phần tử
// TODO: Viết hàm lấy giá trị từ từ điển (xử lý trường hợp khóa không tồn tại)
string bai_22(map<string, string> d, string key) {
    // TODO: Implement
    return "";
}

// Bài 23: Đếm tần số ký tự
// TODO: Đếm xem mỗi ký tự xuất hiện bao nhiêu lần trong chuỗi
map<char, int> bai_23(string s) {
    // TODO: Implement
    return map<char, int>();
}

// Bài 24: Gộp từ điển
// TODO: Gộp hai từ điển thành một
map<string, string> bai_24(map<string, string> d1, map<string, string> d2) {
    // TODO: Implement
    return map<string, string>();
}

// Bài 25: Sắp xếp từ điển
// TODO: Sắp xếp từ điển theo khóa hoặc giá trị
map<string, string> bai_25(map<string, string> d) {
    // TODO: Implement
    return d;
}

// ========== PHẦN 6: HÀM (FUNCTION) ==========

// Bài 26: Hàm có giá trị mặc định
// TODO: Viết hàm tính lũy thừa với giá trị mặc định là 2
int bai_26(int n, int power = 2) {
    // TODO: Implement
    return 0;
}

// Bài 27: Hàm với số lượng đối số không cố định
// TODO: Viết hàm tính tổng của nhiều số bất kỳ (dùng initializer_list hoặc vector)
int bai_27(initializer_list<int> args) {
    // TODO: Implement
    return 0;
}

// Bài 28: Hàm recursive (đệ quy)
// TODO: Tính giai thừa của n bằng đệ quy
int bai_28(int n) {
    // TODO: Implement
    return 0;
}

// Bài 29: Function pointer hoặc Lambda
// TODO: Dùng lambda để tính bình phương của các số trong danh sách
vector<int> bai_29(vector<int> lst) {
    // TODO: Implement
    return vector<int>();
}

// Bài 30: Transform và Filter
// TODO: Nhân mỗi số với 2, rồi lọc số >= 10
vector<int> bai_30(vector<int> lst) {
    // TODO: Implement
    return vector<int>();
}

// ========== PHẦN 7: FILE I/O ==========

// Bài 31: Đọc file
// TODO: Viết hàm đọc file và trả về nội dung
string bai_31(string filename) {
    // TODO: Implement
    return "";
}

// Bài 32: Ghi file
// TODO: Viết hàm ghi một danh sách vào file
void bai_32(string filename, vector<string> data) {
    // TODO: Implement
}

// Bài 33: Đếm dòng trong file
// TODO: Đếm số dòng trong một file
int bai_33(string filename) {
    // TODO: Implement
    return 0;
}

// Bài 34: Tìm từ trong file
// TODO: Tìm tất cả dòng chứa một từ cụ thể
vector<string> bai_34(string filename, string word) {
    // TODO: Implement
    return vector<string>();
}

// Bài 35: Sao chép file
// TODO: Sao chép nội dung từ file này sang file khác
void bai_35(string source, string destination) {
    // TODO: Implement
}

// ========== PHẦN 8: LỚP (CLASS) VÀ ĐỐI TƯỢNG ==========

// Bài 36: Tạo lớp
// TODO: Tạo lớp Person với thuộc tính name, age
class Person {
public:
    string name;
    int age;
    // TODO: Implement constructor and methods
};

// Bài 37: Phương thức
// TODO: Thêm phương thức introduce() để in ra thông tin
class Student {
public:
    string name;
    int age;
    // TODO: Implement methods
};

// Bài 38: Kế thừa
// TODO: Tạo lớp Employee kế thừa từ Person
class Employee : public Person {
public:
    // TODO: Implement
};

// Bài 39: Tính đa hình
// TODO: Tạo các lớp khác nhau và phương thức move() với hành vi khác nhau
class Animal {
public:
    virtual void move() {}
    // TODO: Implement
};

// Bài 40: Khóa cấp (Encapsulation)
// TODO: Tạo lớp BankAccount với thuộc tính private _balance
class BankAccount {
private:
    double balance;
public:
    // TODO: Implement getter/setter and methods
};

// ========== PHẦN 9: NÂNG CAO ==========

// Bài 41: Vector comprehension (tạo danh sách bình phương)
// TODO: Tạo danh sách bình phương của các số từ 1 đến 10
vector<int> bai_41() {
    // TODO: Implement
    return vector<int>();
}

// Bài 42: Generator (dãy số)
// TODO: Tạo dãy Fibonacci
vector<int> bai_42(int n) {
    // TODO: Implement
    return vector<int>();
}

// Bài 43: Decorator (decorator pattern)
// TODO: Viết decorator đo thời gian thực hiện hàm
void bai_43() {
    // TODO: Implement
}

// Bài 44: Exception handling
// TODO: Viết hàm chia hai số với xử lý lỗi
double bai_44(double a, double b) {
    // TODO: Implement
    return 0;
}

// Bài 45: JSON (dùng thư viện hoặc tạo string)
// TODO: Chuyển đổi giữa struct và JSON string
void bai_45() {
    // TODO: Implement (có thể dùng thư viện như nlohmann/json)
}

// ========== PHẦN 10: PROBLEM SOLVING ==========

// Bài 46: FizzBuzz
// TODO: In các số từ 1 đến 100, nhưng:
// - In "Fizz" nếu chia hết cho 3
// - In "Buzz" nếu chia hết cho 5
// - In "FizzBuzz" nếu chia hết cho cả 3 và 5
void bai_46() {
    // TODO: Implement
}

// Bài 47: Tìm cặp số có tổng bằng target
// TODO: Tìm hai số trong danh sách có tổng bằng target
pair<int, int> bai_47(vector<int> lst, int target) {
    // TODO: Implement
    return make_pair(-1, -1);
}

// Bài 48: Tìm số xuất hiện nhiều nhất
// TODO: Tìm số có tần suất xuất hiện cao nhất
int bai_48(vector<int> lst) {
    // TODO: Implement
    return 0;
}

// Bài 49: Nén chuỗi
// TODO: "aabbccdd" → "a2b2c2d2"
string bai_49(string s) {
    // TODO: Implement
    return "";
}

// Bài 50: Bài toán kinh điển
// TODO: Tìm 10 số Fibonacci đầu tiên
vector<int> bai_50() {
    // TODO: Implement
    return vector<int>();
}

// ========================================
// GỢI Ý KIỂM TRA KẾT QUẢ
// ========================================

int main() {
    cout << "==================================================" << endl;
    cout << "BÀI TẬP LUYỆN TẬP C++" << endl;
    cout << "==================================================" << endl;
    
    // Bài 1
    cout << "\nBài 1: In Hello C++" << endl;
    bai_1();
    
    // Bài 2
    cout << "\nBài 2: Tổng 5 + 3 = " << bai_2(5, 3) << endl;
    
    // Bài 3
    cout << "\nBài 3: 4 có chẵn không? " << (bai_3(4) ? "true" : "false") << endl;
    
    // Bài 6
    cout << "\nBài 6: Các số từ 1-10:" << endl;
    bai_6();
    
    // Bài 16
    vector<int> test_list = {3, 7, 2, 9, 1};
    cout << "\nBài 16: Số lớn nhất trong [3,7,2,9,1]: " << bai_16(test_list) << endl;
    
    return 0;
    // Thêm các test khác theo cần thiết
}