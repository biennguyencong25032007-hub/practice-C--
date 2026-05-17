"""
🐍 PYTHON LEARNING HUB - BẢN ĐỒ NHANH
====================================
File này giúp bạn nhanh chóng tìm thấy những gì bạn cần
"""

# ASCII Art Welcome
print("""
╔══════════════════════════════════════════════════════════════════════════╗
║                                                                          ║
║           🐍 PYTHON LEARNING ROADMAP - CƠ BẢN ĐẾN NÂNG CAO 🐍           ║
║                                                                          ║
║                    Chào mừng bạn đến với hành trình                    ║
║                         Làm chủ lập trình Python                        ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
""")

# Menu chính
def main_menu():
    while True:
        print("""
┌──────────────────────────────────────────────────────────────────────────┐
│ MENU CHÍNH - CHỌN NHỮNG GÌ BẠN MUỐN LÀNG                               │
└──────────────────────────────────────────────────────────────────────────┘

1️⃣  📖 LESSONS (Bài học có giải thích chi tiết)
    ├─ Lesson 1: Cơ bản (Biến, kiểu dữ liệu)
    ├─ Lesson 2: Điều khiển luồng (If/Else, Loop)
    ├─ Lesson 3: Cấu trúc dữ liệu (List, Dict, Tuple, Set)
    ├─ Lesson 4: Hàm (Functions, *args, lambda)
    └─ Lesson 5: Lập trình hướng đối tượng (OOP)

2️⃣  💪 EXERCISES (Bài tập thực hành)
    ├─ Beginner Exercises (cơ bản)
    ├─ Beginner Solutions (đáp án)
    ├─ Intermediate Exercises (trung bình)
    └─ Intermediate Solutions (đáp án)

3️⃣  🎮 MINI PROJECTS (Dự án thực tế nhỏ)
    ├─ Project 1: Calculator (Máy tính)
    ├─ Project 2: To-Do List (Danh sách việc)
    └─ Project 3: Guessing Game (Trò chơi đoán số)

4️⃣  📚 LIBRARIES GUIDE (Hướng dẫn thư viện)
    └─ 14 thư viện Python phổ biến

5️⃣  🚀 QUICK REFERENCE (Tham khảo nhanh)
    └─ Tất cả cú pháp, ví dụ, tips

6️⃣  📊 PROGRESS TRACKER (Theo dõi tiến độ)
    └─ Đánh dấu những gì đã học

7️⃣  📄 ROADMAP & README (Kế hoạch & Hướng dẫn)
    ├─ Sơ đồ học tập chi tiết
    └─ Hướng dẫn cách sử dụng

0️⃣  Thoát
        """)
        
        choice = input("👉 Nhập lựa chọn (0-7): ").strip()
        
        if choice == '1':
            lessons_menu()
        elif choice == '2':
            exercises_menu()
        elif choice == '3':
            projects_menu()
        elif choice == '4':
            libraries_menu()
        elif choice == '5':
            print("\n📌 Mở file: QUICK_REFERENCE.py")
            print("   Dùng Ctrl+F để tìm kiếm nhanh\n")
        elif choice == '6':
            print("\n📊 Mở file: PROGRESS_TRACKER.py để theo dõi tiến độ\n")
        elif choice == '7':
            roadmap_menu()
        elif choice == '0':
            print("""
╔══════════════════════════════════════════════════════════════════════════╗
║                                                                          ║
║   Cảm ơn đã sử dụng Python Learning Hub!                               ║
║                                                                          ║
║   Hãy nhớ: "Mỗi ngày một chút, không bao giờ là muộn"                  ║
║                                                                          ║
║   Happy Coding! 🚀 💻 🐍                                                 ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
            """)
            break
        else:
            print("❌ Lựa chọn không hợp lệ!\n")

def lessons_menu():
    print("""
┌──────────────────────────────────────────────────────────────────────────┐
│ BÀI HỌC - CHỌN BÀI BẠN MUỐN HỌC                                        │
└──────────────────────────────────────────────────────────────────────────┘

File location: Lessons/

📝 LESSON 1: BASICS (CƠ BẢN)
   File: 1_basics_lesson.py
   Thời gian: ~45 phút
   Nội dung:
     • Print statement
     • Biến & gán giá trị
     • Kiểu dữ liệu: int, float, str, bool, None
     • Toán tử cơ bản
     • Comments
   Skills: Understanding Python fundamentals
   ⭐ Độ khó: ⭐

🔄 LESSON 2: CONTROL FLOW (ĐIỀU KHIỂN LUỒNG)
   File: 2_control_flow_lesson.py
   Thời gian: ~1 giờ
   Nội dung:
     • If/Elif/Else statements
     • Toán tử logic (and, or, not)
     • While loop
     • For loop
     • Break, Continue, Pass
     • Nested loops
   Skills: Control program flow
   ⭐ Độ khó: ⭐

📦 LESSON 3: DATA STRUCTURES (CẤU TRÚC DỮ LIỆU)
   File: 3_data_structures_lesson.py
   Thời gian: ~1.5 giờ
   Nội dung:
     • List & methods
     • Tuple (immutable)
     • Dictionary & operations
     • Set & operations
     • Slicing & indexing
     • List comprehension
   Skills: Work with complex data
   ⭐ Độ khó: ⭐⭐

⚙️  LESSON 4: FUNCTIONS (HÀM)
   File: 4_functions_lesson.py
   Thời gian: ~1.5 giờ
   Nội dung:
     • Định nghĩa hàm
     • Parameters & arguments
     • Return values
     • Default arguments
     • *args & **kwargs
     • Lambda functions
     • Scope (global, local, nonlocal)
     • Docstrings
     • Decorators
   Skills: Reusable, modular code
   ⭐ Độ khó: ⭐⭐

🏛️  LESSON 5: OOP (LẬP TRÌNH HƯỚNG ĐỐI TƯỢNG)
   File: 5_oop_lesson.py
   Thời gian: ~2 giờ
   Nội dung:
     • Class & Object
     • Attributes & Methods
     • Constructor (__init__)
     • Inheritance (kế thừa)
     • Polymorphism (đa hình)
     • Encapsulation (che giấu)
     • Special methods (__str__, __eq__, etc)
     • @property decorator
   Skills: Object-oriented design
   ⭐ Độ khó: ⭐⭐⭐

💡 NEXT STEP: Làm Exercise tương ứng sau mỗi lesson!
    """)
    input("Nhấn Enter để quay lại...")

def exercises_menu():
    print("""
┌──────────────────────────────────────────────────────────────────────────┐
│ BÀI TẬP - THỰC HÀNH & KIỂM ĐỊNH KIẾN THỨC                             │
└──────────────────────────────────────────────────────────────────────────┘

File location: Exercises/

🟢 BEGINNER EXERCISES (BÀI TẬP CƠ BẢN)
   File: 1_beginner_exercises.py
   Số lượng: 15+ bài
   Độ khó: ⭐ dễ
   Thời gian: 2-3 giờ
   
   Bao gồm:
   ✓ Bài tập về biến, kiểu dữ liệu
   ✓ Bài tập về điều kiện (if/else)
   ✓ Bài tập về loop (for/while)
   ✓ Bài tập về string & list
   
   💡 TIP: Làm trước, xem đáp án sau!

🟢 BEGINNER SOLUTIONS (ĐÁP ÁN CHI TIẾT)
   File: 1_beginner_solutions.py
   Nội dung: Lời giải chi tiết cho tất cả bài tập cơ bản
   💡 CÁCH DÙNG: So sánh với code của bạn sau khi làm xong

🟡 INTERMEDIATE EXERCISES (BÀI TẬP TRUNG BÌNH)
   File: 2_intermediate_exercises.py
   Số lượng: 15+ bài
   Độ khó: ⭐⭐⭐ khó
   Thời gian: 4-6 giờ
   
   Bao gồm:
   ✓ Data structures nâng cao
   ✓ Functions & decorators
   ✓ OOP & design patterns
   ✓ File I/O & exception handling
   ✓ Algorithms & problem solving
   
   💡 TIP: Thử code trước, sau đó xem gợi ý

🟡 INTERMEDIATE SOLUTIONS (ĐÁP ÁN)
   File: 2_intermediate_solutions.py
   (Sẽ được tạo sau)

📊 RECOMMENDED PROGRESS:
   Week 1-2: Làm hết Beginner Exercises
   Week 3-4: Bắt đầu Intermediate Exercises
   Week 5+: Làm project khi vừa hoàn thành exercise liên quan
    """)
    input("Nhấn Enter để quay lại...")

def projects_menu():
    print("""
┌──────────────────────────────────────────────────────────────────────────┐
│ MINI PROJECTS - DỰ ÁN THỰC TIỄN NHỎ ĐỂ ÁP DỤNG KIẾN THỨC             │
└──────────────────────────────────────────────────────────────────────────┘

File location: Mini_Projects/

🧮 PROJECT 1: CALCULATOR (MÁY TÍNH ĐƠN GIẢN)
   File: 1_calculator.py
   Kỹ năng: Variables, Functions, Control Flow, Try/Except
   Thời gian: 30-45 phút
   Độ khó: ⭐
   
   Tính năng:
   ✓ Phép cộng, trừ, nhân, chia
   ✓ Menu tương tác
   ✓ Xử lý lỗi (chia cho 0)
   ✓ Thoát chương trình
   
   🎯 Bạn sẽ học:
     - Viết functions tái sử dụng
     - Xử lý input từ user
     - Exception handling
     - While loop & menu
   
   🚀 Chạy bằng: python Mini_Projects/1_calculator.py

✅ PROJECT 2: TO-DO LIST (DANH SÁCH VIỆC CẦN LÀM)
   File: 2_todo_list.py
   Kỹ năng: OOP, File I/O, JSON, List & Dict
   Thời gian: 1-1.5 giờ
   Độ khó: ⭐⭐
   
   Tính năng:
   ✓ Thêm/xóa/hoàn thành việc
   ✓ Xem danh sách
   ✓ Lưu vào file JSON
   ✓ Ưu tiên việc làm
   ✓ Ghi log ngày tạo
   
   🎯 Bạn sẽ học:
     - Tạo class từ đầu
     - Quản lý dữ liệu với JSON
     - Tương tác file system
     - Menu-driven application
   
   🚀 Chạy bằng: python Mini_Projects/2_todo_list.py

🎮 PROJECT 3: GUESSING GAME (TRÒ CHƠI ĐỐN SỐ)
   File: 3_guessing_game.py
   Kỹ năng: OOP, Game Logic, Random, JSON, File I/O
   Thời gian: 1.5-2 giờ
   Độ khó: ⭐⭐
   
   Tính năng:
   ✓ Chế độ một người chơi
   ✓ Chế độ hai người chơi
   ✓ Gợi ý thông minh
   ✓ Xếp hạng điểm (leaderboard)
   ✓ Lưu/tải điểm từ file
   
   🎯 Bạn sẽ học:
     - Thiết kế game logic
     - Quản lý game state
     - Scoreboard & rankings
     - Advanced OOP
     - User experience
   
   🚀 Chạy bằng: python Mini_Projects/3_guessing_game.py

📈 PROGRESSION:
   ✅ Project 1: Sau Lesson 2
   ✅ Project 2: Sau Lesson 5
   ✅ Project 3: Sau Lesson 5 (OOP)

💡 TIPS:
   • Chạy code để hiểu cách hoạt động
   • Modify code - thêm tính năng mới
   • Refactor code - cải thiện chất lượng
   • Tạo project riêng với cấu trúc tương tự
    """)
    input("Nhấn Enter để quay lại...")

def libraries_menu():
    print("""
┌──────────────────────────────────────────────────────────────────────────┐
│ LIBRARIES GUIDE - HỌC SỬ DỤNG CÁC THƯ VIỆN PYTHON PHỔ BIẾN            │
└──────────────────────────────────────────────────────────────────────────┘

File location: Libraries_Guide/

📚 LIBRARIES OVERVIEW
   File: libraries_overview.py
   Thời gian: 1-2 giờ để đọc & thực hành
   
   14 thư viện được giới thiệu:
   
   1️⃣  os & sys - Thao tác hệ thống
   2️⃣  math & random - Toán học & số ngẫu nhiên
   3️⃣  datetime - Ngày giờ
   4️⃣  string - Xử lý chuỗi
   5️⃣  json - Xử lý dữ liệu JSON
   6️⃣  csv - Xử lý file CSV
   7️⃣  re (regex) - Biểu thức chính quy
   8️⃣  collections - Cấu trúc dữ liệu nâng cao
   9️⃣  itertools - Công cụ lặp
   🔟 functools - Công cụ hàm
   1️⃣1️⃣ requests - Lấy dữ liệu từ web
   1️⃣2️⃣ flask/django - Web frameworks
   1️⃣3️⃣ pandas - Phân tích dữ liệu
   1️⃣4️⃣ numpy - Tính toán khoa học
   
   📖 Mỗi thư viện có:
      ✓ Giới thiệu
      ✓ Code example
      ✓ Cách cài đặt
      ✓ Use cases

🔧 CÀI ĐẶT PACKAGE:
   pip install <package_name>
   
   Ví dụ:
   pip install requests
   pip install pandas
   pip install numpy

💡 TIPS:
   • Đọc official documentation
   • Thực hành với code examples
   • Sử dụng trong projects
   • Khám phá package mới trên PyPI.org
    """)
    input("Nhấn Enter để quay lại...")

def roadmap_menu():
    print("""
┌──────────────────────────────────────────────────────────────────────────┐
│ ROADMAP & GUIDES - SƠ ĐỒ & HƯỚNG DẪN HỌC TẬP                         │
└──────────────────────────────────────────────────────────────────────────┘

📋 PYTHON_LEARNING_ROADMAP.md
   Nội dung: Sơ đồ chi tiết học Python
   Bao gồm:
   ✓ 10 levels học tập từ cơ bản đến nâng cao
   ✓ Timeline & mốc thời gian
   ✓ Các khái niệm chính ở mỗi level
   ✓ Cách sử dụng tài liệu này
   ✓ Best practices
   
   💡 Đọc file này trước khi bắt đầu!

📖 README.md
   Nội dung: Hướng dẫn sử dụng toàn bộ học liệu
   Bao gồm:
   ✓ Cấu trúc folder
   ✓ Cách bắt đầu
   ✓ Timeline đề xuất
   ✓ Tài liệu bổ sung
   ✓ FAQ

⚡ QUICK_REFERENCE.py
   Nội dung: Tham khảo nhanh tất cả cú pháp
   Bao gồm:
   ✓ Biến & kiểu dữ liệu
   ✓ Toán tử
   ✓ Cấu trúc điều khiển
   ✓ Hàm
   ✓ String methods
   ✓ List & Dictionary
   ✓ File I/O
   ✓ Exception handling
   ✓ OOP
   ✓ Tips & best practices
   
   💡 Giữ file này ở tay khi code!

📊 PROGRESS_TRACKER.py
   Nội dụng: Theo dõi tiến độ học tập
   Bao gồm:
   ✓ Checklist cho mỗi lesson
   ✓ Bài tập & project
   ✓ Tóm tắt tiến độ
   ✓ Bước tiếp theo
   
   💡 Chạy định kỳ để review tiến độ!

🎯 RECOMMENDED READING ORDER:
   1️⃣  PYTHON_LEARNING_ROADMAP.md (đầu tiên)
   2️⃣  README.md (get started)
   3️⃣  PROGRESS_TRACKER.py (track progress)
   4️⃣  QUICK_REFERENCE.py (khi code)
    """)
    input("Nhấn Enter để quay lại...")

# ===== GETTING STARTED TIPS =====
def print_getting_started():
    print("""
╔══════════════════════════════════════════════════════════════════════════╗
║                      🚀 GETTING STARTED - BẮT ĐẦU NGAY                 ║
╚══════════════════════════════════════════════════════════════════════════╝

1️⃣  ĐỌC SƠ ĐỒ
    Mở: PYTHON_LEARNING_ROADMAP.md
    Thời gian: 10 phút
    Mục tiêu: Hiểu cơ bản cấu trúc học tập

2️⃣  CHẠY LESSON 1
    Mở: Lessons/1_basics_lesson.py
    Nhấn F5 hoặc chạy: python Lessons/1_basics_lesson.py
    Thời gian: 45 phút
    Mục tiêu: Học biến, kiểu dữ liệu, print

3️⃣  LÀM BÀI TẬP
    Mở: Exercises/1_beginner_exercises.py
    Làm 3-5 bài đầu tiên
    Thời gian: 30-45 phút
    Mục tiêu: Thực hành những gì vừa học

4️⃣  SO SÁNH ĐÁP ÁN
    Mở: Exercises/1_beginner_solutions.py
    So sánh code của bạn
    Thời gian: 15-30 phút
    Mục tiêu: Học từ những cách khác

5️⃣  LẶP LẠI NGÀY HÔM SAU
    Học Lesson 2
    Làm tất cả bài tập
    Tổng thời gian mỗi ngày: 2-3 giờ
    Mục tiêu: Xây dựng momentum

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 GOLDEN RULES:

   ✅ Code mỗi ngày - Consistency > Intensity
   ✅ Type code - Đừng copy-paste
   ✅ Debug - Đừng nhìn đáp án ngay
   ✅ Thực hành - Bài tập + Projects
   ✅ Ghi chú - Viết notes riêng
   ✅ Tìm hiểu - Google & đọc docs

❌ MISTAKES TO AVOID:

   ❌ Nhảy cóc các level
   ❌ Xem hết video rồi code
   ❌ Copy-paste code
   ❌ Bỏ qua bài tập
   ❌ Học mà không thực hành

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📈 TIMELINE:

Week 1-2:  Learn Lesson 1-2, Do Exercises, Start Project 1
Week 3-4:  Learn Lesson 3-4, Do More Exercises, Refactor Project 1
Week 5-6:  Learn Lesson 5, Intermediate Exercises, Project 2-3
Week 7-8+: Libraries, Algorithms, Own Projects

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 SUCCESS METRICS:

   ✓ Viết được hàm tái sử dụng
   ✓ Thiết kế được class & object
   ✓ Xử lý được file & exception
   ✓ Sử dụng được thư viện
   ✓ Tạo được project hoàn chỉnh
   ✓ Có thể giúp người khác debug code
    """)

# Run
if __name__ == "__main__":
    print_getting_started()
    print("\n")
    main_menu()
