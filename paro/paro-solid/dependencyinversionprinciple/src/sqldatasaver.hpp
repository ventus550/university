#pragma once
#include <string>
#include <iostream>
#include "solution/Saver.hpp"


class SqlAdress
{
public:
    SqlAdress(std::string adress)
        :sqlAdress(adress)  {}

    std::string get()  {return sqlAdress;}
private:
    std::string sqlAdress;
};


class SqlDataSaver : public Saver
{
public:
    SqlDataSaver(SqlAdress adress)
    {
        std::cout << "SQL data Saver created. Connection established at: " << adress.get() << std::endl;
    }

    void saveData(std::string data) override
    {
        std::cout << "saving data to sql db: " << data << std::endl;
    }
};

