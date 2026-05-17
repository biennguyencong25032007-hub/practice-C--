"""
PROJECT 1: CALCULATOR (Máy tính)
================================
Dự án cơ bản - Xây dựng một máy tính đơn giản

Yêu cầu:
- Thực hiện các phép toán cơ bản (+, -, *, /)
- Cho phép người dùng nhập liên tục
- Xử lý lỗi chia cho 0
- Cho phép thoát chương trình

Skills: Variables, Input, If/Else, Functions, While Loop, Try/Except
"""

print("=" * 50)
print("MÁYTÍNH CẤP SỐ CƠ BẢN")
print("=" * 50)

def add(x, y):
    """Cộng hai số"""
    return x + y

def subtract(x, y):
    """Trừ hai số"""
    return x - y

def multiply(x, y):
    """Nhân hai số"""
    return x * y

def divide(x, y):
    """Chia hai số"""
    if y == 0:
        return None
    return x / y

def calculator():
    print("\nMáy tính đơn giản")
    print("Chọn phép toán:")
    print("1. Cộng")
    print("2. Trừ")
    print("3. Nhân")
    print("4. Chia")
    print("5. Thoát")
    
    while True:
        choice = input("\nNhập lựa chọn (1/2/3/4/5): ")
        
        if choice == '5':
            print("Cảm ơn, tạm biệt!")
            break
        
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Nhập số thứ nhất: "))
                num2 = float(input("Nhập số thứ hai: "))
            except ValueError:
                print("Vui lòng nhập số hợp lệ!")
                continue
            
            if choice == '1':
                print(f"Kết quả: {num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"Kết quả: {num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Kết quả: {num1} × {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                if num2 == 0:
                    print("Lỗi: Không thể chia cho 0!")
                else:
                    print(f"Kết quả: {num1} ÷ {num2} = {divide(num1, num2):.2f}")
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")

if __name__ == "__main__":
    calculator()


print("\n" + "=" * 50)
print("PROJECT 1 HOÀN THÀNH!")
print("=" * 50)
