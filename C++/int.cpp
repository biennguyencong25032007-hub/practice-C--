#include <iostream>

int main(){
    // Declare and initialize integer variables
    int num1, num2;

    // Get user input
    std::cout << "Nhap so thu nhat: ";
    std::cin >> num1;

    std::cout << "Nhap so thu hai: ";
    std::cin >> num2;

    // Perform calculations
    std::cout << "\n=== Ket qua ===" << std::endl;
    std::cout << "Cong: " << num1 << " + " << num2 << " = " << (num1 + num2) << std::endl;
    std::cout << "Tru: " << num1 << " - " << num2 << " = " << (num1 - num2) << std::endl;
    std::cout << "Nhan: " << num1 << " * " << num2 << " = " << (num1 * num2) << std::endl;
    
    if (num2 != 0) {
        std::cout << "Chia: " << num1 << " / " << num2 << " = " << (num1 / num2) << std::endl;
        std::cout << "Chia lay du: " << num1 << " % " << num2 << " = " << (num1 % num2) << std::endl;
    } else {
        std::cout << "Khong the chia cho 0!" << std::endl;
    }

    return 0;
}