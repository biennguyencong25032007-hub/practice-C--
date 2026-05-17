"""
HƯỚNG DẪN CÁC THƯ VIỆN PHỔ BIẾN (LIBRARIES GUIDE)
=================================================
Giới thiệu và ví dụ về các thư viện Python quan trọng
"""

print("=" * 70)
print("HƯỚNG DẪN THƯ VIỆN PYTHON")
print("=" * 70)

# ===== 1. OS & SYS (HỆ THỐNG) =====
print("\n[1] OS & SYS - Thao tác hệ thống")
print("-" * 70)

import os
import sys

print("Thư viện OS - Thao tác với hệ thống file:")
print(f"  • Thư mục hiện tại: {os.getcwd()}")
print(f"  • Tên OS: {sys.platform}")
print(f"  • Phiên bản Python: {sys.version}")

# Tạo thư mục (nếu chưa tồn tại)
test_dir = "test_folder"
if not os.path.exists(test_dir):
    os.makedirs(test_dir)
    print(f"  ✓ Tạo thư mục: {test_dir}")

# Liệt kê file trong thư mục
print(f"  • File trong thư mục hiện tại: {os.listdir('.')[:5]}")  # 5 file đầu tiên


# ===== 2. MATH & RANDOM =====
print("\n[2] MATH & RANDOM - Toán học & Số ngẫu nhiên")
print("-" * 70)

import math
import random

print("Thư viện MATH:")
print(f"  • π = {math.pi}")
print(f"  • √16 = {math.sqrt(16)}")
print(f"  • 2^3 = {math.pow(2, 3)}")
print(f"  • sin(π/2) = {math.sin(math.pi/2)}")
print(f"  • Làm tròn 3.7 = {math.floor(3.7)}, {math.ceil(3.7)}")

print("\nThư viện RANDOM:")
print(f"  • Số ngẫu nhiên [0-100): {random.randint(0, 100)}")
print(f"  • Số float [0-1): {random.random():.3f}")
print(f"  • Chọn từ list: {random.choice(['A', 'B', 'C', 'D'])}")

# Tạo danh sách ngẫu nhiên
numbers = list(range(1, 11))
random.shuffle(numbers)
print(f"  • Danh sách sau shuffle: {numbers}")


# ===== 3. DATETIME =====
print("\n[3] DATETIME - Ngày giờ")
print("-" * 70)

from datetime import datetime, timedelta, date

now = datetime.now()
today = date.today()

print("Thư viện DATETIME:")
print(f"  • Bây giờ: {now}")
print(f"  • Ngày hôm nay: {today}")
print(f"  • Năm: {now.year}, Tháng: {now.month}, Ngày: {now.day}")

# Tính toán ngày
future = now + timedelta(days=7)
print(f"  • 7 ngày sau: {future.strftime('%Y-%m-%d')}")

# Format ngày
print(f"  • Format tùy chỉnh: {now.strftime('%d/%m/%Y - %H:%M:%S')}")


# ===== 4. STRING METHODS =====
print("\n[4] STRING - Xử lý chuỗi")
print("-" * 70)

text = "  Hello Python World  "

print("Các phương thức string:")
print(f"  • Gốc: '{text}'")
print(f"  • Loại khoảng trắng: '{text.strip()}'")
print(f"  • Chữ thường: {text.lower()}")
print(f"  • Chữ hoa: {text.upper()}")
print(f"  • Thay thế: {text.replace('Python', 'Java')}")
print(f"  • Split: {text.split()}")
print(f"  • Find: {text.find('Python')}")
print(f"  • Bắt đầu với 'Hello': {text.strip().startswith('Hello')}")


# ===== 5. JSON =====
print("\n[5] JSON - Xử lý dữ liệu JSON")
print("-" * 70)

import json

# Convert dict to JSON string
data = {
    "name": "Minh",
    "age": 25,
    "hobbies": ["reading", "gaming", "coding"]
}

json_string = json.dumps(data, indent=2)
print("Chuyển dict thành JSON:")
print(json_string)

# Convert JSON string back to dict
json_text = '{"city": "Hà Nội", "country": "Việt Nam"}'
parsed = json.loads(json_text)
print(f"\nChuyển JSON thành dict: {parsed}")


# ===== 6. CSV =====
print("\n[6] CSV - Xử lý file CSV")
print("-" * 70)

import csv
from io import StringIO

print("Ví dụ đọc CSV:")
csv_data = """name,age,city
An,20,Hà Nội
Bình,25,TPHCM
Chi,22,Đà Nẵng"""

reader = csv.DictReader(StringIO(csv_data))
for row in reader:
    print(f"  {row['name']} - {row['age']} tuổi - {row['city']}")


# ===== 7. REGEX (REGULAR EXPRESSIONS) =====
print("\n[7] REGEX - Biểu thức chính quy")
print("-" * 70)

import re

print("Thư viện RE (Regular Expression):")

# Tìm pattern
text = "Email: example@gmail.com hoặc test@yahoo.com"
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
print(f"  • Tìm email: {emails}")

# Replace
text = "Giá 100,000đ"
text_clean = re.sub(r'[,đ]', '', text)
print(f"  • Gốc: {text}")
print(f"  • Sau xóa ký tự: {text_clean}")

# Split
text = "Apple, Banana; Orange"
items = re.split(r'[,;]', text)
print(f"  • Split: {[item.strip() for item in items]}")


# ===== 8. COLLECTIONS =====
print("\n[8] COLLECTIONS - Cấu trúc dữ liệu nâng cao")
print("-" * 70)

from collections import Counter, defaultdict, namedtuple

# Counter - đếm phần tử
items = ['a', 'b', 'a', 'c', 'a', 'b']
counter = Counter(items)
print(f"  • Counter {items}: {dict(counter)}")

# defaultdict - dict với giá trị mặc định
dd = defaultdict(list)
dd['key1'].append('value1')
print(f"  • defaultdict: {dict(dd)}")

# namedtuple - tuple có tên
Point = namedtuple('Point', ['x', 'y'])
p = Point(10, 20)
print(f"  • namedtuple: Point({p.x}, {p.y})")


# ===== 9. ITERTOOLS =====
print("\n[9] ITERTOOLS - Công cụ lặp nâng cao")
print("-" * 70)

from itertools import combinations, permutations, chain

print("Thư viện ITERTOOLS:")

# Combinations
items = ['A', 'B', 'C']
combos = list(combinations(items, 2))
print(f"  • Combinations: {combos}")

# Chain - nối danh sách
list1 = [1, 2]
list2 = [3, 4]
chained = list(chain(list1, list2))
print(f"  • Chain: {chained}")


# ===== 10. FUNCTOOLS =====
print("\n[10] FUNCTOOLS - Công cụ hàm")
print("-" * 70)

from functools import reduce

print("Thư viện FUNCTOOLS:")

# Reduce - áp dụng hàm cumulatively
numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
print(f"  • Reduce (tích): {product} (1*2*3*4*5)")


# ===== 11. REQUESTS (Web) =====
print("\n[11] REQUESTS - Lấy dữ liệu từ internet")
print("-" * 70)

print("Thư viện REQUESTS (cần cài: pip install requests):")
print("  • GET request: requests.get(url)")
print("  • POST request: requests.post(url, data=data)")
print("  • Response: response.status_code, response.text, response.json()")


# ===== 12. FLASK/DJANGO (Web Framework) =====
print("\n[12] FLASK/DJANGO - Framework Web")
print("-" * 70)

print("Framework phổ biến (cần cài):")
print("  • Flask (nhẹ): pip install flask")
print("  • Django (nặng): pip install django")
print("  • Dùng để: Tạo web application, API, REST service")


# ===== 13. PANDAS (Data Science) =====
print("\n[13] PANDAS - Phân tích dữ liệu")
print("-" * 70)

print("Thư viện PANDAS (cần cài: pip install pandas):")
print("  • DataFrame: Bảng dữ liệu (giống Excel)")
print("  • Series: Cột dữ liệu 1D")
print("  • Đọc: pd.read_csv(), pd.read_excel()")
print("  • Ghi: df.to_csv(), df.to_excel()")


# ===== 14. NUMPY (Khoa học dữ liệu) =====
print("\n[14] NUMPY - Tính toán khoa học")
print("-" * 70)

print("Thư viện NUMPY (cần cài: pip install numpy):")
print("  • Array: Mảng nhiều chiều")
print("  • Tính toán: Nhanh, hiệu quả")
print("  • Linear algebra, FFT, Random")


print("\n" + "=" * 70)
print("✅ HẾT HƯỚNG DẪN THƯ VIỆN")
print("=" * 70)

print("\n📌 CÀI ĐẶT THƯ VIỆN:")
print("""
Sử dụng pip (Python Package Manager):
  pip install <package_name>
  
Ví dụ:
  pip install requests
  pip install pandas
  pip install numpy
  
Xem các package đã cài:
  pip list
  
Cập nhật pip:
  pip install --upgrade pip
""")

print("\n📚 TÌM HIỂU THÊM:")
print("""
- Trang chính thức Python: https://www.python.org/
- PyPI (Package Index): https://pypi.org/
- Tài liệu Python: https://docs.python.org/
- Real Python: https://realpython.com/
""")
