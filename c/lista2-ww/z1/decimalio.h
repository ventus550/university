#ifndef DECIMALIO_H
#define DECIMALIO_H

typedef unsigned char bool;

static bool is_digit(const char c);

static bool is_space_or_newline(const char c);

int read_decimal();

int trace_decimal(const int d);

#endif
