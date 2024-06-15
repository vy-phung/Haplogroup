#!/bin/bash
#Dataset1 information
DataList=/content/drive/MyDrive/Haplogroup/finalCodes/others/UniqueAccNumForDataset1.txt
Field_Separator=$IFS
IFS=,
for accnum in `cat $DataList`; do 
echo "$accnum" >> /content/drive/MyDrive/Haplogroup/finalCodes/others/Dataset1_accnumInfo.txt
${HOME}/edirect/esummary -db nuccore -id "$accnum" -format medline | egrep "AUTHORS|TITLE|PUBMED|isolate|ORGANISM" >> /content/drive/MyDrive/Haplogroup/finalCodes/others/Dataset1_accnumInfo.txt
done