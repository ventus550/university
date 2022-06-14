#pragma once
#include <string>

class Saver {
public:
    virtual void saveData(std::string data) =0;
};
