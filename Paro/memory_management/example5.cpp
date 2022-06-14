#include <iostream>
#include <chrono>
#include <memory>

struct Partner {};

std::size_t getCurrentTime()
{
    return std::chrono::system_clock::now().time_since_epoch().count();
}

bool process()
{
    if (getCurrentTime() % 17 == 0) throw 17;
    return true;
}

bool processSecond()
{
	if (getCurrentTime() % 2) throw 3.14;
	return true;
}

void convertMe()
{
    std::unique_ptr<Partner> pFirst = std::make_unique<Partner>();

    if (!process())
        return;

    std::unique_ptr<Partner> pSecond = std::make_unique<Partner>();

    if (!processSecond())
        return;

    process();
}

int main()
{
    try
    {
        convertMe();
    }
    catch(int i)
    {
        std::cout << "Ups: " << i << std::endl;
    }
    catch(double d)
    {
        std::cout << "Ups: " << d << std::endl;
    }
    return 0;
}
