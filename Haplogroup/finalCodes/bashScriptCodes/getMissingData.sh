#!/bin/bash
getMissingData(){  
#string="Large-scale mitochondrial DNA analysis in Southeast Asia reveals evolutionary effects of cultural isolation in the multi-ethnic population of Myanmar"
string=$1
country=$2
for accnum in `${HOME}/edirect/esearch -db nucleotide -query "$string" -sort "Date Released" | ${HOME}/edirect/efetch -format acc`; do
  if ! grep -wq "$accnum" /content/drive/MyDrive/RetrieveData/OldCountryFasta/"$country".fasta
  then
    ${HOME}/edirect/esearch -db nucleotide -query "$accnum" -sort "Date Released" | ${HOME}/edirect/efetch -format fasta >> /content/drive/MyDrive/RetrieveData/OldCountryFasta/"$country".fasta
    #echo "Hi, $accnum"  
  fi
  done
}
#getMissingData "Large-scale mitochondrial DNA analysis in Southeast Asia reveals evolutionary effects of cultural isolation in the multi-ethnic population of Myanmar" "Myanmar"

