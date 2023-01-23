#!/bin/bash

python pow2.py numbers.txt > output.txt
cmp -s test.txt output.txt || exit 1