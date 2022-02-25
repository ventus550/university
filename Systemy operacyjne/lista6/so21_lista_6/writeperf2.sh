#!/bin/bash

OPTS="-l 300 -t 300"

runtest() {
  echo "Method: $1"
  strace -e write,writev -c ./writeperf $OPTS $1 > test
  md5sum test
  rm test
  echo ""
}

runtest write
runtest fwrite
runtest fwrite-line
runtest fwrite-full
runtest writev
