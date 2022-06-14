#pragma once

#include "Shape.hpp"

class Circle final : public Shape
{
public:
    Circle(double r);
    Circle(Color c);
    Circle(const Circle & other) = default;

    double getArea() const;
    double getPerimeter() const;
    double getRadius() const;
    void print() const;

private:
    Circle() = delete; // doesn't allow to call default constructor

    double r_ = 1.0;
};
