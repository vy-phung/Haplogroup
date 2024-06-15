#!/bin/bash
file=/content/drive/MyDrive/RetrieveData/others/extraData/countries.txt
for i in `cat $file`; do echo "$i"
for data in 1 2; do echo "Dataset$data"; ls /content/drive/MyDrive/RetrieveData/"Dataset"$data/$i/fasta | wc -l; done
for term in nonHomoSapiens D-loop ref; do echo "$term"; cat /content/drive/MyDrive/RetrieveData/Dataset1/$i/$i*seq_name.txt | grep "$term" | wc -l; done
done > /content/drive/MyDrive/RetrieveData/others/NumOfFiles.txt
