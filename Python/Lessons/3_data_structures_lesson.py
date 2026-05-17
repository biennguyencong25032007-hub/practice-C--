"""
LESSON 3: CẤU TRÚC DỮ LIỆU (DATA STRUCTURES)
=============================================
Mục tiêu: Hiểu List, Tuple, Dictionary, Set và các method của chúng

Nội dung:
1. List (Danh sách)
2. Tuple (Bộ dữ liệu bất biến)
3. Dictionary (Từ điển)
4. Set (Tập hợp)
5. Slicing và Methods
"""

# ===== 1. LIST (DANH SÁCH) =====
print("=== LIST ===\n")

# Tạo list
numbers = [1, 2, 3, 4, 5]
fruits = ["táo", "cam", "chuối"]
mixed = [1, "hello", 3.14, True]
empty = []

print(f"Numbers: {numbers}")
print(f"Type: {type(numbers)}")

# Truy cập phần tử (indexing)
print(f"Phần tử đầu: {numbers[0]}")
print(f"Phần tử cuối: {numbers[-1]}")
print(f"Phần tử thứ 2: {numbers[1]}")

# Độ dài list
print(f"Độ dài: {len(numbers)}")

# Thay đổi phần tử
numbers[0] = 10
print(f"Sau khi thay đổi: {numbers}")

# Add phần tử
numbers.append(6)
print(f"Sau append: {numbers}")

# Insert vào vị trí cụ thể
numbers.insert(0, 0)
print(f"Sau insert: {numbers}")

# Remove phần tử
numbers.remove(6)
print(f"Sau remove: {numbers}")

# Pop (xóa theo index, mặc định cuối cùng)
last = numbers.pop()
print(f"Pop ra: {last}, List còn: {numbers}")

# Extend (thêm nhiều phần tử)
numbers.extend([7, 8, 9])
print(f"Sau extend: {numbers}")

# Sắp xếp
scores = [85, 92, 78, 95, 88]
scores.sort()
print(f"Sorted: {scores}")

# Đảo ngược
scores.reverse()
print(f"Reversed: {scores}")

# Index (tìm vị trí)
pos = fruits.index("cam")
print(f"Vị trí 'cam': {pos}")

# Count (đếm phần tử)
data = [1, 2, 2, 3, 2, 4]
print(f"Số lần '2' xuất hiện: {data.count(2)}")

# Copy list
original = [1, 2, 3]
copy_list = original.copy()
copy_list[0] = 999
print(f"Original: {original}, Copy: {copy_list}")

# Clear
temp_list = [1, 2, 3]
temp_list.clear()
print(f"After clear: {temp_list}")


# ===== 2. TUPLE (BỘ DỮ LIỆU BẤT BIẾN) =====
print("\n=== TUPLE ===\n")

# Tạo tuple
point = (10, 20)
colors = ("red", "green", "blue")
single = (42,)  # Phải có dấu phẩy
empty_tuple = ()

print(f"Point: {point}")
print(f"Type: {type(point)}")

# Truy cập
print(f"X: {point[0]}, Y: {point[1]}")

# Không thể thay đổi (immutable)
# point[0] = 30  # ❌ Lỗi!

# Unpacking
x, y = point
print(f"Unpacked: x={x}, y={y}")

a, b, c = colors
print(f"Colors: {a}, {b}, {c}")

# Length
print(f"Độ dài tuple colors: {len(colors)}")

# Count & Index
data_tuple = (1, 2, 2, 3, 2)
print(f"Count 2: {data_tuple.count(2)}")
print(f"Index 3: {data_tuple.index(3)}")


# ===== 3. DICTIONARY (TỪ ĐIỂN) =====
print("\n=== DICTIONARY ===\n")

# Tạo dictionary
student = {"name": "Minh", "age": 20, "score": 85}
empty_dict = {}
scores_dict = {
    "An": 90,
    "Bình": 85,
    "Chi": 95
}

print(f"Student: {student}")
print(f"Type: {type(student)}")

# Truy cập giá trị
print(f"Name: {student['name']}")
print(f"Age: {student.get('age')}")

# Thêm key-value
student['city'] = "Hà Nội"
print(f"After adding city: {student}")

# Cập nhật giá trị
student['age'] = 21
print(f"After updating age: {student}")

# Xóa key
del student['city']
# hoặc
# student.pop('city')
print(f"After deleting city: {student}")

# Các method quan trọng
print(f"Keys: {student.keys()}")
print(f"Values: {student.values()}")
print(f"Items: {student.items()}")

# Loop qua dictionary
print("\nLoop qua dictionary:")
for key, value in student.items():
    print(f"  {key}: {value}")

# Check key có tồn tại không
if "name" in student:
    print("'name' tồn tại")

# Get với default value
job = student.get('job', 'Unknown')
print(f"Job: {job}")

# Update dictionary
student.update({"job": "Student", "city": "TPHCM"})
print(f"After update: {student}")


# ===== 4. SET (TẬP HỢP) =====
print("\n=== SET ===\n")

# Tạo set (không có thứ tự, không trùng lặp)
numbers_set = {1, 2, 3, 4, 5}
colors_set = {"red", "green", "blue"}
empty_set = set()  # Không dùng {}

print(f"Set: {numbers_set}")
print(f"Type: {type(numbers_set)}")

# Add phần tử
numbers_set.add(6)
print(f"After add: {numbers_set}")

# Remove
numbers_set.remove(6)
# hoặc discard (không lỗi nếu không tồn tại)
print(f"After remove: {numbers_set}")

# Lấy set mới từ list (loại bỏ trùng lặp)
data = [1, 2, 2, 3, 3, 3, 4]
unique = set(data)
print(f"Unique: {unique}")

# Set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print(f"Union (hợp): {set_a | set_b}")
print(f"Intersection (giao): {set_a & set_b}")
print(f"Difference (hiệu): {set_a - set_b}")

# Check membership
if 3 in set_a:
    print("3 có trong set_a")


# ===== 5. SLICING (CẮT CHUỖI) =====
print("\n=== SLICING ===\n")

text = "Python"
items = [0, 1, 2, 3, 4, 5]

# Syntax: sequence[start:stop:step]
print(f"text[0:3]: {text[0:3]}")        # 'Pyt' (0,1,2)
print(f"text[3:]: {text[3:]}")          # 'hon' (từ 3 đến cuối)
print(f"text[:3]: {text[:3]}")          # 'Pyt' (từ đầu đến 3)
print(f"text[::2]: {text[::2]}")        # 'Pto' (bước 2)
print(f"text[::-1]: {text[::-1]}")      # 'nohtyP' (đảo ngược)

print(f"items[1:4]: {items[1:4]}")      # [1, 2, 3]
print(f"items[::2]: {items[::2]}")      # [0, 2, 4]
print(f"items[::-1]: {items[::-1]}")    # [5, 4, 3, 2, 1, 0]


# ===== THỰC HÀNH =====
print("\n=== THỰC HÀNH ===\n")

# Bài 1: Tính trung bình điểm
scores = [85, 90, 78, 95, 88]
average = sum(scores) / len(scores)
print(f"Điểm trung bình: {average:.2f}")

# Bài 2: Tìm điểm cao nhất
max_score = max(scores)
min_score = min(scores)
print(f"Cao nhất: {max_score}, Thấp nhất: {min_score}")

# Bài 3: Đếm phần tử trong list
grades = ["A", "B", "A", "C", "A", "B"]
from collections import Counter
grade_count = Counter(grades)
print(f"Đếm điểm: {dict(grade_count)}")

# Bài 4: Kết hợp 2 dict
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
combined = {**dict1, **dict2}
print(f"Dict kết hợp: {combined}")

# Bài 5: List comprehension
squares = [x**2 for x in range(1, 6)]
print(f"Bình phương: {squares}")

# Bài 6: Lọc dữ liệu
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers if x % 2 == 0]
print(f"Số chẵn: {evens}")


print("\n=== HẾT LESSON 3 ===")
