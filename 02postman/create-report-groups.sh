#!/usr/bin/env bash

echo "Running create-report-groups.sh"

for d in ./*/ ; do
    # Loop through each subdirectory 
    # and count the number of words in each file
    (cd "$d" && ls -lrt);
done