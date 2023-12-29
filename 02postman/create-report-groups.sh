#!/usr/bin/env bash

echo "Running create-report-groups.sh"
cd  newman/
for d in ./*/ ; do
    # Loop through each subdirectory 
    # and count the number of words in each file
    echo "List Directory $d"
    (cd "$d" && ls -lrt);
done