#!/bin/bash
# get poly of 4932 seqs
# allow the permission to execute the haplogrep
chmod u+x ./haplogrep

# run haplogrep
AccList=/content/drive/MyDrive/Haplogroup/finalCodes/others/newNameSeqsDataset3_4932.txt
Field_Separator=$IFS
IFS=,

for val in `cat $AccList`
do ./haplogrep classify --in $val --format fasta --extend-report --output mostRecentAcc.txt
cat mostRecentAcc.txt >> /content/drive/MyDrive/Haplogroup/finalCodes/others/FixNameHaplo_acc_extendReport.txt
done
