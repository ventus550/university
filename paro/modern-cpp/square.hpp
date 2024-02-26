#pragma once

#include "Rectangle.hpp"

class Square : public Rectangle
{
public:
    Square(double x);
    Square(Color c);
    Square(const Square & other) = default;

    double getArea() const override;
    double getPerimeter() const override;
    void print();

private:
    double getY() = delete; // should not have Y dimension
    Square() = delete;
};
