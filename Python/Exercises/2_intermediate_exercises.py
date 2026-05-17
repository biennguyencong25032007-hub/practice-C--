"""
BÀI TẬP TRUNG BÌNH (INTERMEDIATE EXERCISES)
==========================================
Các bài tập để luyện tập Lesson 3-5: Data Structures, Functions & OOP
"""

print("=" * 70)
print("BÀI TẬP TRUNG BÌNH - PHẦN 1: CẤU TRÚC DỮ LIỆU")
print("=" * 70)

"""
BÀI 1.1: Thống kê text
Yêu cầu: Đọc một đoạn text, thống kê:
  - Số từ
  - Từ xuất hiện nhiều nhất
  - Độ dài trung bình từ
  - Số câu (từ các dấu . ! ?)
"""
# Viết code ở đây


"""
BÀI 1.2: Merge dictionaries
Yêu cầu: Kết hợp 2 dictionary, xử lý key trùng
  - Nếu key trùng, giữ giá trị từ dict thứ 2
  - Nếu giá trị là list, hợp nhất chúng
"""
# Viết code ở đây


"""
BÀI 1.3: Transpose matrix
Yêu cầu: Chuyển vị ma trận
  Input: [[1,2,3], [4,5,6]]
  Output: [[1,4], [2,5], [3,6]]
"""
# Viết code ở đây


"""
BÀI 1.4: Dictionary to List & Vice Versa
Yêu cầu: 
  - Chuyển dict thành list of tuples
  - Chuyển list of tuples thành dict
"""
# Viết code ở đây


print("\n" + "=" * 70)
print("BÀI TẬP TRUNG BÌNH - PHẦN 2: HÀM NÂNG CAO")
print("=" * 70)

"""
BÀI 2.1: Decorator đo thời gian
Yêu cầu: Tạo decorator để đo thời gian chạy của hàm
  @timing_decorator
  def slow_function():
      # Thực thi 10 giây
  
  Output: Function slow_function took 10.23 seconds
"""
# Viết code ở đây


"""
BÀI 2.2: Memoization (Caching)
Yêu cầu: Cache kết quả của hàm Fibonacci để tăng tốc độ
  fib(50) - lần đầu chậm, lần thứ hai nhanh
"""
# Viết code ở đây


"""
BÀI 2.3: Higher-order functions
Yêu cầu: 
  - compose(f, g) → f(g(x))
  - partial(func, arg) → Cố định một argument
  - pipe(x, f, g, h) → h(g(f(x)))
"""
# Viết code ở đây


print("\n" + "=" * 70)
print("BÀI TẬP TRUNG BÌNH - PHẦN 3: OOP")
print("=" * 70)

"""
BÀI 3.1: Bank Account System
Yêu cầu: 
  - Class BankAccount với balance, deposit, withdraw
  - Xử lý lỗi: rút quá số dư
  - Ghi log các giao dịch
  - Tính lãi suất
"""
# Viết code ở đây


"""
BÀI 3.2: Inheritance - Shape Hierarchy
Yêu cầu:
  - Class Shape (cha)
  - Class Rectangle, Circle, Triangle (con)
  - Mỗi class tính diện tích, chu vi
  - Phương thức để so sánh diện tích
"""
# Viết code ở đây


"""
BÀI 3.3: Library Management System
Yêu cầu:
  - Class Book: title, author, isbn, available
  - Class Library: thêm/xóa sách, tìm kiếm
  - Method borrow, return
  - Kiểm tra sách hết hạn
"""
# Viết code ở đây


"""
BÀI 3.4: Employee Management
Yêu cầu:
  - Class Employee: name, salary, department
  - Class Manager (kế thừa Employee): team, bonus
  - Tính lương, thưởng
  - Quản lý nhân viên
"""
# Viết code ở đây


print("\n" + "=" * 70)
print("BÀI TẬP TRUNG BÌNH - PHẦN 4: FILE & EXCEPTION")
print("=" * 70)

"""
BÀI 4.1: CSV Processing
Yêu cầu:
  - Đọc file CSV
  - Lọc dữ liệu theo điều kiện
  - Ghi kết quả vào file mới
  - Xử lý lỗi encoding
"""
# Viết code ở đây


"""
BÀI 4.2: JSON Configuration
Yêu cầu:
  - Đọc cấu hình từ file JSON
  - Validate dữ liệu
  - Ghi lại cấu hình
  - Xử lý sai lệch
"""
# Viết code ở đây


"""
BÀI 4.3: Log File Parser
Yêu cầu:
  - Đọc file log
  - Phân tích lỗi
  - Đếm tần suất
  - Tạo báo cáo
"""
# Viết code ở đây


print("\n" + "=" * 70)
print("BÀI TẬP TRUNG BÌNH - PHẦN 5: ALGORITHM")
print("=" * 70)

"""
BÀI 5.1: Sorting Algorithms
Yêu cầu: Cài đặt các thuật toán sắp xếp
  - Bubble Sort
  - Quick Sort
  - Merge Sort
  - So sánh hiệu suất
"""
# Viết code ở đây


"""
BÀI 5.2: Search Algorithms
Yêu cầu:
  - Binary Search
  - Linear Search
  - Compare performance
"""
# Viết code ở đây


"""
BÀI 5.3: Dynamic Programming - Coin Change
Yêu cầu: Tìm số coin tối thiểu để tạo thành một tổng
  coins = [1, 2, 5]
  amount = 5
  Output: 1 (sử dụng 1 coin [5])
"""
# Viết code ở đây


print("\n" + "=" * 70)
print("HƯỚNG DẪN LÀM BÀI:")
print("=" * 70)
print("""
1. ĐỌC KỸ yêu cầu của mỗi bài
2. THIẾT KẾ trước (flowchart, pseudocode)
3. CODE từ từ, test từng phần
4. XỬ LÝ EXCEPTION nếu cần
5. SO SÁNH với đáp án (file solutions_intermediate.py)
6. RÚT RA BÀI HỌC từ từng bài

TIPS:
   ✓ Sử dụng print() để debug
   ✓ Test với nhiều input khác nhau
   ✓ Đảm bảo code clean & readable
   ✓ Viết comments giải thích logic
   ✓ Tái sử dụng code (DRY principle)

Happy Coding! 🎉
""")
