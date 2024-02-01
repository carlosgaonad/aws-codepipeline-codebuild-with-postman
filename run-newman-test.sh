#!/usr/bin/env bash

echo "Running run-newman-test.sh $1"
cd "$1" 
pwd
ls -lrt *
for directory in *; do
    # Loop through each subdirectory 
    # and count the number of words in each file
    echo "****** Directory $directory **********"
    cd "$directory"
    ls -lrt
    cd ..
done