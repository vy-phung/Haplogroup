#!/bin/bash
DataList=URL.txt
Field_Separator=$IFS
IFS=,
mkdir /content/drive/MyDrive/OUCRUwork/RetrieveData/tables/GEODownloads/
for val in `cat $DataList`
do wget -P /content/drive/MyDrive/OUCRUwork/RetrieveData/tables/GEODownloads/ $val
done
