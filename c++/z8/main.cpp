#include "definitions.cpp"
#include <iostream>
#include <conio.h>

using namespace std;
List<int> ls = {2, 1, 3, 5, 6, 0, 1, 3};
void print_list() {
    cout << "List: " << ls << endl;
}

void MainMenu();

void sub_menu_set() {
    system("cls");
    print_list();
    int i, val;
    cout << "Index?" << endl;
    cin >> i;
    cout << "Value?" << endl;
    cin >> val;

    ls.insert(i, val);

    MainMenu();
}

void sub_menu_remove() {
    system("cls");
    print_list();
    int val;
    cout << "Value?" << endl;
    cin >> val;

    ls.remove(val);
    MainMenu();
}

void sub_menu_find() {
    system("cls");
    print_list();
    int val;
    cout << "Value?" << endl;
    cin >> val;

    cout << ls.find(val);
    getch();

    MainMenu();
}

void MainMenu() {
    system("cls");
    print_list();
    cout << "Choose an operation by typing the corresponding number. \n";
    cout << "1) Set value under the given index \n";
    cout << "2) Remove value from the list\n";
    cout << "3) Check if element is present\n";
    cout << "4) Print length of the list\n";
    cout << "5) Check if the list is sorted\n";
    cout << "6) Sort the list\n";

    int num = getch() - '0';

    if(num == 1)
        sub_menu_set();
    if(num == 2)
        sub_menu_remove();
    if(num == 3)
        sub_menu_find();
    if(num == 4) {
        cout << "Length: " << ls.len() << endl;
        getch();
        MainMenu();
    }
    if(num == 5) {
        cout << check<int>(ls) << endl;
        getch();
        MainMenu();
    }

    if(num == 6) {
        sort<int>(ls);
        MainMenu();
    }

    if(num > 4)
        MainMenu();
}






int main()
{
    MainMenu();
    return 0;
}
