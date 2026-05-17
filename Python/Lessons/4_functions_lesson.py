"""
LESSON 4: HÀM (FUNCTIONS)
========================
Mục tiêu: Hiểu cách viết hàm, parameter, return values, và scope

Nội dung:
1. Định nghĩa hàm
2. Parameter & Arguments
3. Return values
4. Default & Keyword arguments
5. *args & **kwargs
6. Lambda functions
7. Scope
"""

# ===== 1. ĐỊNH NGHĨA HÀM =====
print("=== HÀM CƠ BẢN ===\n")

# Hàm đơn giản
def greet():
    print("Xin chào!")

greet()  # Gọi hàm

# Hàm với parameter (tham số)
def greet_person(name):
    print(f"Xin chào, {name}!")

greet_person("Minh")
greet_person("Hùng")

# Hàm với return
def add(a, b):
    result = a + b
    return result

sum_result = add(5, 3)
print(f"Kết quả: {sum_result}")

# Multiple return values (trả về tuple)
def get_name_and_age():
    return "Minh", 25

name, age = get_name_and_age()
print(f"Tên: {name}, Tuổi: {age}")


# ===== 2. PARAMETER & ARGUMENTS =====
print("\n=== PARAMETER & ARGUMENTS ===\n")

# Positional arguments (theo vị trí)
def subtract(a, b):
    return a - b

print(f"10 - 3 = {subtract(10, 3)}")

# Keyword arguments (theo tên)
print(f"3 - 10 = {subtract(b=10, a=3)}")

# Mix positional & keyword
def create_profile(name, age, city):
    return f"{name} {age} tuổi ở {city}"

print(create_profile("An", 20, "Hà Nội"))
print(create_profile("An", city="TPHCM", age=20))  # Keyword có thể khác thứ tự


# ===== 3. DEFAULT ARGUMENTS =====
print("\n=== DEFAULT ARGUMENTS ===\n")

def greet_with_default(name, greeting="Xin chào"):
    return f"{greeting}, {name}!"

print(greet_with_default("Minh"))  # Dùng default greeting
print(greet_with_default("Hùng", "Hi"))  # Override default

# Hàm với nhiều default
def introduce(name, age=18, city="Hà Nội"):
    return f"{name}, {age} tuổi, ở {city}"

print(introduce("An"))
print(introduce("Bình", 25))
print(introduce("Chi", 22, "TPHCM"))


# ===== 4. *ARGS (VARIADIC POSITIONAL ARGUMENTS) =====
print("\n=== *ARGS ===\n")

# Nhận số lượng argument không xác định
def sum_all(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_all(1, 2, 3))          # 6
print(sum_all(1, 2, 3, 4, 5))    # 15
print(sum_all(10))               # 10

# Sử dụng sum()
def sum_all_v2(*numbers):
    return sum(numbers)

print(sum_all_v2(5, 10, 15))  # 30

# Hàm với parameter bình thường + *args
def print_info(name, *hobbies):
    print(f"Tên: {name}")
    print("Sở thích:")
    for hobby in hobbies:
        print(f"  - {hobby}")

print_info("Minh", "đọc sách", "chơi game", "đi du lịch")


# ===== 5. **KWARGS (VARIADIC KEYWORD ARGUMENTS) =====
print("\n=== **KWARGS ===\n")

# Nhận keyword arguments không xác định
def print_person(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

print_person(name="Minh", age=25, city="Hà Nội")
print_person(product="Laptop", price=15000000, brand="Dell")

# Kết hợp *args & **kwargs
def describe(name, *skills, **info):
    print(f"Tên: {name}")
    print(f"Kỹ năng: {skills}")
    print(f"Thông tin: {info}")

describe("An", "Python", "JavaScript", age=20, city="HCM")


# ===== 6. LAMBDA FUNCTIONS (HÀM ẨNdanh) =====
print("\n=== LAMBDA FUNCTIONS ===\n")

# Lambda = hàm vô danh, một dòng
add_lambda = lambda x, y: x + y
print(f"3 + 5 = {add_lambda(3, 5)}")

# Lambda với map()
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(f"Bình phương: {squared}")

# Lambda với filter()
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Số chẵn: {evens}")

# Lambda với sorted()
data = [("An", 90), ("Bình", 85), ("Chi", 95)]
sorted_data = sorted(data, key=lambda x: x[1])
print(f"Sắp xếp theo điểm: {sorted_data}")


# ===== 7. SCOPE (PHẠM VỊ BIẾN) =====
print("\n=== SCOPE ===\n")

# Global scope
global_var = "Tôi là biến global"

def func1():
    # Local scope
    local_var = "Tôi là biến local"
    print(local_var)
    print(global_var)

func1()
# print(local_var)  # ❌ Lỗi - local_var không tồn tại ở đây

# Sửa biến global
counter = 0

def increment():
    global counter
    counter += 1
    print(f"Counter: {counter}")

increment()
increment()
increment()

# Nonlocal (cho nested functions)
def outer():
    value = 10
    
    def inner():
        nonlocal value
        value += 5
        print(f"Inner: {value}")
    
    inner()
    print(f"Outer: {value}")

outer()


# ===== DOCSTRINGS =====
print("\n=== DOCSTRINGS ===\n")

def calculate_area(radius):
    """
    Tính diện tích hình tròn.
    
    Parameters:
        radius (float): Bán kính hình tròn
    
    Returns:
        float: Diện tích hình tròn
    """
    import math
    return math.pi * radius ** 2

print(f"Diện tích với r=5: {calculate_area(5):.2f}")
print(calculate_area.__doc__)  # In docstring


# ===== THỰC HÀNH =====
print("\n=== THỰC HÀNH ===\n")

# Bài 1: Hàm tính giai thừa
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(f"5! = {factorial(5)}")

# Bài 2: Hàm kiểm tra số nguyên tố
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(f"7 là số nguyên tố: {is_prime(7)}")
print(f"10 là số nguyên tố: {is_prime(10)}")

# Bài 3: Hàm chuyển đổi nhiệt độ
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

temp_c = 25
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f:.1f}°F")

# Bài 4: Hàm với default & *args
def create_list(default_value=0, *items):
    result = [default_value] + list(items)
    return result

print(create_list())
print(create_list(99, 1, 2, 3))

# Bài 5: Decorator (hàm bao bọc hàm khác)
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Trước khi gọi hàm")
        result = func(*args, **kwargs)
        print("Sau khi gọi hàm")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Xin chào, {name}!")
    return "Done"

say_hello("Minh")


print("\n=== HẾT LESSON 4 ===")
