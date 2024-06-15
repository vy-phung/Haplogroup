#!/bin/bash
# allow the permission to execute the haplogrep
chmod u+x ./haplogrep

# run haplogrep
AccList=DataList=/content/drive/MyDrive/Haplogroup/finalCodes/others/nameAccSeqsDataset3.txt
Field_Separator=$IFS
IFS=,

for val in `cat $AccList`
do ./haplogrep classify --in $val --format fasta  --output mostRecentAcc.txt
cat mostRecentAcc.txt >> /content/drive/MyDrive/Haplogroup/finalCodes/others/Haplo_acc.txt
done