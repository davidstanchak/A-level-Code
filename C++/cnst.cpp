#include <iostream>
int main(){
    const double PI = 3.14159; // constants will never change. naming convention: all caps. add prefix of const before variable type.
    double radius = 10;
    double circumference = 2*pi*radius;
    std::cout << circumference <<  "cm";


    return 0;

}