#!/bin/bash

dir="."

directory=`realpath $dir`
gnuscript=`realpath 2d.gnu`

cd "$directory"
find . -type f -name "*.dat" -exec basename {} .dat \; \
    | parallel gnuplot -e "filename=\'{}\'" \"$gnuscript\"

