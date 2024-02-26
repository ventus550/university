#include "Square.hpp"
#include <iostream>

Square::Square(double x)
    : Rectangle(x, x)
{}

Square::Square(Color c) : Rectangle(c) {
    this->color = c;
};

double Square::getArea() const
{
    return getX() * getX();
}

double Square::getPerimeter() const
{
    return 4 * getX();
}

void Square::print()
{
    std::cout << "Square:      x: " << getX() << std::endl
              << "          area: " << getArea() << std::endl
              << "     perimeter: " << getPerimeter() << std::endl;
}
