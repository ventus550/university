#include "decimalio.c"

int main() {
    int d = read_decimal();

    for(int i = 0; i < d; i++)
        trace_decimal(i*i);
}
