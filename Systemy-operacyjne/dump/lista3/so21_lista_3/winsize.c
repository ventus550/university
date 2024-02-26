#include <sys/ioctl.h>
#include "include/csapp.h"


/*
    SIGWINCH - sygnał zmiany rozmiaru okna
    TIOCGWINSZ - typ requesta, w tym przypadku prosimy o rozmiar okna
*/


void sigwinch_handler(int sig)
{
    /* pobieramy wymiary okna structem winsize

            struct winsize {
                unsigned short ws_row;
                unsigned short ws_col;
                unsigned short ws_xpixel;
                unsigned short ws_ypixel;
            }
    */

    struct winsize window;
    ioctl(STDIN_FILENO, TIOCGWINSZ, &window);
    printf("row: %d col: %d\n", window.ws_row, window.ws_col);
}

int main()
{
    signal(SIGWINCH, sigwinch_handler);
    while (1) pause();
}
