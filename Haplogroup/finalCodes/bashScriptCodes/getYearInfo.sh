#!/bin/bash
# get year from LOCUS
accList=/content/drive/MyDrive/Haplogroup/finalCodes/others/AccNumForLOCUS.txt
#accList=/content/drive/MyDrive/Haplogroup/finalCodes/others/TheRestDataset3.txt
Field_Separator=$IFS
IFS=,

for acc in `cat $accList`; do
${HOME}/edirect/esummary -db nuccore -id "$acc" -format medline | egrep "LOCUS" >> /content/drive/MyDrive/Haplogroup/finalCodes/others/LOCUS_Data3.txt
done

echo "done LOCUS"

# get year from pubDate
PubList=/content/drive/MyDrive/Haplogroup/finalCodes/others/PubIDForPubDate.txt
Field_Separator=$IFS
IFS=,

for id in `cat $PubList`; do
echo $id >> /content/drive/MyDrive/Haplogroup/finalCodes/others/Pubdate_Data3.txt
${HOME}/edirect/esummary -db pubmed -id "$id" | grep "PubDate" | head -n1 >> /content/drive/MyDrive/Haplogroup/finalCodes/others/Pubdate_Data3.txt
done

echo "done PubDate"