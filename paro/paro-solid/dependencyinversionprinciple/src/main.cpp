#include "SqlDataSaver.hpp"
#include "Logger.hpp"

int main()
{
    SqlAdress adress("127.0.0.1");
    auto sqlsaver = std::make_unique<SqlDataSaver>(adress);
    Logger logger(std::move(sqlsaver));
    logger.log("ciekawy log 1");
    logger.log("ciekawy log 2");
    logger.log("ciekawy log 3");
 }
