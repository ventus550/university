#pragma once
#include <string>
#include <memory>
#include "solution/Saver.hpp"


class Logger {
public:
    Logger(std::unique_ptr<Saver> s) : dataSaver(std::move(s)) {}

    void log(std::string log)
    {
        dataSaver->saveData(log);
    }

private:
    std::unique_ptr<Saver> dataSaver;
};



