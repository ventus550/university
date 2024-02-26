#pragma once

#include <iostream>

struct Point{
    int x,y;
    Point operator+(const Point other)
    {
        Point result{.x = x + other.x, .y = y + other.y}
        x += other.x;
        y += other.y;
    }
};

std::ostream& operator<<(std::ostream& out, const Point& p)
{
    return out << "(" << p.x << " " << p.y << ")";
}