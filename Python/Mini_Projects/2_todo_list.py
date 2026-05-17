"""
PROJECT 2: TODO LIST (Danh sách việc cần làm)
=============================================
Dự án cơ bản/Trung bình - Quản lý danh sách việc cần làm

Yêu cầu:
- Thêm việc làm
- Xem danh sách
- Đánh dấu hoàn thành
- Xóa việc làm
- Lưu vào file

Skills: List, Dictionary, File I/O, Functions, While Loop, JSON
"""

import json
import os
from datetime import datetime

class TodoList:
    def __init__(self, filename="todos.json"):
        self.filename = filename
        self.todos = self.load_todos()
    
    def load_todos(self):
        """Tải danh sách từ file"""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return []
        return []
    
    def save_todos(self):
        """Lưu danh sách vào file"""
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.todos, f, indent=4, ensure_ascii=False)
    
    def add_todo(self, task, priority="Normal"):
        """Thêm việc làm"""
        todo = {
            "id": len(self.todos) + 1,
            "task": task,
            "completed": False,
            "priority": priority,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")
        }
        self.todos.append(todo)
        self.save_todos()
        print(f"✅ Thêm: {task}")
    
    def view_todos(self):
        """Xem danh sách"""
        if not self.todos:
            print("📝 Danh sách trống")
            return
        
        print("\n" + "=" * 60)
        print("DANH SÁCH VIỆC CẦN LÀM")
        print("=" * 60)
        
        for todo in self.todos:
            status = "✓" if todo["completed"] else "○"
            priority_symbol = "🔴" if todo["priority"] == "High" else "🟡" if todo["priority"] == "Normal" else "🟢"
            
            task_str = f"[{todo['id']}] {status} {todo['task']}"
            if todo["completed"]:
                task_str = "~~" + task_str + "~~"
            
            print(f"{priority_symbol} {task_str}")
            print(f"   Ưu tiên: {todo['priority']} | Tạo: {todo['created_at']}")
        
        print("=" * 60 + "\n")
    
    def complete_todo(self, todo_id):
        """Đánh dấu hoàn thành"""
        for todo in self.todos:
            if todo["id"] == todo_id:
                todo["completed"] = True
                self.save_todos()
                print(f"✅ Hoàn thành: {todo['task']}")
                return
        print("❌ Không tìm thấy việc làm")
    
    def delete_todo(self, todo_id):
        """Xóa việc làm"""
        for i, todo in enumerate(self.todos):
            if todo["id"] == todo_id:
                task = todo["task"]
                self.todos.pop(i)
                self.save_todos()
                print(f"🗑️ Xóa: {task}")
                return
        print("❌ Không tìm thấy việc làm")
    
    def clear_completed(self):
        """Xóa tất cả việc hoàn thành"""
        count = len([t for t in self.todos if t["completed"]])
        self.todos = [t for t in self.todos if not t["completed"]]
        self.save_todos()
        print(f"🗑️ Xóa {count} việc hoàn thành")

def main():
    print("=" * 60)
    print("QUẢN LÝ DANH SÁCH VIỆC CẦN LÀM")
    print("=" * 60)
    
    todo_list = TodoList()
    
    while True:
        print("\nMenu:")
        print("1. Xem danh sách")
        print("2. Thêm việc làm")
        print("3. Hoàn thành việc")
        print("4. Xóa việc")
        print("5. Xóa hoàn thành")
        print("6. Thoát")
        
        choice = input("\nChọn (1-6): ")
        
        if choice == '1':
            todo_list.view_todos()
        
        elif choice == '2':
            task = input("Nhập việc cần làm: ").strip()
            if task:
                priority = input("Ưu tiên (High/Normal/Low) [Normal]: ").strip() or "Normal"
                todo_list.add_todo(task, priority)
            else:
                print("❌ Việc không được để trống")
        
        elif choice == '3':
            try:
                todo_id = int(input("Nhập ID việc hoàn thành: "))
                todo_list.complete_todo(todo_id)
            except ValueError:
                print("❌ ID không hợp lệ")
        
        elif choice == '4':
            try:
                todo_id = int(input("Nhập ID việc xóa: "))
                todo_list.delete_todo(todo_id)
            except ValueError:
                print("❌ ID không hợp lệ")
        
        elif choice == '5':
            todo_list.clear_completed()
        
        elif choice == '6':
            print("👋 Tạm biệt!")
            break
        
        else:
            print("❌ Lựa chọn không hợp lệ")

if __name__ == "__main__":
    main()
