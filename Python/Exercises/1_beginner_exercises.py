"""
BÀI TẬP CƠ BẢN (BEGINNER EXERCISES)
==================================
Các bài tập để luyện tập Lesson 1-2: Basics & Control Flow
"""

print("=" * 50)
print("BÀI TẬP CƠ BẢN - PHẦN 1: BIẾN & OUTPUT")
print("=" * 50)

"""
BÀI 1.1: In thông tin cá nhân
Yêu cầu: Tạo biến lưu tên, tuổi, thành phố. In ra màn hình theo định dạng.
"""
# Viết code ở đây
print("Nguyen Cong Bien \n",
      "sinh nam 2007 \n",
      "dang lam viec va sinh song tai ha noi")
# ...

"""
BÀI 1.2: Tính toán đơn giản
Yêu cầu: Nhập chiều dài và chiều rộng, tính diện tích hình chữ nhật
"""
# Viết code ở đây
chieu_dai = float(input("nhap chieu dai cua hinh chu nhat: "))
chieu_rong = float(input("nhap chieu rong cua hinh chu nhat: "))
dien_tich = chieu_dai * chieu_rong
chu_vi = (chieu_rong + chieu_dai) * 2
print(f"chu vi cua hinh chu nhat la: ",{chu_vi})
print(f"dien tich cua hinh chu nhat la:", {dien_tich})
# ...

"""
BÀI 1.3: Chuyển đổi đơn vị
Yêu cầu: Tạo hàm chuyển km sang m, m sang cm
"""
# Viết code ở đây
def km(km):
      return km * 1000
def m(m):
      return m * 100

print(f"5 km = {km(5)} m")
print(f"2 m = {m(2)} cm")

# ...


print("\n" + "=" * 50)
print("BÀI TẬP CƠ BẢN - PHẦN 2: ĐIỀU KIỆN")
print("=" * 50)

"""
BÀI 2.1: Kiểm tra số chẵn/lẻ
Yêu cầu: Nhập một số, kiểm tra là chẵn hay lẻ
"""
# Viết code ở đây
n = int(input("nhap vao so bat ki: "))
if n % 2 == 0:
      print(f"{n} la so chan!")
      pass
else:
      print(f"{n} la so le!")

# ...

"""
BÀI 2.2: Tìm số lớn nhất
Yêu cầu: Nhập 3 số, tìm số lớn nhất
"""
# Viết code ở đây
a, b, c = 12, 34, 67

if a>=b and a>=c:
      max_num = a
      pass
elif b>= a and b >= c:
      max_num = b
      pass
else:
      max_num = c
      pass
print(f"gia tri lon nhat la: {max_num}")
max_num = max(a, b, c)
print(f"gia tri lon nhat la: {max_num}")
# ...

"""
BÀI 2.3: Xếp loại điểm
Yêu cầu: Nhập điểm, xếp loại: A(90-100), B(80-89), C(70-79), D(<70)
"""
# Viết code ở đây
def xep_loai(diem_thi):
      if diem_thi >= 90:
            return " đạt điểm A"
      elif diem_thi >= 80:
            return " đạt điểm B"
      elif diem_thi >= 70:
            return " đạt điểm C"
      else:
            return "đạt điểm D"
      pass
diem_thi = [95, 85, 73, 63, 42]
for diem_thi in diem_thi:
      print(f"điểm {diem_thi} -> xếp loại: {xep_loai(diem_thi)}")
# ...

"""
BÀI 2.4: Kiểm tra tuổi
Yêu cầu: Nhập tuổi, kiểm tra là trẻ em (< 13), thiếu niên (13-17), người lớn (≥18)
"""
# Viết code ở đây
def xep_loai(do_tuoi):
      if do_tuoi <= 13:
            return " là trẻ em "
      elif do_tuoi < 18:
            return " là thiếu niên "
      else:
            return " là người lớn "
      pass
# test
do_tuoi= [10, 17, 22]
for do_tuoi in do_tuoi:
      print(f"{do_tuoi} đã {xep_loai(do_tuoi)}")

      
# ...


print("\n" + "=" * 50)
print("BÀI TẬP CƠ BẢN - PHẦN 3: LOOP")
print("=" * 50)

"""
BÀI 3.1: In bảng cửu chương
Yêu cầu: In bảng cửu chương từ 1 đến 9
"""
# Viết code ở đây
print("bảng cửu chương ")
for i in range(1, 10):
      print(f"bảng cửu chương {i}: ")
      for j in range(1, 11):
            print(f"{i} x {j} = {i * j}")
      print()
# ...

"""
BÀI 3.2: Tính tổng từ 1 đến N
Yêu cầu: Nhập N, tính tổng 1+2+3+...+N
"""
# Viết code ở đây
n = int(input("nhập vào số n: "))
total = 0
for i in range(1, n+1):
      total += i
print(f"tổng từ {n} là: {total}")
# ...

"""
BÀI 3.3: Dãy Fibonacci
Yêu cầu: In 10 số Fibonacci đầu tiên (0, 1, 1, 2, 3, 5, 8, 13, ...)
"""
# Viết code ở đây
a, b = 0, 1
for _ in range(10):
      print(a, end=" ")
      a, b = b, a + b
print()
# ...

"""
BÀI 3.4: Kiểm tra số nguyên tố
Yêu cầu: Kiểm tra một số có phải số nguyên tố không
"""
# Viết code ở đây

# ...

"""
BÀI 3.5: Hình sao
Yêu cầu: In hình tam giác sao:
*
**
***
****
*****
"""
# Viết code ở đây
# hình tam giác:
print("tam giác sao: ")
for i in range(1, 6):
      print("*" * i)

# hình thoi:
n = 5
for i in range(1, n + 1):
   print(" " * (n - i) + "*" * (2 * i - 1))
   pass
for i in range(n-1, 0 , 1):
      print(" " * (n - i) + "*" * (2*i-1))
# ...


print("\n" + "=" * 50)
print("BÀI TẬP CƠ BẢN - PHẦN 4: STRING & LIST")
print("=" * 50)

"""
BÀI 4.1: Đếm ký tự
Yêu cầu: Nhập chuỗi, đếm số ký tự, số từ
"""
# Viết code ở đây
ky_tu = str(input("nhập vào ký tự: "))
print("số ký tự bạn nhập là: ",len(ky_tu))
# ...

"""
BÀI 4.2: Đảo ngược chuỗi
Yêu cầu: Nhập chuỗi, in chuỗi đảo ngược
"""
# Viết code ở đây
chill = "python hoc kho vl"
dao_chill = chill [::-1]
print(f"chuỗi: {chill}")
print(f"đảo ngược: {dao_chill}")
# ...

"""
BÀI 4.3: Kiểm tra Palindrome
Yêu cầu: Kiểm tra xem chuỗi có phải Palindrome không (ví dụ: "racecar")
"""
# Viết code ở đây
# ...

"""
BÀI 4.4: Sắp xếp list
Yêu cầu: Nhập danh sách số, sắp xếp tăng dần và giảm dần
"""
# Viết code ở đây
# ...

"""
BÀI 4.5: Tìm max/min
Yêu cầu: Nhập danh sách, tìm max, min mà không dùng hàm max/min
"""
# Viết code ở đây
# ...


print("\n" + "=" * 50)
print("HƯỚNG DẪN:")
print("=" * 50)
print("""
1. Đọc kỹ yêu cầu của mỗi bài
2. Tự viết code, không copy-paste đáp án
3. Test code bằng cách chạy nó
4. Nếu lỗi, hãy debug thay vì xem đáp án ngay
5. Sau khi hoàn thành, xem file solutions_beginner.py để so sánh

Happy Coding! 🎉
""")
