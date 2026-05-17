"""
LESSON 2: CẤU TRÚC ĐIỀU KHIỂN (CONTROL FLOW)
==============================================
Mục tiêu: Hiểu if/elif/else, loop (for, while), và logic điều kiện

Nội dung:
1. If/Elif/Else statements
2. Toán tử logic (and, or, not)
3. While loop
4. For loop
5. Break, Continue, Pass
"""

# ===== 1. IF/ELIF/ELSE STATEMENTS =====

age = 18

# If statement
if age >= 18:
    print("Bạn đã trưởng thành")

# If/Else
if age < 18:
    print("Bạn là trẻ em")
else:
    print("Bạn là người lớn")

# If/Elif/Else (nhiều điều kiện)
if age < 13:
    status = "Trẻ em"
elif age < 18:
    status = "Thiếu niên"
elif age < 60:
    status = "Người lớn"
else:
    status = "Người già"

print(f"Trạng thái: {status}")

# Nested if (if lồng)
score = 75

if score >= 0:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    else:
        grade = "D"
    print(f"Điểm số: {grade}")


# ===== 2. TOÁN TỬ LOGIC =====

# and - cả hai điều kiện đều đúng
age = 25
income = 5000000

if age > 18 and income > 3000000:
    print("Đủ điều kiện vay tiền")  # In ra (True and True = True)

# or - ít nhất một điều kiện đúng
is_weekend = True
is_holiday = False

if is_weekend or is_holiday:
    print("Hôm nay không cần đi làm")  # In ra (True or False = True)

# not - phủ định
is_raining = False

if not is_raining:
    print("Thời tiết đẹp")  # In ra (not False = True)

# Kết hợp nhiều logic
temp = 25
humidity = 60
is_comfortable = (20 <= temp <= 30) and (40 <= humidity <= 70)
print(f"Thời tiết thoải mái: {is_comfortable}")  # True


# ===== 3. WHILE LOOP =====

print("\n=== WHILE LOOP ===")

# While loop cơ bản
count = 0
while count < 5:
    print(f"Count: {count}")
    count = count + 1  # hoặc count += 1

# While loop với điều kiện phức tạp
n = 5
factorial = 1
while n > 1:
    factorial *= n
    n -= 1
print(f"5! = {factorial}")

# While True (loop vô tận)
counter = 0
while True:
    print(f"Iteration: {counter}")
    counter += 1
    if counter >= 3:
        break  # Thoát khỏi loop
print("Loop dừng")


# ===== 4. FOR LOOP =====

print("\n=== FOR LOOP ===")

# For loop cơ bản với range()
for i in range(5):
    print(f"i = {i}")

# Range với start, stop, step
for i in range(1, 10, 2):  # Từ 1 đến 9, bước 2
    print(i)  # In: 1, 3, 5, 7, 9

# For loop với list
fruits = ["táo", "cam", "chuối"]
for fruit in fruits:
    print(f"Quả: {fruit}")

# For loop với string
for char in "Python":
    print(char)

# For loop với enumerate (lấy cả index)
students = ["An", "Bình", "Chi"]
for index, student in enumerate(students):
    print(f"{index}: {student}")

# For loop với dict
scores = {"Minh": 90, "Hùng": 85, "Trang": 95}
for name, score in scores.items():
    print(f"{name}: {score}")

# For loop với range(len())
items = ["A", "B", "C"]
for i in range(len(items)):
    print(f"Index {i}: {items[i]}")


# ===== 5. BREAK, CONTINUE, PASS =====

print("\n=== BREAK, CONTINUE, PASS ===")

# Break - thoát khỏi loop
for i in range(10):
    if i == 5:
        break  # Dừng loop khi i = 5
    print(i)  # In: 0 1 2 3 4

print()

# Continue - bỏ qua phần còn lại của iteration hiện tại
for i in range(5):
    if i == 2:
        continue  # Bỏ qua i = 2
    print(i)  # In: 0 1 3 4

print()

# Pass - làm không có gì (placeholder)
for i in range(3):
    if i == 1:
        pass  # Không làm gì
    print(i)  # In: 0 1 2

# Pass thường dùng với if
if True:
    pass  # Để placeholder, làm sau


# ===== THỰC HÀNH =====

print("\n=== THỰC HÀNH ===")

# Bài 1: Tìm số chẵn từ 1 đến 20
print("Số chẵn:")
for num in range(1, 21):
    if num % 2 == 0:
        print(num, end=" ")
print()

# Bài 2: Tính tổng từ 1 đến 100
total = 0
for i in range(1, 101):
    total += i
print(f"Tổng 1-100: {total}")

# Bài 3: Tìm ký tự trong chuỗi
text = "Hello"
search = "l"
count = 0
for char in text:
    if char == search:
        count += 1
print(f"Ký tự '{search}' xuất hiện {count} lần")

# Bài 4: FizzBuzz problem
print("\nFizzBuzz:")
for i in range(1, 16):
    if i % 15 == 0:
        print("FizzBuzz", end=" ")
    elif i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")


# ===== NESTED LOOP =====

print("\n\n=== NESTED LOOP ===")

# Bảng cửu chương 2x2
for i in range(1, 3):
    for j in range(1, 3):
        print(f"{i}x{j}={i*j}", end="  ")
    print()  # Xuống dòng

print("\nHình tam giác:")
for i in range(1, 5):
    print("*" * i)

print("\nHình chữ nhật:")
for i in range(3):
    for j in range(5):
        print("█", end="")
    print()


print("\n=== HẾT LESSON 2 ===")
