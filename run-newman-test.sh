#!/usr/bin/env bash

echo "Running run-newman-test.sh $1"
cd "$1" 
pwd
for directory in *; do
    # Loop through each subdirectory 
    # and count the number of words in each file
    echo "****** Directory $directory **********"
    cd "$directory"
    ./../../update-postman-environment.sh $2 $3 $4
    #newman run postman_collection.json --environment postman_environment.json -r junit --reporter-junit-export "newman/$directory"
    cd ..
done