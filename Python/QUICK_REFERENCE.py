"""
QUICK REFERENCE GUIDE - HƯỚNG DẪN NHANH PYTHON
==============================================
Tham khảo nhanh các cú pháp và khái niệm Python
"""

print("=" * 80)
print("QUICK REFERENCE - PYTHON")
print("=" * 80)

# ===== BIẾN & KIỂU DỮ LIỆU =====
print("\n[1] BIẾN & KIỂU DỮ LIỆU")
print("-" * 80)

reference = """
INT (Số nguyên):           x = 42
FLOAT (Số thực):           y = 3.14
STRING (Chuỗi):            name = "Python"
BOOLEAN (Đúng/Sai):        is_active = True
NONE (Rỗng):               result = None
LIST (Danh sách):          items = [1, 2, 3]
TUPLE (Bộ không đổi):      point = (10, 20)
DICTIONARY (Từ điển):      data = {"key": "value"}
SET (Tập hợp):             unique = {1, 2, 3}

Kiểm tra kiểu:             type(x)
Chuyển đổi kiểu:           int("42"), str(42), float("3.14")
"""
print(reference)


# ===== TOÁN TỬ =====
print("[2] TOÁN TỬ")
print("-" * 80)

operators = """
CỘng:          +      a + b
TRỪ:           -      a - b
NHÂN:          *      a * b
ChIA:          /      a / b (số thực)
ChIA LẤYPHẦN NGUYÊN:   //   a // b
LẤY PHẦN DƯ:   %      a % b
LŨY THỪA:      **     a ** b

SO SÁNH:
=== Bằng           ==    a == b
!= Không bằng      !=    a != b
> Lớn hơn          >     a > b
< Nhỏ hơn          <     a < b
>= Lớn hơn bằng    >=    a >= b
<= Nhỏ hơn bằng    <=    a <= b

Logic:
VÀ:         and    a and b
HOẶC:       or     a or b
PHỦ ĐỊNH:   not    not a

GÁN:
Gán bình thường:   x = 5
Gán vội (+= -= *=...): x += 3  tương đương x = x + 3
"""
print(operators)


# ===== CẤU TRÚC ĐIỀU KHIỂN =====
print("[3] CẤU TRÚC ĐIỀU KHIỂN")
print("-" * 80)

control = """
IF/ELIF/ELSE:
    if condition:
        # code
    elif condition2:
        # code
    else:
        # code

WHILE LOOP:
    while condition:
        # code
        break      # Thoát loop
        continue   # Bỏ qua phần còn lại, vào vòng tiếp

FOR LOOP:
    for i in range(10):
        # code
    
    for item in list:
        # code
    
    for i, item in enumerate(list):
        # i là index, item là giá trị

TERNARY (Ba ngôi):
    x = a if condition else b
"""
print(control)


# ===== HÀM =====
print("[4] HÀM")
print("-" * 80)

functions = """
ĐịNH NGHĨA:
    def function_name(param1, param2):
        '''Docstring (mô tả hàm)'''
        return result

KIỂU PARAMETER:
    Positional:         def func(a, b)
    Default:            def func(a, b=10)
    *args:              def func(*args) - số lượng bất định
    **kwargs:           def func(**kwargs) - keyword arguments
    Kết hợp:            def func(a, *args, **kwargs)

GỌIHÀM:
    func(1, 2)                  # Positional
    func(a=1, b=2)             # Keyword
    func(1, b=2)                # Mix
    func(1, 2, 3)               # *args
    func(a=1, b=2, c=3)        # **kwargs

LAMBDA (Hàm vô danh):
    lambda x: x ** 2
    lambda x, y: x + y
    numbers = [1,2,3]
    squared = list(map(lambda x: x**2, numbers))
"""
print(functions)


# ===== CHUỖI (STRING) =====
print("[5] CHUỖI (STRING)")
print("-" * 80)

strings = """
CÁC CÁCH TẠO:
    s1 = "chuỗi đơn"
    s2 = 'chuỗi đơn'
    s3 = '''chuỗi
    nhiều dòng'''

INDEXING:
    s = "Python"
    s[0] → 'P'
    s[-1] → 'n'
    s[1:4] → 'yth'
    s[::2] → 'Pto'
    s[::-1] → 'nohtyP'

METHODS:
    len(s)              → Độ dài
    s.lower()           → Chữ thường
    s.upper()           → Chữ hoa
    s.strip()           → Loại khoảng trắng
    s.replace(a, b)     → Thay thế
    s.split()           → Tách chuỗi
    s.join(list)        → Nối danh sách
    s.find(substring)   → Tìm vị trí
    s.startswith(prefix) → Kiểm tra bắt đầu
    s.endswith(suffix)  → Kiểm tra kết thúc

F-STRING:
    name = "Minh"
    age = 25
    print(f"Tên: {name}, Tuổi: {age}")
    print(f"Năm: {2024 + 1}")
"""
print(strings)


# ===== LIST & DICTIONARY =====
print("[6] LIST & DICTIONARY")
print("-" * 80)

data_structures = """
LIST:
    items = [1, 2, 3, 4, 5]
    items[0] → 1
    items[-1] → 5
    items[1:3] → [2, 3]
    
    append(x)       → Thêm cuối
    insert(i, x)    → Chèn vào vị trí i
    remove(x)       → Xóa phần tử x
    pop(i)          → Xóa vị trí i
    sort()          → Sắp xếp
    reverse()       → Đảo ngược
    len()           → Độ dài
    sum()           → Tổng
    max(), min()    → Max, min

DICTIONARY:
    data = {"key": "value", "age": 25}
    data["key"] → "value"
    data.get("age", 0) → 25 (có default)
    
    data["new_key"] = "new_value"  → Thêm
    del data["key"]                → Xóa
    data.keys()    → Danh sách key
    data.values()  → Danh sách value
    data.items()   → Cặp key-value
    
    for key, value in data.items():
        print(key, value)

LIST COMPREHENSION:
    squares = [x**2 for x in range(5)]  → [0, 1, 4, 9, 16]
    evens = [x for x in range(10) if x%2==0]  → [0, 2, 4, 6, 8]
"""
print(data_structures)


# ===== FILE I/O =====
print("[7] FILE I/O - ĐỌC/GHI FILE")
print("-" * 80)

file_io = """
ĐỌC FILE:
    with open("file.txt", "r") as f:
        content = f.read()      → Đọc toàn bộ
        # hoặc
        lines = f.readlines()   → Đọc từng dòng
        # hoặc
        for line in f:
            print(line)

GHI FILE:
    with open("file.txt", "w") as f:
        f.write("Hello")        → Ghi toàn bộ
        # hoặc
        f.writelines(["A", "B"]) → Ghi danh sách

MỞ FILE:
    "r"  → Đọc (mặc định)
    "w"  → Ghi (xóa nếu tồn tại)
    "a"  → Thêm (append)
    "r+" → Đọc và ghi

KIỂM TRA FILE:
    import os
    os.path.exists("file.txt")  → True/False
    os.path.isfile("file.txt")  → True/False
    os.path.isdir("folder")     → True/False
"""
print(file_io)


# ===== EXCEPTION HANDLING =====
print("[8] EXCEPTION HANDLING - XỬ LÝ LỖI")
print("-" * 80)

exceptions = """
TRY/EXCEPT:
    try:
        x = int("abc")  # Sẽ lỗi
    except ValueError:
        print("Lỗi: nhập số không hợp lệ")
    except Exception as e:
        print(f"Lỗi: {e}")
    else:
        print("Không có lỗi")  # Chạy nếu không lỗi
    finally:
        print("Luôn chạy")

RAISE (Ném lỗi):
    if value < 0:
        raise ValueError("Value phải >= 0")

COMMON EXCEPTIONS:
    ValueError         → Giá trị không hợp lệ
    TypeError          → Kiểu dữ liệu không đúng
    ZeroDivisionError  → Chia cho 0
    IndexError         → Index ngoài phạm vi
    KeyError           → Key không tồn tại
    FileNotFoundError  → File không tồn tại
    ImportError        → Module không tìm thấy
"""
print(exceptions)


# ===== IMPORTS & MODULES =====
print("[9] IMPORTS & MODULES")
print("-" * 80)

imports = """
IMPORT MODULE:
    import os                      → Import toàn bộ
    import os as operating_system  → Đặt alias
    from os import path            → Import một phần
    from os import path, getcwd    → Import nhiều
    from os import *               → Import tất cả (không khuyến khích)

VỊ TRỊ MODULE:
    import sys
    print(sys.path)     → Tìm kiếm module ở đây

KIỂM TRA:
    import os
    dir(os)             → Liệt kê attributes/functions
    help(os.getcwd)     → Trợ giúp
"""
print(imports)


# ===== CLASS & OOP =====
print("[10] CLASS & OOP")
print("-" * 80)

oop = """
TẠO CLASS:
    class ClassName:
        class_var = "tôi là class variable"
        
        def __init__(self, param):
            self.param = param      # Instance variable
        
        def method(self):
            return self.param

INHERITANCE:
    class Parent:
        pass
    
    class Child(Parent):
        def __init__(self, param):
            super().__init__()      # Gọi parent constructor
        
        def method(self):           # Override
            return super().method() # Gọi parent method

SPECIAL METHODS:
    __init__(self)      → Constructor
    __str__(self)       → Gọi khi print()
    __repr__(self)      → Biểu diễn code
    __len__(self)       → Gọi khi len()
    __eq__(self, other) → So sánh ==
    __lt__(self, other) → So sánh <
    __add__(self, other) → Cộng +
    __call__(self)      → Gọi object như hàm

PROPERTY:
    @property
    def attr(self):
        return self._attr
    
    @attr.setter
    def attr(self, value):
        self._attr = value
"""
print(oop)


# ===== DECORATORS =====
print("[11] DECORATORS")
print("-" * 80)

decorators = """
ĐỊnH NGHĨA:
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            print("Before")
            result = func(*args, **kwargs)
            print("After")
            return result
        return wrapper
    
    @my_decorator
    def hello():
        print("Hello")

BUILT-IN DECORATORS:
    @staticmethod       → Không dùng self
    @classmethod        → Dùng cls thay vì self
    @property           → Thuộc tính giống method
"""
print(decorators)


# ===== TIPS & BEST PRACTICES =====
print("[12] TIPS & BEST PRACTICES")
print("-" * 80)

tips = """
CODE STYLE:
    ✓ snake_case cho biến, function:     my_variable, my_function()
    ✓ PascalCase cho class:              MyClass
    ✓ UPPER_CASE cho hằng số:            MAX_SIZE = 100
    ✓ Dùng 4 spaces để indent (không tab)
    ✓ Dòng tối đa 79 ký tự

NAMING:
    ✓ Tên có ý nghĩa:              student_age (không a, x)
    ✓ Tránh từ khóa Python:        không dùng if, class làm tên
    ✓ Private attribute:           _private_attr

COMMENTS:
    ✓ Giải thích TẠI SAO, không ĐIỀU GÌ
    ✓ Dùng docstring cho hàm/class:
        def func():
            '''Mô tả hàm'''
    
    ✓ Tránh comments quá dài:     tối đa 72 ký tự

FUNCTIONS:
    ✓ Một hàm = một nhiệm vụ
    ✓ Độc lập, có thể reuse
    ✓ Tính pure function (không thay đổi state)
    ✓ Xử lý error/exception

PERFORMANCE:
    ✓ List comprehension > loop
    ✓ dict lookup nhanh hơn list search
    ✓ Dùng generator cho dữ liệu lớn
    ✓ Tránh global variable
"""
print(tips)


# ===== DEBUGGING =====
print("[13] DEBUGGING - SỬA BỔ LỖI")
print("-" * 80)

debugging = """
PRINT DEBUG:
    print(f"Debug: x={x}")
    print(f"Type: {type(x)}")

BUILT-IN FUNCTIONS:
    type(x)         → Kiểu dữ liệu
    isinstance(x, int) → Kiểm tra kiểu
    dir(object)     → Liệt kê attributes
    help(function)  → Trợ giúp

PDB (Python Debugger):
    import pdb
    pdb.set_trace()  # Dừng tại đây
    # hoặc
    breakpoint()     # Python 3.7+

ASSERTIONS (Khẳng định):
    assert x > 0, "x phải > 0"
    assert isinstance(x, int), "x phải là số"
"""
print(debugging)


print("\n" + "=" * 80)
print("✅ HẾT QUICK REFERENCE")
print("=" * 80)

print("""

📚 TÀI LIỆU CHỈ DẪN:
   - Python Official Docs: https://docs.python.org/
   - PEP 8 Style Guide: https://pep8.org/
   - Real Python: https://realpython.com/
   - W3Schools Python: https://www.w3schools.com/python/
   - GeeksforGeeks Python: https://www.geeksforgeeks.org/python/

🎯 LUYỆN TẬP:
   - LeetCode: https://leetcode.com/
   - HackerRank: https://www.hackerrank.com/
   - Codewars: https://www.codewars.com/
   - Project Euler: https://projecteuler.net/

💻 IDE & TOOLS:
   - VS Code với Python extension
   - PyCharm Community
   - Jupyter Notebook (thực hành data science)
   - Thonny (cho beginners)

Chúc bạn học tập thành công! 🚀
""")
