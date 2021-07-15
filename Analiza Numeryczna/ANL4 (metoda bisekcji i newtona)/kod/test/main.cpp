#include <iostream>

using namespace std;


class FILE_DATA {

public:
    string heading, comment, style;
    int width, height;

    int ***tab;

    FILE_DATA(int width, int height) {
        const int X=width, Y=height, Z=3;

        tab = new int**[X];
        for(int i =0; i<X; i++){
           tab[i] = new int*[Y];
           for(int j =0; j<Y; j++){
               tab[i][j] = new int[Z];
               for(int k = 0; k<Z;k++){
                  tab[i][j][k] = 0;
               }
           }
        }
    }
};

int main()
{
    cout << "Hello world!" << endl;
    return 0;
}
