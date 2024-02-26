#pragma once

#include <netinet/ip.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <errno.h>
#include <iostream>
#include <fstream>
#include <assert.h>

#define DEBUG 0

#if DEBUG
#define debug(x) x
#define drint(x) cout << x << endl;
#else
#define debug(x)
#define drint(x)
#endif


typedef unsigned int num;
typedef std::string str;

const num
WINSIZE = 450,
SEGSIZE = 1000,
PATIENCE = 3;

const double TIME = 0.1;


