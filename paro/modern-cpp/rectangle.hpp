#pragma once

#include "Shape.hpp"

class Rectangle : public Shape
{
public:
    Rectangle(double x, double y);
    Rectangle(Color c);
    Rectangle(const Rectangle & other) = default;

    double getArea() const override;
    double getPerimeter() const override;
    double getX() const; // only virtual functions can be marked as final
    double getY() const;
    void print() const;

private:
    Rectangle() = delete;

    double x_ = 1.0;
    double y_ = 1.0;
};
