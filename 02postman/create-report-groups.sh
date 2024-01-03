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
        REPORT_NAME=$(echo $d| rev |cut -d'/' -f 1)
        # ./02postman//newman-run-report-2024-01-02-21-57-59-022-0.xml
        # revert newman-run-report-2024-01-02-21-57-59-022-0.xml//02postman/.
        FILE_REPORT=$(echo $entry| rev |cut -d'/' -f 1)
        echo "XML File : $FILE_REPORT "
        REPORT_ARN=$(aws codebuild create-report-group --name "ReportTest$REPORT_NAME" --type TEST --export-config reportGroupConf.json -query "reportGroup.{arn:arn}" | grep "arn" | tr -d '"')
        echo "Report Group ReportTest$REPORT_NAME Created with ARN $REPORT_ARN "
    done
done