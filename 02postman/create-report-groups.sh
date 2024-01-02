#!/usr/bin/env bash

echo "Running create-report-groups.sh"
cd  newman/
for d in ./*/ ; do
    # Loop through each subdirectory 
    # and count the number of words in each file
    echo "List Directory $d"
    for entry in "$d"/*
    do
        echo "File $entry on $d"
        SUBSTRING=$(echo $entry| cut -d'/' -f 4)
        echo "XML File : $SUBSTRING "
    done
done