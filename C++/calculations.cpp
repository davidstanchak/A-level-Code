#include <iostream>

int main() {

    std::cout << "Enter width, then height" << '\n';

    int width;
    int height;
    
    std::cin >> width;
    std::cin >> height;

    int area = width*height;
    std::cout << "The area is " << area;





    return 0;
}