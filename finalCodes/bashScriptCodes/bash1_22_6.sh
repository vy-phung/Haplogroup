#!/bin/bash
DataList=extra.txt
Field_Separator=$IFS
IFS=,
for val in `cat $DataList`; do cp /content/drive/MyDrive/RetrieveData/Dataset1/Malaysia/fasta1/$val /content/drive/MyDrive/RetrieveData/Dataset1/Malaysia/fasta/$val
cp  /content/drive/MyDrive/RetrieveData/Dataset1/Malaysia/fasta1/$val /content/drive/MyDrive/RetrieveData/Dataset2/Malaysia/fasta/$val 
cat /content/drive/MyDrive/RetrieveData/Dataset1/Malaysia/Malay/Malaysia_seq_name.txt  | grep "complete genome" | awk '{print$1}' > complete.txt 
done
