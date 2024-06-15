#!/bin/bash
function download () {

    # make directory to save the data
    if ! test -d /content/drive/MyDrive/RetrieveData; then
      mkdir /content/drive/MyDrive/RetrieveData
      mkdir /content/drive/MyDrive/RetrieveData/OldCountryFasta
    else
      if ! test -d /content/drive/MyDrive/RetrieveData/OldCountryFasta; then
      mkdir /content/drive/MyDrive/RetrieveData/OldCountryFasta
      fi
    fi

    # run code to get data of 11 countries
    # DataList=/content/drive/MyDrive/RetrieveData/others/extraData/countries.txt
    # saveFolder=/content/drive/MyDrive/RetrieveData/OldCountryFasta
    DataList=$1
    SaveFolder=$2
    Field_Separator=$IFS
    IFS=,

    for val in `cat $DataList`
    do ${HOME}/edirect/esearch -db nucleotide -query "Homo sapiens AND mitochondrion AND $val" -sort "Date Released" | ${HOME}/edirect/efetch -format fasta > $SaveFolder/$val.fasta
    done

}
