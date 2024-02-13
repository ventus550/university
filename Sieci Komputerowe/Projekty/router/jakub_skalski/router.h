#pragma once

#include <netinet/ip.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <errno.h>
#include <iostream>

// #define DEBUG

#ifdef DEBUG
#define debug(x) x
#else
#define debug(x)
#endif

#define UNREACHABLE 32
#define DIRECT 0

typedef uint32_t ip_t;
typedef uint8_t mask_t;
typedef uint32_t distance_t;

typedef struct __attribute__((__packed__)) {
	ip_t ip;
	mask_t mask;
	distance_t dist;
} vec;