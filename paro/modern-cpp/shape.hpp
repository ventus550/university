#pragma once

enum class Color : unsigned char {
    PINK = 'p',
    BLUE = 'b',
    RED  = 'r',
    NONE
};

class Shape
{
public:
    Shape() = default;
    Shape(Color c);
    Color color = Color::NONE;

    // cannot override function marked as final
    virtual ~Shape() {}
    virtual double getArea() const = 0;
    virtual double getPerimeter() const = 0;
    virtual void print() const;
};
