"""
LỜI GIẢI BÀI TẬP TRUNG BÌNH (INTERMEDIATE SOLUTIONS)
====================================================
Giải pháp cho các bài tập Lesson 3-5: Data Structures, Functions & OOP
"""

import time
import json
import csv
from datetime import datetime
from functools import wraps
from typing import Dict, List, Tuple, Callable, Any

print("=" * 70)
print("BÀI TẬP TRUNG BÌNH - PHẦN 1: CẤU TRÚC DỮ LIỆU")
print("=" * 70)

# ========== BÀI 1.1: Thống kê text ==========
print("\n📝 BÀI 1.1: Thống kê text")
print("-" * 70)

def analyze_text(text: str) -> Dict[str, Any]:
    """
    Phân tích một đoạn text và thống kê:
    - Số từ
    - Từ xuất hiện nhiều nhất
    - Độ dài trung bình từ
    - Số câu
    """
    # Xóa khoảng trắng thừa
    text = text.strip()
    
    # Đếm từ
    words = text.split()
    word_count = len(words)
    
    # Tìm từ xuất hiện nhiều nhất
    word_freq = {}
    for word in words:
        cleaned_word = word.lower().rstrip('.,!?;:')
        word_freq[cleaned_word] = word_freq.get(cleaned_word, 0) + 1
    
    most_common_word = max(word_freq, key=word_freq.get)
    most_common_count = word_freq[most_common_word]
    
    # Tính độ dài trung bình từ
    total_chars = sum(len(word) for word in words)
    avg_word_length = total_chars / word_count if word_count > 0 else 0
    
    # Đếm câu (dấu . ! ?)
    sentence_count = sum(1 for char in text if char in '.!?')
    
    return {
        'word_count': word_count,
        'most_common_word': most_common_word,
        'most_common_count': most_common_count,
        'avg_word_length': round(avg_word_length, 2),
        'sentence_count': sentence_count
    }

# Test
sample_text = "Hello world! This is a test. Python is great! I love Python."
result = analyze_text(sample_text)
print(f"Text: {sample_text}")
print(f"Kết quả: {json.dumps(result, indent=2)}")


# ========== BÀI 1.2: Merge dictionaries ==========
print("\n📝 BÀI 1.2: Merge dictionaries")
print("-" * 70)

def merge_dicts(dict1: Dict, dict2: Dict) -> Dict:
    """
    Kết hợp 2 dictionary:
    - Nếu key trùng, giữ giá trị từ dict thứ 2
    - Nếu giá trị là list, hợp nhất chúng
    """
    result = dict1.copy()
    
    for key, value in dict2.items():
        if key in result:
            # Nếu cả hai giá trị là list, hợp nhất
            if isinstance(result[key], list) and isinstance(value, list):
                result[key] = result[key] + value
            else:
                # Ngược lại, giữ giá trị từ dict2
                result[key] = value
        else:
            result[key] = value
    
    return result

# Test
dict_a = {'name': 'Alice', 'hobbies': ['reading', 'coding'], 'age': 25}
dict_b = {'age': 26, 'hobbies': ['gaming'], 'city': 'Hanoi'}
merged = merge_dicts(dict_a, dict_b)
print(f"Dict 1: {dict_a}")
print(f"Dict 2: {dict_b}")
print(f"Merged: {merged}")


# ========== BÀI 1.3: Transpose matrix ==========
print("\n📝 BÀI 1.3: Transpose matrix")
print("-" * 70)

def transpose_matrix(matrix: List[List[int]]) -> List[List[int]]:
    """
    Chuyển vị ma trận
    Input: [[1,2,3], [4,5,6]]
    Output: [[1,4], [2,5], [3,6]]
    """
    if not matrix:
        return []
    
    # Cách 1: Dùng list comprehension
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]
    
    # Cách 2: Dùng zip (ngắn hơn)
    # return [list(col) for col in zip(*matrix)]

# Test
matrix = [[1, 2, 3], [4, 5, 6]]
transposed = transpose_matrix(matrix)
print(f"Ma trận gốc:\n{matrix}")
print(f"Ma trận chuyển vị:\n{transposed}")


# ========== BÀI 1.4: Dictionary to List & Vice Versa ==========
print("\n📝 BÀI 1.4: Dictionary to List & Vice Versa")
print("-" * 70)

def dict_to_list(d: Dict) -> List[Tuple]:
    """Chuyển dict thành list of tuples"""
    return list(d.items())

def list_to_dict(lst: List[Tuple]) -> Dict:
    """Chuyển list of tuples thành dict"""
    return dict(lst)

# Test
my_dict = {'a': 1, 'b': 2, 'c': 3}
dict_as_list = dict_to_list(my_dict)
converted_back = list_to_dict(dict_as_list)

print(f"Dict gốc: {my_dict}")
print(f"Chuyển thành list: {dict_as_list}")
print(f"Chuyển lại thành dict: {converted_back}")


print("\n" + "=" * 70)
print("BÀI TẬP TRUNG BÌNH - PHẦN 2: HÀM NÂNG CAO")
print("=" * 70)

# ========== BÀI 2.1: Decorator đo thời gian ==========
print("\n📝 BÀI 2.1: Decorator đo thời gian")
print("-" * 70)

def timing_decorator(func: Callable) -> Callable:
    """
    Decorator để đo thời gian chạy của hàm
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        
        elapsed_time = end_time - start_time
        print(f"Function '{func.__name__}' took {elapsed_time:.4f} seconds")
        
        return result
    
    return wrapper

@timing_decorator
def slow_function(n: int = 1000000):
    """Hàm chậm để test decorator"""
    total = sum(i * i for i in range(n))
    return total

# Test
result = slow_function(1000000)
print(f"Kết quả: {result}")


# ========== BÀI 2.2: Memoization (Caching) ==========
print("\n📝 BÀI 2.2: Memoization (Caching)")
print("-" * 70)

def memoize(func: Callable) -> Callable:
    """
    Decorator để cache kết quả của hàm
    """
    cache = {}
    
    @wraps(func)
    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    
    return wrapper

@memoize
def fibonacci(n: int) -> int:
    """Tính số Fibonacci thứ n (có caching)"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Test
print("Lần đầu (chậm):")
start = time.time()
fib_50 = fibonacci(50)
print(f"fibonacci(50) = {fib_50}, Time: {time.time() - start:.4f}s")

print("\nLần thứ 2 (nhanh hơn - từ cache):")
start = time.time()
fib_50_again = fibonacci(50)
print(f"fibonacci(50) = {fib_50_again}, Time: {time.time() - start:.4f}s")


# ========== BÀI 2.3: Higher-order functions ==========
print("\n📝 BÀI 2.3: Higher-order functions")
print("-" * 70)

def compose(f: Callable, g: Callable) -> Callable:
    """
    Compose hai hàm: f(g(x))
    """
    return lambda x: f(g(x))

def partial(func: Callable, arg: Any) -> Callable:
    """
    Cố định một argument của hàm
    """
    return lambda *args, **kwargs: func(arg, *args, **kwargs)

def pipe(x: Any, *funcs: Callable) -> Any:
    """
    Pipe: h(g(f(x)))
    """
    result = x
    for func in funcs:
        result = func(result)
    return result

# Test
def add_one(x):
    return x + 1

def multiply_two(x):
    return x * 2

def square(x):
    return x ** 2

# compose: (x + 1) * 2
composed = compose(multiply_two, add_one)
print(f"compose(multiply_two, add_one)(5) = {composed(5)}")  # (5+1)*2 = 12

# partial: func(10, x) với func = add
def add(a, b):
    return a + b

add_10 = partial(add, 10)
print(f"partial(add, 10)(5) = {add_10(5)}")  # 10+5 = 15

# pipe: ((5+1)*2)^2
result = pipe(5, add_one, multiply_two, square)
print(f"pipe(5, add_one, multiply_two, square) = {result}")  # ((5+1)*2)^2 = 144


print("\n" + "=" * 70)
print("BÀI TẬP TRUNG BÌNH - PHẦN 3: OOP")
print("=" * 70)

# ========== BÀI 3.1: Bank Account System ==========
print("\n📝 BÀI 3.1: Bank Account System")
print("-" * 70)

class BankAccount:
    """
    Hệ thống tài khoản ngân hàng
    """
    interest_rate = 0.05  # 5% lãi suất hàng năm
    
    def __init__(self, owner: str, initial_balance: float = 0):
        self.owner = owner
        self.balance = initial_balance
        self.transactions = []
        if initial_balance > 0:
            self._log_transaction('Initial deposit', initial_balance)
    
    def deposit(self, amount: float) -> None:
        """Gửi tiền"""
        if amount <= 0:
            raise ValueError("Số tiền gửi phải lớn hơn 0")
        self.balance += amount
        self._log_transaction('Deposit', amount)
        print(f"✓ Gửi ${amount:.2f}. Số dư hiện tại: ${self.balance:.2f}")
    
    def withdraw(self, amount: float) -> None:
        """Rút tiền"""
        if amount <= 0:
            raise ValueError("Số tiền rút phải lớn hơn 0")
        if amount > self.balance:
            raise ValueError(f"Rút quá số dư! Số dư: ${self.balance:.2f}")
        self.balance -= amount
        self._log_transaction('Withdrawal', -amount)
        print(f"✓ Rút ${amount:.2f}. Số dư hiện tại: ${self.balance:.2f}")
    
    def apply_interest(self) -> None:
        """Tính lãi suất"""
        interest = self.balance * self.interest_rate
        self.balance += interest
        self._log_transaction('Interest', interest)
        print(f"✓ Tính lãi: ${interest:.2f}. Số dư mới: ${self.balance:.2f}")
    
    def _log_transaction(self, type_: str, amount: float) -> None:
        """Ghi log giao dịch"""
        self.transactions.append({
            'date': datetime.now(),
            'type': type_,
            'amount': amount,
            'balance': self.balance
        })
    
    def show_history(self) -> None:
        """Hiển thị lịch sử giao dịch"""
        print(f"\n📋 Lịch sử giao dịch của {self.owner}:")
        for i, trans in enumerate(self.transactions, 1):
            print(f"{i}. {trans['date'].strftime('%Y-%m-%d %H:%M:%S')} | "
                  f"{trans['type']:12} | ${trans['amount']:8.2f} | "
                  f"Số dư: ${trans['balance']:8.2f}")

# Test
account = BankAccount("Nguyễn Văn A", 1000)
try:
    account.deposit(500)
    account.withdraw(200)
    account.apply_interest()
    account.show_history()
except ValueError as e:
    print(f"❌ Lỗi: {e}")


# ========== BÀI 3.2: Inheritance - Shape Hierarchy ==========
print("\n📝 BÀI 3.2: Inheritance - Shape Hierarchy")
print("-" * 70)

import math

class Shape:
    """Class cha cho các hình dạng"""
    
    def area(self) -> float:
        raise NotImplementedError("Subclass phải implement area()")
    
    def perimeter(self) -> float:
        raise NotImplementedError("Subclass phải implement perimeter()")
    
    def compare_area(self, other: 'Shape') -> str:
        """So sánh diện tích với hình khác"""
        my_area = self.area()
        other_area = other.area()
        
        if my_area > other_area:
            return f"{self.__class__.__name__} lớn hơn {other.__class__.__name__}"
        elif my_area < other_area:
            return f"{self.__class__.__name__} nhỏ hơn {other.__class__.__name__}"
        else:
            return f"{self.__class__.__name__} và {other.__class__.__name__} bằng nhau"

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
    
    def area(self) -> float:
        return self.width * self.height
    
    def perimeter(self) -> float:
        return 2 * (self.width + self.height)
    
    def __str__(self):
        return f"Rectangle({self.width}x{self.height})"

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius
    
    def area(self) -> float:
        return math.pi * self.radius ** 2
    
    def perimeter(self) -> float:
        return 2 * math.pi * self.radius
    
    def __str__(self):
        return f"Circle(r={self.radius})"

class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        self.a = a
        self.b = b
        self.c = c
    
    def area(self) -> float:
        """Công thức Heron"""
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))
    
    def perimeter(self) -> float:
        return self.a + self.b + self.c
    
    def __str__(self):
        return f"Triangle({self.a}, {self.b}, {self.c})"

# Test
rect = Rectangle(5, 3)
circle = Circle(2)
triangle = Triangle(3, 4, 5)

shapes = [rect, circle, triangle]

print("Thông tin các hình:")
for shape in shapes:
    print(f"{shape}: Diện tích = {shape.area():.2f}, Chu vi = {shape.perimeter():.2f}")

print(f"\n{circle.compare_area(rect)}")
print(f"{triangle.compare_area(rect)}")


# ========== BÀI 3.3: Library Management System ==========
print("\n📝 BÀI 3.3: Library Management System")
print("-" * 70)

class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True
        self.borrowed_date = None
    
    def __str__(self):
        status = "✓ Có sẵn" if self.available else "✗ Đã cho mượn"
        return f"{self.title} - {self.author} (ISBN: {self.isbn}) [{status}]"

class Library:
    def __init__(self):
        self.books = {}  # isbn -> Book
    
    def add_book(self, book: Book) -> None:
        """Thêm sách vào thư viện"""
        if book.isbn not in self.books:
            self.books[book.isbn] = book
            print(f"✓ Đã thêm: {book.title}")
        else:
            print(f"⚠ Sách đã tồn tại: {book.title}")
    
    def remove_book(self, isbn: str) -> None:
        """Xóa sách khỏi thư viện"""
        if isbn in self.books:
            book = self.books.pop(isbn)
            print(f"✓ Đã xóa: {book.title}")
        else:
            print(f"❌ Không tìm thấy sách với ISBN: {isbn}")
    
    def search(self, keyword: str) -> List[Book]:
        """Tìm kiếm sách theo tiêu đề hoặc tác giả"""
        keyword = keyword.lower()
        results = []
        for book in self.books.values():
            if keyword in book.title.lower() or keyword in book.author.lower():
                results.append(book)
        return results
    
    def borrow(self, isbn: str) -> bool:
        """Mượn sách"""
        if isbn in self.books:
            book = self.books[isbn]
            if book.available:
                book.available = False
                book.borrowed_date = datetime.now()
                print(f"✓ Bạn đã mượn: {book.title}")
                return True
            else:
                print(f"❌ {book.title} đã được cho mượn")
                return False
        else:
            print(f"❌ Không tìm thấy sách")
            return False
    
    def return_book(self, isbn: str) -> bool:
        """Trả sách"""
        if isbn in self.books:
            book = self.books[isbn]
            if not book.available:
                book.available = True
                book.borrowed_date = None
                print(f"✓ Bạn đã trả: {book.title}")
                return True
            else:
                print(f"❌ {book.title} không được cho mượn")
                return False
        else:
            print(f"❌ Không tìm thấy sách")
            return False
    
    def list_all(self) -> None:
        """Liệt kê tất cả sách"""
        print("\n📚 Danh sách sách trong thư viện:")
        for book in self.books.values():
            print(f"  {book}")

# Test
library = Library()
book1 = Book("Python Basics", "John Doe", "001")
book2 = Book("Advanced Python", "Jane Smith", "002")
book3 = Book("Django for Beginners", "John Doe", "003")

library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.list_all()

print("\n📖 Mượn sách:")
library.borrow("001")

print("\n🔍 Tìm kiếm 'John':")
results = library.search("John")
for book in results:
    print(f"  {book}")

print("\n📤 Trả sách:")
library.return_book("001")


# ========== BÀI 3.4: Employee Management ==========
print("\n📝 BÀI 3.4: Employee Management")
print("-" * 70)

class Employee:
    """Class nhân viên"""
    
    def __init__(self, name: str, salary: float, department: str):
        self.name = name
        self.salary = salary
        self.department = department
    
    def get_annual_salary(self) -> float:
        """Tính lương hàng năm"""
        return self.salary * 12
    
    def __str__(self):
        return f"{self.name} - Dept: {self.department} - Salary: ${self.salary:.2f}/month"

class Manager(Employee):
    """Class quản lý (kế thừa Employee)"""
    
    def __init__(self, name: str, salary: float, department: str, 
                 team: List[Employee] = None, bonus_rate: float = 0.1):
        super().__init__(name, salary, department)
        self.team = team if team is not None else []
        self.bonus_rate = bonus_rate
    
    def add_employee(self, employee: Employee) -> None:
        """Thêm nhân viên vào nhóm"""
        self.team.append(employee)
        print(f"✓ Đã thêm {employee.name} vào nhóm của {self.name}")
    
    def remove_employee(self, name: str) -> None:
        """Xóa nhân viên khỏi nhóm"""
        self.team = [e for e in self.team if e.name != name]
        print(f"✓ Đã xóa {name} khỏi nhóm")
    
    def get_bonus(self) -> float:
        """Tính thưởng quản lý"""
        return self.salary * self.bonus_rate
    
    def get_total_salary(self) -> float:
        """Tính lương + thưởng"""
        return self.get_annual_salary() + self.get_bonus() * 12
    
    def show_team(self) -> None:
        """Hiển thị nhóm nhân viên"""
        print(f"\n👥 Nhóm của {self.name}:")
        for employee in self.team:
            print(f"  • {employee}")
        print(f"  Tổng lương nhân viên: ${sum(e.get_annual_salary() for e in self.team):.2f}")
    
    def __str__(self):
        return f"{super().__str__()} [Manager] Bonus: ${self.get_bonus():.2f}/month"

# Test
emp1 = Employee("Alice", 2000, "Engineering")
emp2 = Employee("Bob", 1800, "Engineering")
emp3 = Employee("Charlie", 1600, "Sales")

manager = Manager("David", 3000, "Engineering", [emp1, emp2], bonus_rate=0.15)

print("📋 Thông tin nhân viên:")
print(emp1)
print(emp2)
print(emp3)
print(manager)

manager.show_team()
print(f"\n💰 Lương hàng năm của {manager.name} (kể cả thưởng): ${manager.get_total_salary():.2f}")


print("\n" + "=" * 70)
print("BÀI TẬP TRUNG BÌNH - PHẦN 4: FILE & EXCEPTION")
print("=" * 70)

# ========== BÀI 4.1: CSV Processing ==========
print("\n📝 BÀI 4.1: CSV Processing")
print("-" * 70)

def process_csv(input_file: str, output_file: str, filter_column: str, 
                filter_value: Any) -> None:
    """
    Đọc file CSV, lọc dữ liệu và ghi vào file mới
    """
    try:
        data = []
        with open(input_file, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row.get(filter_column) == str(filter_value):
                    data.append(row)
        
        if not data:
            print(f"⚠ Không tìm thấy dữ liệu phù hợp")
            return
        
        # Ghi kết quả
        with open(output_file, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
        
        print(f"✓ Đã xử lý {len(data)} dòng và ghi vào {output_file}")
    
    except FileNotFoundError:
        print(f"❌ Không tìm thấy file: {input_file}")
    except Exception as e:
        print(f"❌ Lỗi: {e}")

print("(Hàm process_csv được định nghĩa, có thể sử dụng với file CSV)")


# ========== BÀI 4.2: JSON Configuration ==========
print("\n📝 BÀI 4.2: JSON Configuration")
print("-" * 70)

def load_config(config_file: str) -> Dict:
    """Đọc cấu hình từ file JSON"""
    try:
        with open(config_file, 'r', encoding='utf-8') as f:
            config = json.load(f)
        print(f"✓ Đã load cấu hình từ {config_file}")
        return config
    except FileNotFoundError:
        print(f"❌ Không tìm thấy file: {config_file}")
        return {}
    except json.JSONDecodeError:
        print(f"❌ File JSON không hợp lệ")
        return {}

def validate_config(config: Dict, required_keys: List[str]) -> bool:
    """Validate dữ liệu cấu hình"""
    for key in required_keys:
        if key not in config:
            print(f"❌ Thiếu khóa bắt buộc: {key}")
            return False
    return True

def save_config(config: Dict, config_file: str) -> None:
    """Ghi cấu hình vào file JSON"""
    try:
        with open(config_file, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=4, ensure_ascii=False)
        print(f"✓ Đã lưu cấu hình vào {config_file}")
    except Exception as e:
        print(f"❌ Lỗi khi lưu: {e}")

print("(Các hàm cấu hình JSON được định nghĩa)")


# ========== BÀI 4.3: Log File Parser ==========
print("\n📝 BÀI 4.3: Log File Parser")
print("-" * 70)

def parse_log_file(log_file: str) -> Dict[str, int]:
    """
    Đọc file log và phân tích lỗi
    """
    error_count = {}
    
    try:
        with open(log_file, 'r', encoding='utf-8') as f:
            for line in f:
                # Tìm lỗi (dòng chứa ERROR, WARNING, Exception)
                if 'ERROR' in line.upper() or 'EXCEPTION' in line.upper():
                    # Trích xuất loại lỗi
                    parts = line.split(':')
                    if len(parts) > 1:
                        error_type = parts[0].strip()
                        error_count[error_type] = error_count.get(error_type, 0) + 1
        
        print(f"✓ Phân tích {log_file}")
        print("\n📊 Thống kê lỗi:")
        for error_type, count in sorted(error_count.items(), key=lambda x: x[1], reverse=True):
            print(f"  {error_type}: {count} lần")
        
        return error_count
    
    except FileNotFoundError:
        print(f"❌ Không tìm thấy file log: {log_file}")
        return {}

print("(Hàm parse_log_file được định nghĩa)")


print("\n" + "=" * 70)
print("BÀI TẬP TRUNG BÌNH - PHẦN 5: ALGORITHM")
print("=" * 70)

# ========== BÀI 5.1: Sorting Algorithms ==========
print("\n📝 BÀI 5.1: Sorting Algorithms")
print("-" * 70)

def bubble_sort(arr: List[int]) -> List[int]:
    """Sắp xếp nổi bọt"""
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def quick_sort(arr: List[int]) -> List[int]:
    """Sắp xếp nhanh"""
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)

def merge_sort(arr: List[int]) -> List[int]:
    """Sắp xếp trộn"""
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def merge(left: List[int], right: List[int]) -> List[int]:
    """Trộn hai mảng đã sắp xếp"""
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Test
test_array = [64, 34, 25, 12, 22, 11, 90]
print(f"Mảng gốc: {test_array}")
print(f"Bubble Sort: {bubble_sort(test_array)}")
print(f"Quick Sort: {quick_sort(test_array)}")
print(f"Merge Sort: {merge_sort(test_array)}")


# ========== BÀI 5.2: Search Algorithms ==========
print("\n📝 BÀI 5.2: Search Algorithms")
print("-" * 70)

def linear_search(arr: List[int], target: int) -> int:
    """Tìm kiếm tuyến tính"""
    for i, value in enumerate(arr):
        if value == target:
            return i
    return -1

def binary_search(arr: List[int], target: int) -> int:
    """Tìm kiếm nhị phân (mảng phải đã sắp xếp)"""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

# Test
sorted_array = [11, 12, 22, 25, 34, 64, 90]
target = 25

print(f"Mảng: {sorted_array}, Tìm: {target}")
print(f"Linear Search: Vị trí {linear_search(sorted_array, target)}")
print(f"Binary Search: Vị trí {binary_search(sorted_array, target)}")


# ========== BÀI 5.3: Dynamic Programming - Coin Change ==========
print("\n📝 BÀI 5.3: Dynamic Programming - Coin Change")
print("-" * 70)

def coin_change(coins: List[int], amount: int) -> int:
    """
    Tìm số coin tối thiểu để tạo thành tổng
    coins = [1, 2, 5]
    amount = 5
    Output: 1 (sử dụng 1 coin [5])
    """
    # dp[i] = số coin tối thiểu để tạo thành i
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1

def coin_change_with_path(coins: List[int], amount: int) -> Tuple[int, List[int]]:
    """Coin change với trả lại đường đi"""
    dp = [float('inf')] * (amount + 1)
    parent = [-1] * (amount + 1)
    dp[0] = 0
    
    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                parent[i] = coin
    
    # Truy ngược đường đi
    path = []
    current = amount
    while current > 0:
        coin = parent[current]
        path.append(coin)
        current -= coin
    
    return dp[amount] if dp[amount] != float('inf') else -1, path

# Test
coins = [1, 2, 5]
amount = 11

min_coins = coin_change(coins, amount)
min_coins_path, used_coins = coin_change_with_path(coins, amount)

print(f"Coins: {coins}, Amount: {amount}")
print(f"Số coin tối thiểu: {min_coins}")
print(f"Coins sử dụng: {sorted(used_coins)} (tổng: {sum(used_coins)})")


print("\n" + "=" * 70)
print("✅ HẾT LỜI GIẢI!")
print("=" * 70)
