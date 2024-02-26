#include <cstdio>
#include <memory>
#include <string>

using ShoppingList = std::shared_ptr<std::FILE>;

ShoppingList makeFile(const char* filename, const char* flags)
{
    /*Edit here*/
    std::FILE* fp = std::fopen(filename, flags);
    if (fp) return ShoppingList(fp, std::fclose);
    std::fprintf(stderr, "Failed to open file.");
    return ShoppingList();
}

class Partner
{
public:
    void addToFile(std::string element)
    {
        /*Edit here*/
        fprintf(this->shoppingList.get(), "%s\n", element.c_str());
    }
    ShoppingList shoppingList;
};

int main()
{
    Partner boy{};
    boy.shoppingList = makeFile("ShoppingList", "wb");

    Partner girl{};
    girl.shoppingList = boy.shoppingList;
    girl.addToFile("Butter");
    girl.addToFile("Milk");
}
