"""
STUDY PROGRESS TRACKER - THEO DÕI TIẾN ĐỘ HỌC TẬP
==================================================
File để theo dõi tiến độ học của bạn
"""

# Hướng dẫn: Thay True/False để đánh dấu hoàn thành

PROGRESS = {
    "LESSON 1 - BASICS": {
        "status": "not_started",  # not_started, in_progress, completed
        "date_started": "",
        "date_completed": "",
        "notes": "Học về biến, print, input, kiểu dữ liệu",
        "subtopics": {
            "Print statement": False,
            "Biến & gán giá trị": False,
            "Kiểu dữ liệu (int, float, str, bool)": False,
            "Toán tử": False,
            "Comments": False,
        },
        "exercises": {
            "Bài 1.1 - In thông tin cá nhân": False,
            "Bài 1.2 - Tính diện tích": False,
            "Bài 1.3 - Chuyển đổi đơn vị": False,
        },
        "projects": {
            "Project 1 - Calculator": False,
        }
    },
    
    "LESSON 2 - CONTROL FLOW": {
        "status": "not_started",
        "date_started": "",
        "date_completed": "",
        "notes": "If/elif/else, while, for, break, continue",
        "subtopics": {
            "If/Elif/Else": False,
            "Toán tử logic (and, or, not)": False,
            "While loop": False,
            "For loop": False,
            "Break, Continue, Pass": False,
            "Nested loop": False,
        },
        "exercises": {
            "Bài 2.1 - Kiểm tra chẵn/lẻ": False,
            "Bài 2.2 - Tìm số lớn nhất": False,
            "Bài 2.3 - Xếp loại điểm": False,
            "Bài 2.4 - Kiểm tra tuổi": False,
            "Bài 3.1 - Bảng cửu chương": False,
            "Bài 3.2 - Tính tổng": False,
            "Bài 3.3 - Dãy Fibonacci": False,
            "Bài 3.4 - Kiểm tra số nguyên tố": False,
            "Bài 3.5 - Hình sao": False,
        },
        "projects": {
            "Project 1 - Calculator (Hoàn thiện)": False,
        }
    },
    
    "LESSON 3 - DATA STRUCTURES": {
        "status": "not_started",
        "date_started": "",
        "date_completed": "",
        "notes": "List, Tuple, Dictionary, Set, Slicing",
        "subtopics": {
            "List - tạo, truy cập, modify": False,
            "List - methods (append, insert, remove, etc)": False,
            "Tuple - bất biến": False,
            "Dictionary - key-value": False,
            "Set - tập hợp": False,
            "Slicing - cắt chuỗi": False,
            "List Comprehension": False,
        },
        "exercises": {
            "Bài 4.1 - Đếm ký tự": False,
            "Bài 4.2 - Đảo ngược chuỗi": False,
            "Bài 4.3 - Kiểm tra Palindrome": False,
            "Bài 4.4 - Sắp xếp list": False,
            "Bài 4.5 - Tìm max/min": False,
            "Bài 1.1 (Intermediate) - Thống kê text": False,
            "Bài 1.2 - Merge dictionaries": False,
            "Bài 1.3 - Transpose matrix": False,
            "Bài 1.4 - Dict to List": False,
        },
        "projects": {
            "Project 2 - To-Do List": False,
        }
    },
    
    "LESSON 4 - FUNCTIONS": {
        "status": "not_started",
        "date_started": "",
        "date_completed": "",
        "notes": "Định nghĩa hàm, parameters, return, lambda, *args, **kwargs",
        "subtopics": {
            "Định nghĩa hàm cơ bản": False,
            "Parameters & Arguments": False,
            "Return values": False,
            "Default arguments": False,
            "*args (variadic positional)": False,
            "**kwargs (variadic keyword)": False,
            "Lambda functions": False,
            "Scope (global, local, nonlocal)": False,
            "Docstrings": False,
            "Decorators (cơ bản)": False,
        },
        "exercises": {
            "Bài 2.1 (Intermediate) - Decorator đo thời gian": False,
            "Bài 2.2 - Memoization": False,
            "Bài 2.3 - Higher-order functions": False,
        },
        "projects": {
            "Refactor Project 1 & 2 với functions": False,
        }
    },
    
    "LESSON 5 - OOP (OBJECT-ORIENTED PROGRAMMING)": {
        "status": "not_started",
        "date_started": "",
        "date_completed": "",
        "notes": "Class, Object, Inheritance, Polymorphism, Encapsulation",
        "subtopics": {
            "Class & Object - cơ bản": False,
            "Attributes & Methods": False,
            "Constructor (__init__)": False,
            "Inheritance (kế thừa)": False,
            "Polymorphism (đa hình)": False,
            "Encapsulation (che giấu dữ liệu)": False,
            "Special Methods (__str__, __eq__, etc)": False,
            "@property decorator": False,
            "@classmethod, @staticmethod": False,
        },
        "exercises": {
            "Bài 3.1 (Intermediate) - Bank Account System": False,
            "Bài 3.2 - Shape Hierarchy": False,
            "Bài 3.3 - Library Management": False,
            "Bài 3.4 - Employee Management": False,
        },
        "projects": {
            "Project 3 - Guessing Game": False,
            "Refactor Projects với OOP": False,
        }
    },
    
    "LESSON 6 - FILE I/O & EXCEPTION": {
        "status": "not_started",
        "date_started": "",
        "date_completed": "",
        "notes": "Đọc/ghi file, xử lý lỗi, exception handling",
        "subtopics": {
            "Đọc file (read, readlines)": False,
            "Ghi file (write, append)": False,
            "Context Manager (with statement)": False,
            "Try/Except/Finally": False,
            "Raising Exceptions": False,
            "Custom Exceptions": False,
            "JSON processing": False,
            "CSV processing": False,
        },
        "exercises": {
            "Bài 4.1 (Intermediate) - CSV Processing": False,
            "Bài 4.2 - JSON Configuration": False,
            "Bài 4.3 - Log File Parser": False,
        },
        "projects": {
            "Thêm file I/O vào To-Do List": False,
            "Thêm file I/O vào Guessing Game": False,
        }
    },
    
    "LESSON 7 - MODULES & PACKAGES": {
        "status": "not_started",
        "date_started": "",
        "date_completed": "",
        "notes": "Import modules, tạo module riêng, pip, virtual environment",
        "subtopics": {
            "Import & modules": False,
            "Tạo module riêng": False,
            "Tạo package": False,
            "Pip & package installation": False,
            "Virtual environment (venv)": False,
            "__name__ == '__main__'": False,
        },
        "projects": {
            "Organize projects thành modules": False,
        }
    },
    
    "LIBRARIES & FRAMEWORKS": {
        "status": "not_started",
        "date_started": "",
        "date_completed": "",
        "notes": "Học các thư viện phổ biến",
        "libraries": {
            "os & sys (Hệ thống)": False,
            "math & random (Toán học)": False,
            "datetime (Ngày giờ)": False,
            "json & csv (Data)": False,
            "regex (Regular expressions)": False,
            "collections (Cấu trúc dữ liệu)": False,
            "itertools & functools": False,
            "requests (Web scraping)": False,
            "flask (Web framework)": False,
            "pandas (Data science)": False,
            "numpy (Numerical)": False,
        },
        "projects": {
            "Web Scraper project": False,
            "Data Analysis project": False,
            "Simple Web App": False,
        }
    },
    
    "ALGORITHMS & PROBLEM SOLVING": {
        "status": "not_started",
        "date_started": "",
        "date_completed": "",
        "notes": "Thuật toán, Big O, optimization",
        "subtopics": {
            "Sorting Algorithms": False,
            "Search Algorithms": False,
            "Time & Space Complexity": False,
            "Recursion": False,
            "Dynamic Programming": False,
        },
        "exercises": {
            "Bài 5.1 (Intermediate) - Sorting Algorithms": False,
            "Bài 5.2 - Search Algorithms": False,
            "Bài 5.3 - Dynamic Programming": False,
        },
        "projects": {
            "Algorithm implementations": False,
        }
    },
}

# ===== Hàm Helper =====

def print_progress_summary():
    """In tóm tắt tiến độ"""
    print("\n" + "=" * 70)
    print("TÓML TẮT TIẾN ĐỘ HỌC TẬP")
    print("=" * 70)
    
    total_sections = len(PROGRESS)
    completed_sections = sum(1 for section in PROGRESS.values() if section["status"] == "completed")
    in_progress_sections = sum(1 for section in PROGRESS.values() if section["status"] == "in_progress")
    
    completion_rate = (completed_sections / total_sections) * 100 if total_sections > 0 else 0
    
    print(f"\nTổng sections: {total_sections}")
    print(f"Đã hoàn thành: {completed_sections}")
    print(f"Đang học: {in_progress_sections}")
    print(f"Chưa bắt đầu: {total_sections - completed_sections - in_progress_sections}")
    print(f"Tỷ lệ hoàn thành: {completion_rate:.1f}%")
    
    print("\n" + "-" * 70)
    print("Chi tiết từng section:")
    print("-" * 70)
    
    for section_name, section_data in PROGRESS.items():
        status_icon = {
            "not_started": "⭕",
            "in_progress": "🟡",
            "completed": "✅"
        }[section_data["status"]]
        
        print(f"{status_icon} {section_name}")
        print(f"   Status: {section_data['status']}")
        if section_data["date_started"]:
            print(f"   Started: {section_data['date_started']}")
        if section_data["date_completed"]:
            print(f"   Completed: {section_data['date_completed']}")

def print_current_lesson():
    """In bài học hiện tại"""
    print("\n" + "=" * 70)
    print("BÀI HỌC HIỆN TẠI")
    print("=" * 70)
    
    for section_name, section_data in PROGRESS.items():
        if section_data["status"] == "in_progress" or section_data["status"] == "not_started":
            print(f"\n📚 {section_name}")
            print(f"   Note: {section_data['notes']}")
            print("\n   Subtopics:")
            for topic, completed in section_data.get("subtopics", {}).items():
                icon = "✓" if completed else "○"
                print(f"      [{icon}] {topic}")
            break

def print_next_steps():
    """In các bước tiếp theo"""
    print("\n" + "=" * 70)
    print("BƯỚC TIẾP THEO")
    print("=" * 70)
    
    print("""
1. NGÀY HÔM NAY:
   → Chạy Lessons/1_basics_lesson.py
   → Làm 3 bài tập đầu tiên từ Exercises/1_beginner_exercises.py
   → Mất khoảng 30-45 phút

2. NGÀY THỨ 2:
   → Hoàn thành tất cả bài tập từ Lesson 1-2
   → Bắt đầu Project 1: Calculator
   → Mất khoảng 1 giờ

3. TUẦN THỨ 2:
   → Hoàn thành Lesson 3 - Data Structures
   → Làm tất cả exercises
   → Hoàn thành Project 1 hoàn toàn

4. TUẦN THỨ 3-4:
   → Lesson 4 - Functions
   → Lesson 5 - OOP
   → Project 2: To-Do List
   → Project 3: Guessing Game

5. SAU ĐÓ:
   → Học thư viện
   → Tạo project riêng
   → Tham gia coding challenges
   → Tìm internship/project thực tế
    """)

if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("📊 PYTHON LEARNING PROGRESS TRACKER")
    print("=" * 70)
    
    print("""
Hướng dẫn sử dụng:
1. Sửa PROGRESS dictionary: Thay True khi hoàn thành
2. Chạy script để xem tóm tắt tiến độ
3. Cập nhật status: "not_started" → "in_progress" → "completed"
4. Ghi chú ngày bắt đầu & hoàn thành

Example:
    PROGRESS["LESSON 1 - BASICS"]["status"] = "in_progress"
    PROGRESS["LESSON 1 - BASICS"]["subtopics"]["Print statement"] = True
    """)
    
    # Hiển thị menu
    while True:
        print("\n" + "-" * 70)
        print("Menu:")
        print("1. Xem tóm tắt tiến độ")
        print("2. Xem bài học hiện tại")
        print("3. Xem bước tiếp theo")
        print("4. Thoát")
        
        choice = input("\nChọn (1-4): ")
        
        if choice == '1':
            print_progress_summary()
        elif choice == '2':
            print_current_lesson()
        elif choice == '3':
            print_next_steps()
        elif choice == '4':
            print("\nGood luck with your Python journey! 🚀")
            break
        else:
            print("Lựa chọn không hợp lệ!")
