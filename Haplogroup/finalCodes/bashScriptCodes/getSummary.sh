#!/bin/bash
createListof11CountriesIsolate(){
  countriesList=$1
  SaveFolder=$2
  Field_Separator=$IFS
  IFS=,

  for val in `cat $countriesList`; do
  # create accnum list
  cat RetrieveData\OldCountryFasta
  do ${HOME}/edirect/esearch -db nucleotide -query "Homo sapiens AND mitochondrion AND $val" -sort "Date Released" | ${HOME}/edirect/efetch -format fasta > $SaveFolder/$val.fasta
  done
}
summary(){
  accnum=$1
  key=$2
  ${HOME}/edirect/esummary -db nuccore -id "$accnum" -format medline | egrep "$key" >> /content/drive/MyDrive/RetrieveData/summary/"$accnum"_"$key"_summary.txt 
}
#example:
#summary "KU521409" "isolate"
# create "./Haplogroup/finalCodes/others/countries.txt"