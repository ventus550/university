#include <iostream>
#include <stdexcept>

class fat_error : public std::logic_error {
    public:
        fat_error(const std::string& __arg) : std::logic_error(__arg) {};
};

void validateArguments(int argc)
{
    if(argc != 2)
    {
        std::cerr << "You need to pass 1 argument" << std::endl;
        exit(-1);
    }
}

class Resource
{
public:
    void use(const char* arg)
    {
        std::cout << "Using resource. Passed " << *arg << std::endl;
        if (*arg == 'd')
        {
            throw fat_error("Passed d. d is prohibited.");
        }
    }
};


int main(int argc, char* argv[])
{
    validateArguments(argc);

    const char* argument = argv[1];
    Resource* rsc = nullptr;

    try
    {
        rsc = new Resource();
        rsc->use(argument);
    }
    catch (fat_error& e)
    {
        std::cout << e.what() << std::endl;
    }

    delete rsc;
    return 0;
}

