#!/bin/sh

cd $(dirname $0)/src
make
cd ../test
python *.py
