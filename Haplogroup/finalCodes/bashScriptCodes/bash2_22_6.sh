#!/bin/bash
DataList=comGene.txt
Field_Separator=$IFS
IFS=,
for val in `cat $DataList`; do cp /content/drive/MyDrive/RetrieveData/Dataset1/Malaysia/fasta1/$val /content/drive/MyDrive/RetrieveData/Dataset3/Malaysia/fasta/$val
done
