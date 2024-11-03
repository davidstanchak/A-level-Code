#include <iostream>

int main(){
    int x; // declaration
    x = 5; // asignment
    int y = 6;
    int sum = x + y;

    std::cout << x << std::endl; // displays x // new line also
    std::cout << y << '\n'; // you can make new line like this too
    std::cout << sum << '\n';

    // double is a number including decimal, so a float basically.
    double price = 10.99;
    double grade = 57.6;
    double temperature = 25.1;

    std::cout << price;

    // only one letter
    char grade = 'A';
    char initial = 'D';
    char currency = '£';

    std::cout << initial;

    //boolean, only has true or false, must be in lowercase
    bool student = true;
    bool power = false; // no power

    // STRING, can store whole sentences.

    std::string name = "bean"; // <- how to assign a string.
    std::cout << name;

    //concatenation

    std::cout << "Hello" << name;
    std::cout << "Your are " << x << "Years old :)";




    return 0;
}