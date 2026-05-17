"""
LESSON 5: LỚP VÀ ĐỐI TƯỢNG (OOP - OBJECT-ORIENTED PROGRAMMING)
===========================================================
Mục tiêu: Hiểu cách tạo class, object, inheritance, và polymorphism

Nội dung:
1. Class & Object
2. Methods & Attributes
3. Constructor (__init__)
4. Inheritance (Kế thừa)
5. Polymorphism
6. Special Methods
"""

print("=" * 70)
print("LESSON 5: LỚP VÀ ĐỐI TƯỢNG (OOP)")
print("=" * 70)

# ===== 1. CLASS & OBJECT CƠ BẢN =====
print("\n[1] CLASS & OBJECT")
print("-" * 70)

class Dog:
    """Lớp để đại diện cho một con chó"""
    
    # Attributes (thuộc tính)
    species = "Canis familiaris"  # Class attribute (thuộc lớp)
    
    def __init__(self, name, age):
        """Constructor - gọi khi tạo object"""
        self.name = name  # Instance attribute (thuộc đối tượng)
        self.age = age
    
    def bark(self):
        """Method - hành động"""
        return f"{self.name} sủa: Woof! Woof!"
    
    def describe(self):
        return f"{self.name} là một con {self.species}, {self.age} tuổi"

# Tạo object
dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

print(f"Dog1: {dog1.name} - {dog1.age} tuổi")
print(f"Dog2: {dog2.name} - {dog2.age} tuổi")
print(f"Species: {dog1.species}")
print(f"dog1.bark(): {dog1.bark()}")
print(f"dog1.describe(): {dog1.describe()}")


# ===== 2. ATTRIBUTES & METHODS =====
print("\n[2] ATTRIBUTES & METHODS")
print("-" * 70)

class Car:
    """Lớp để đại diện cho một chiếc xe"""
    
    def __init__(self, brand, model, year):
        # Instance attributes
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0  # Thuộc tính được thêm trong constructor
    
    # Instance methods
    def accelerate(self, amount):
        """Tăng tốc độ"""
        self.speed += amount
        return f"{self.brand} {self.model} tăng tốc: {self.speed} km/h"
    
    def brake(self, amount):
        """Giảm tốc độ"""
        self.speed -= amount
        return f"Phanh: {self.speed} km/h"
    
    def info(self):
        """Thông tin xe"""
        return f"{self.year} {self.brand} {self.model} - Tốc độ: {self.speed} km/h"
    
    # Class method
    @classmethod
    def create_from_string(cls, car_string):
        """Tạo object từ string"""
        brand, model, year = car_string.split(",")
        return cls(brand, model, int(year))
    
    # Static method
    @staticmethod
    def max_speed():
        """Tốc độ tối đa (không cần self)"""
        return 200

car = Car("Toyota", "Camry", 2020)
print(car.accelerate(60))
print(car.accelerate(30))
print(car.brake(20))
print(car.info())
print(f"Tốc độ tối đa: {Car.max_speed()} km/h")


# ===== 3. ENCAPSULATION (Che giấu dữ liệu) =====
print("\n[3] ENCAPSULATION - Che giấu dữ liệu")
print("-" * 70)

class BankAccount:
    """Tài khoản ngân hàng"""
    
    def __init__(self, holder, balance=0):
        self.holder = holder
        self.__balance = balance  # Private attribute (bắt đầu bằng __)
    
    def deposit(self, amount):
        """Gửi tiền"""
        if amount > 0:
            self.__balance += amount
            return f"Gửi {amount}. Số dư mới: {self.__balance}"
        return "Số tiền phải > 0"
    
    def withdraw(self, amount):
        """Rút tiền"""
        if amount > self.__balance:
            return f"Không đủ tiền. Số dư: {self.__balance}"
        self.__balance -= amount
        return f"Rút {amount}. Số dư mới: {self.__balance}"
    
    def get_balance(self):
        """Getter - lấy giá trị private"""
        return self.__balance

account = BankAccount("Minh", 1000000)
print(account.deposit(500000))
print(account.withdraw(200000))
print(f"Số dư: {account.get_balance()}")


# ===== 4. INHERITANCE (Kế thừa) =====
print("\n[4] INHERITANCE - Kế thừa")
print("-" * 70)

# Lớp cha (Parent/Super class)
class Animal:
    """Lớp cha - Động vật"""
    
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound
    
    def make_sound(self):
        return f"{self.name} kêu: {self.sound}"
    
    def info(self):
        return f"Đây là một con vật: {self.name}"

# Lớp con (Child/Sub class)
class Cat(Animal):
    """Lớp con - Mèo"""
    
    def __init__(self, name, sound="Meow"):
        super().__init__(name, sound)  # Gọi constructor của lớp cha
        self.has_whiskers = True
    
    # Override method
    def info(self):
        return f"Mèo có tên: {self.name}"

class Bird(Animal):
    """Lớp con - Chim"""
    
    def __init__(self, name, sound, can_fly=True):
        super().__init__(name, sound)
        self.can_fly = can_fly
    
    def fly(self):
        if self.can_fly:
            return f"{self.name} bay cao"
        return f"{self.name} không thể bay"

cat = Cat("Miu")
bird = Bird("Chim Sáo", "Chip Chip")

print(cat.make_sound())
print(cat.info())
print(bird.make_sound())
print(bird.fly())


# ===== 5. POLYMORPHISM (Đa hình) =====
print("\n[5] POLYMORPHISM - Đa hình")
print("-" * 70)

class Shape:
    """Lớp cha - Hình dạng"""
    
    def area(self):
        pass

class Rectangle(Shape):
    """Hình chữ nhật"""
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

class Circle(Shape):
    """Hình tròn"""
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        import math
        return math.pi * self.radius ** 2

# Polymorphism - cùng method, khác cách hoạt động
shapes = [
    Rectangle(5, 4),
    Circle(3),
    Rectangle(10, 10)
]

print("Diện tích các hình:")
for shape in shapes:
    print(f"  {shape.__class__.__name__}: {shape.area():.2f}")


# ===== 6. SPECIAL METHODS (Magic Methods) =====
print("\n[6] SPECIAL METHODS - Các phương thức đặc biệt")
print("-" * 70)

class Person:
    """Lớp người"""
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        """Gọi khi print object"""
        return f"Người: {self.name}, {self.age} tuổi"
    
    def __repr__(self):
        """Biểu diễn code của object"""
        return f"Person('{self.name}', {self.age})"
    
    def __len__(self):
        """Cho phép len(object)"""
        return self.age
    
    def __eq__(self, other):
        """So sánh =="""
        return self.name == other.name and self.age == other.age
    
    def __lt__(self, other):
        """So sánh <"""
        return self.age < other.age
    
    def __add__(self, other):
        """Cho phép object1 + object2"""
        return Person(f"{self.name} & {other.name}", max(self.age, other.age))
    
    def __call__(self):
        """Cho phép gọi object như hàm"""
        return f"Xin chào từ {self.name}"

person1 = Person("An", 25)
person2 = Person("Bình", 30)

print(str(person1))  # Gọi __str__
print(repr(person1))  # Gọi __repr__
print(f"Tuổi: {len(person1)}")  # Gọi __len__
print(f"An == Bình: {person1 == person2}")  # Gọi __eq__
print(f"An < Bình: {person1 < person2}")  # Gọi __lt__

person3 = person1 + person2  # Gọi __add__
print(f"person1 + person2: {person3}")

print(person1())  # Gọi __call__


# ===== 7. PROPERTY DECORATOR =====
print("\n[7] PROPERTY DECORATOR - @property")
print("-" * 70)

class Temperature:
    """Quản lý nhiệt độ"""
    
    def __init__(self, celsius):
        self._celsius = celsius  # _ cho biết đây là private
    
    @property
    def celsius(self):
        """Getter"""
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        """Setter - kiểm tra giá trị hợp lệ"""
        if value < -273:
            raise ValueError("Nhiệt độ không thể < -273°C")
        self._celsius = value
    
    @property
    def fahrenheit(self):
        """Thuộc tính tính toán"""
        return (self._celsius * 9/5) + 32

temp = Temperature(25)
print(f"Celsius: {temp.celsius}")
print(f"Fahrenheit: {temp.fahrenheit:.1f}")

temp.celsius = 30
print(f"Cập nhật - Celsius: {temp.celsius}, Fahrenheit: {temp.fahrenheit:.1f}")


# ===== THỰC HÀNH =====
print("\n[THỰC HÀNH] - Tạo class Student")
print("-" * 70)

class Student:
    """Lớp sinh viên"""
    
    total_students = 0  # Class attribute
    
    def __init__(self, name, student_id, gpa=0):
        self.name = name
        self.student_id = student_id
        self.gpa = gpa
        Student.total_students += 1
    
    def study(self, hours):
        self.gpa += hours * 0.1
        return f"{self.name} học {hours} giờ. GPA mới: {self.gpa:.2f}"
    
    def __str__(self):
        return f"Sinh viên: {self.name} ({self.student_id}) - GPA: {self.gpa:.2f}"
    
    @classmethod
    def total_count(cls):
        return f"Tổng sinh viên: {cls.total_students}"

# Sử dụng
student1 = Student("An", "K20001", 3.5)
student2 = Student("Bình", "K20002", 3.7)

print(student1.study(10))
print(student1)
print(student2)
print(Student.total_count())


print("\n" + "=" * 70)
print("✅ HẾT LESSON 5 - OOP")
print("=" * 70)
