"""
LESSON 1: GIỚI THIỆU & CƠ BẢN PYTHON
=====================================
Mục tiêu: Hiểu cú pháp cơ bản, biến, kiểu dữ liệu và output

Nội dung:
1. Print statement
2. Biến & Gán giá trị
3. Kiểu dữ liệu cơ bản
4. Phép toán cơ bản
5. Comments
"""

# ===== 1. PRINT STATEMENT =====
# Hàm print() để in ra màn hình console
print("Hello, Python!")
print("Đây là lập trình Python")

# In nhiều thứ cùng một lúc
print("Số:", 42)
print("Tên tôi là", "Việt Nam")

# In với dấu cách tùy chỉnh
print("Python", "là", "tuyệt vời", sep=" - ")

# In mà không xuống dòng
print("Hello", end=" ")
print("World")  # Sẽ in "Hello World" trên cùng một dòng


# ===== 2. BIẾN & GÁN GIÁ TRỊ =====
# Biến = tên + giá trị lưu trữ

# Gán giá trị
age = 25
name = "Minh"
height = 1.75
is_student = True

print(age)
print(name)
print(height)
print(is_student)

# Gán nhiều biến cùng lúc
x, y, z = 1, 2, 3
print(x, y, z)

# Gán cùng giá trị cho nhiều biến
a = b = c = 10
print(a, b, c)


# ===== 3. KIỂU DỮ LIỆU (DATA TYPES) =====

# Integer (Số nguyên)
num1 = 42
num2 = -15
print(type(num1))  # <class 'int'>

# Float (Số thực)
num3 = 3.14
num4 = -2.5
print(type(num3))  # <class 'float'>

# String (Chuỗi ký tự)
text1 = "Hello"
text2 = 'Python'
text3 = """Đây là 
chuỗi nhiều dòng"""
print(type(text1))  # <class 'str'>

# Boolean (Đúng/Sai)
is_active = True
is_deleted = False
print(type(is_active))  # <class 'bool'>

# None (Giá trị rỗng)
result = None
print(type(result))  # <class 'NoneType'>


# ===== 4. PHÉP TOÁN CƠ BẢN =====

# Cộng, Trừ, Nhân, Chia
a = 10
b = 3

print(a + b)    # 13
print(a - b)    # 7
print(a * b)    # 30
print(a / b)    # 3.3333... (chia lấy số thực)
print(a // b)   # 3 (chia lấy phần nguyên)
print(a % b)    # 1 (lấy phần dư)
print(a ** b)   # 1000 (lũy thừa)

# Toán học với string
text = "Python"
print(text + " 3")      # Ghép chuỗi
print(text * 3)         # Lặp lại chuỗi

# So sánh
print(5 > 3)     # True
print(5 < 3)     # False
print(5 == 5)    # True (bằng)
print(5 != 3)    # True (không bằng)
print(5 >= 5)    # True
print(5 <= 4)    # False


# ===== 5. COMMENTS (GHI CHÚ) =====

# Đây là comment một dòng
print("Code")  # Comment ở cuối dòng

"""
Đây là comment 
nhiều dòng
"""


# ===== THỰC HÀNH =====
print("\n=== THỰC HÀNH ===")

# Bài 1: In thông tin của bạn
name = "Tôi"
age = 25
country = "Việt Nam"

print(f"Tên: {name}")
print(f"Tuổi: {age}")
print(f"Quốc gia: {country}")

# Bài 2: Tính toán
price = 100000
quantity = 5
total = price * quantity
print(f"Tổng tiền: {total}")

# Bài 3: Kiểm tra kiểu
value = 42
print(f"Value: {value}, Type: {type(value)}")


# ===== KEYWORD ĐẶC BIỆT =====
# Keywords là từ khóa dành riêng cho Python
# Ví dụ: if, else, for, while, def, class, import, True, False, None

# Không được dùng keywords làm tên biến
# if = 5  # ❌ Lỗi!
# class = "A"  # ❌ Lỗi!

value = 5  # ✅ OK
Class = "A"  # ✅ OK (khác với class)


# ===== NAMING CONVENTION =====
# Quy tắc đặt tên biến:
# - Bắt đầu bằng chữ hoặc _
# - Chứa chữ, số, _
# - Không chứa khoảng trắng
# - Phân biệt hoa/thường

student_name = "Hùng"  # ✅ snake_case (khuyến khích)
studentName = "Hùng"   # ✅ camelCase (có thể dùng)
StudentName = "Hùng"   # ✅ PascalCase (cho class)
CONSTANT = 3.14        # ✅ UPPER_CASE (cho hằng số)


print("\n=== HẾT LESSON 1 ===")
