#!/bin/bash
    DataList=listInput.txt
    Field_Separator=$IFS
    IFS=,
    for val in `cat $DataList`
    do ./haplogrep classify --in $val --format fasta --extend-report --output $val.txt
    done
