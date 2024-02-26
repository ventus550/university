#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <memory>
#include "Shape.hpp"
#include "Rectangle.hpp"
#include "Square.hpp"
#include "Circle.hpp"

using namespace std;

using Collection = vector<shared_ptr<Shape>>;

constexpr long fibb(int n) {
    long x = 0, y = 1;
    while (--n) {
        x += 2 * y;
        y = x - y;
        x -= y;
    }
    return y;
};

auto sortByArea = [](shared_ptr<Shape> first, shared_ptr<Shape> second) -> bool {
    if(first == nullptr || second == nullptr)
        return false;
    return (first->getArea() < second->getArea());
};


auto perimeterBiggerThan20 = [](shared_ptr<Shape> s) -> bool {
    if(s)
        return (s->getPerimeter() > 20);
    return false;
};

auto areaLessThanX = [x = 10](shared_ptr<Shape> s) -> bool {
    if(s)
        return (s->getArea() < x);
    return false;
};

void printCollectionElements(const Collection& collection)
{
    for(auto item : collection)
        if(item)
            item->print();
}

void printAreas(const Collection& collection)
{
    for(auto item : collection)
        if(item)
            cout << item->getArea() << std::endl;
}

void findFirstShapeMatchingPredicate(const Collection& collection,
                                     function<bool(shared_ptr<Shape>)> predicate,
                                     std::string info)
{
    auto iter = std::find_if(collection.begin(), collection.end(), predicate);
    if(*iter != nullptr)
    {
        cout << "First shape matching predicate: " << info << endl;
        (*iter)->print();
    }
    else
    {
        cout << "There is no shape matching predicate " << info << endl;
    }
}

int main()
{
    constexpr long f = fibb(45);
    cout << f << endl;

    Collection shapes = {
        make_shared<Circle>(2.0),
        make_shared<Circle>(3.0),
        nullptr,
        make_shared<Circle>(4.0),
        make_shared<Circle>(4.0),
        make_shared<Rectangle>(10.0, 5.0),
        make_shared<Square>(3.0),
        make_shared<Circle>(4.0)
    };
    printCollectionElements(shapes);

    Color color = Color::PINK;
    Square sq(color);
    cout << "color " << char(sq.color) << endl;


    cout << "Areas before sort: " << std::endl;
    printAreas(shapes);

    std::sort(shapes.begin(), shapes.end(), sortByArea);

    cout << "Areas after sort: " << std::endl;
    printAreas(shapes);

    auto square = make_shared<Square>(4.0);
    shapes.push_back(square);

    findFirstShapeMatchingPredicate(shapes, perimeterBiggerThan20, "perimeter bigger than 20");
    findFirstShapeMatchingPredicate(shapes, areaLessThanX, "area less than 10");

    return 0;
}

