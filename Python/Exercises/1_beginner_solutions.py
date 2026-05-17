"""
ĐÁPIN - BÀI TẬP CƠ BẢN (BEGINNER SOLUTIONS)
=========================================
Hướng dẫn giải các bài tập cơ bản
"""

print("=" * 60)
print("ĐÁP ÁN - BÀI TẬP CƠ BẢN")
print("=" * 60)

# ===== BÀI 1.1: In thông tin cá nhân =====
print("\n[BÀI 1.1] In thông tin cá nhân")
print("-" * 40)

name = "Minh"
age = 25
city = "Hà Nội"

print(f"Tên: {name}")
print(f"Tuổi: {age}")
print(f"Thành phố: {city}")
print(f"\nThông tin: {name}, {age} tuổi, ở {city}")


# ===== BÀI 1.2: Tính diện tích hình chữ nhật =====
print("\n[BÀI 1.2] Tính diện tích hình chữ nhật")
print("-" * 40)

length = 10
width = 5
area = length * width
perimeter = 2 * (length + width)

print(f"Chiều dài: {length}")
print(f"Chiều rộng: {width}")
print(f"Diện tích: {area}")
print(f"Chu vi: {perimeter}")


# ===== BÀI 1.3: Chuyển đổi đơn vị =====
print("\n[BÀI 1.3] Chuyển đổi đơn vị")
print("-" * 40)

def km_to_m(km):
    return km * 1000

def m_to_cm(m):
    return m * 100

# Test
print(f"5 km = {km_to_m(5)} m")
print(f"2 m = {m_to_cm(2)} cm")
print(f"3 km = {km_to_m(3) * 100} cm")


# ===== BÀI 2.1: Kiểm tra số chẵn/lẻ =====
print("\n[BÀI 2.1] Kiểm tra số chẵn/lẻ")
print("-" * 40)

number = 7

if number % 2 == 0:
    print(f"{number} là số chẵn")
else:
    print(f"{number} là số lẻ")


# ===== BÀI 2.2: Tìm số lớn nhất =====
print("\n[BÀI 2.2] Tìm số lớn nhất")
print("-" * 40)

# Cách 1: Dùng if/elif
a, b, c = 10, 25, 15

if a >= b and a >= c:
    max_num = a
elif b >= a and b >= c:
    max_num = b
else:
    max_num = c

print(f"Cách 1 - Dùng if/elif: {max_num}")

# Cách 2: Dùng max()
max_num = max(a, b, c)
print(f"Cách 2 - Dùng max(): {max_num}")


# ===== BÀI 2.3: Xếp loại điểm =====
print("\n[BÀI 2.3] Xếp loại điểm")
print("-" * 40)

def grade_point(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "D"

# Test
scores = [95, 85, 75, 65, 45]
for score in scores:
    print(f"Điểm {score} → Xếp loại: {grade_point(score)}")


# ===== BÀI 2.4: Kiểm tra tuổi =====
print("\n[BÀI 2.4] Kiểm tra tuổi")
print("-" * 40)

def categorize_age(age):
    if age < 13:
        return "Trẻ em"
    elif age < 18:
        return "Thiếu niên"
    else:
        return "Người lớn"

# Test
ages = [10, 15, 20, 5, 35]
for age in ages:
    print(f"Tuổi {age} → {categorize_age(age)}")


# ===== BÀI 3.1: Bảng cửu chương =====
print("\n[BÀI 3.1] Bảng cửu chương")
print("-" * 40)

for i in range(1, 10):
    print(f"Bảng {i}:")
    for j in range(1, 10):
        print(f"  {i} × {j} = {i*j}")
    print()


# ===== BÀI 3.2: Tính tổng từ 1 đến N =====
print("\n[BÀI 3.2] Tính tổng từ 1 đến N")
print("-" * 40)

# Cách 1: Dùng for loop
n = 100
total = 0
for i in range(1, n+1):
    total += i
print(f"Cách 1 (for loop): Tổng 1 đến {n} = {total}")

# Cách 2: Dùng công thức
total_formula = n * (n + 1) // 2
print(f"Cách 2 (công thức): Tổng 1 đến {n} = {total_formula}")

# Cách 3: Dùng sum()
total_sum = sum(range(1, n+1))
print(f"Cách 3 (sum): Tổng 1 đến {n} = {total_sum}")


# ===== BÀI 3.3: Dãy Fibonacci =====
print("\n[BÀI 3.3] Dãy Fibonacci")
print("-" * 40)

# Cách 1: Dùng list
fib = [0, 1]
for i in range(2, 10):
    fib.append(fib[i-1] + fib[i-2])
print(f"Fibonacci: {fib}")

# Cách 2: Dùng loop
print("Fibonacci (10 số đầu):")
a, b = 0, 1
for _ in range(10):
    print(a, end=" ")
    a, b = b, a + b
print()


# ===== BÀI 3.4: Kiểm tra số nguyên tố =====
print("\n[BÀI 3.4] Kiểm tra số nguyên tố")
print("-" * 40)

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

# Test
test_numbers = [2, 3, 5, 7, 11, 13, 15, 17, 19, 20, 21]
primes = [n for n in test_numbers if is_prime(n)]
print(f"Số nguyên tố: {primes}")


# ===== BÀI 3.5: Hình sao =====
print("\n[BÀI 3.5] Hình sao")
print("-" * 40)

# Cách 1: Tam giác
print("Tam giác sao:")
for i in range(1, 6):
    print("*" * i)

# Cách 2: Hình thoi
print("\nHình thoi sao:")
n = 5
for i in range(1, n+1):
    print(" " * (n-i) + "*" * (2*i-1))
for i in range(n-1, 0, -1):
    print(" " * (n-i) + "*" * (2*i-1))


# ===== BÀI 4.1: Đếm ký tự =====
print("\n[BÀI 4.1] Đếm ký tự")
print("-" * 40)

text = "Hello Python World"
num_chars = len(text)
num_words = len(text.split())
spaces = text.count(" ")

print(f"Chuỗi: '{text}'")
print(f"Số ký tự: {num_chars}")
print(f"Số từ: {num_words}")
print(f"Số khoảng trắng: {spaces}")


# ===== BÀI 4.2: Đảo ngược chuỗi =====
print("\n[BÀI 4.2] Đảo ngược chuỗi")
print("-" * 40)

# Cách 1: Slicing
text = "Python"
reversed_text = text[::-1]
print(f"Chuỗi: {text}")
print(f"Đảo ngược: {reversed_text}")

# Cách 2: Loop
reversed_text2 = ""
for char in text:
    reversed_text2 = char + reversed_text2
print(f"Đảo ngược (loop): {reversed_text2}")


# ===== BÀI 4.3: Kiểm tra Palindrome =====
print("\n[BÀI 4.3] Kiểm tra Palindrome")
print("-" * 40)

def is_palindrome(text):
    clean = text.lower().replace(" ", "")
    return clean == clean[::-1]

# Test
test_strings = ["racecar", "hello", "A man a plan a canal Panama", "level"]
for s in test_strings:
    result = is_palindrome(s)
    print(f"'{s}' → {result}")


# ===== BÀI 4.4: Sắp xếp list =====
print("\n[BÀI 4.4] Sắp xếp list")
print("-" * 40)

numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# Cách 1: sort() (sửa đổi list gốc)
list1 = numbers.copy()
list1.sort()
print(f"Tăng dần (sort): {list1}")

# Cách 2: sorted() (trả về list mới)
list2 = sorted(numbers, reverse=True)
print(f"Giảm dần (sorted): {list2}")


# ===== BÀI 4.5: Tìm max/min =====
print("\n[BÀI 4.5] Tìm max/min (không dùng hàm max/min)")
print("-" * 40)

numbers = [45, 23, 78, 12, 95, 34]

# Cách 1: Loop
max_val = numbers[0]
min_val = numbers[0]

for num in numbers:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num

print(f"Danh sách: {numbers}")
print(f"Max: {max_val}")
print(f"Min: {min_val}")


print("\n" + "=" * 60)
print("✅ HẾT ĐÁPIN - BÀI TẬP CƠ BẢN")
print("=" * 60)
