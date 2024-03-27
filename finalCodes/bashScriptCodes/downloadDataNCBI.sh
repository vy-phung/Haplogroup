#!/bin/bash
function download () {
    # Download and Install Entrez Direct
    sh -c "$(wget -q https://ftp.ncbi.nlm.nih.gov/entrez/entrezdirect/install-edirect.sh -O -)"
    export PATH=${HOME}/edirect:${PATH}

    # run code to get data of 11 countries
    # DataList=/content/drive/MyDrive/OUCRUwork/RetrieveData/others/extraData/countries.txt
    # saveFolder=/content/drive/MyDrive/RetrieveData/OldCountryFasta
    DataList=$folder
    SaveFolder=$saveFolder
    Field_Separator=$IFS
    IFS=,
    for val in `cat $DataList`
    do ${HOME}/edirect/esearch -db nucleotide -query "Homo sapiens AND mitochondrion AND $val" -sort "Date Released" | ${HOME}/edirect/efetch -format fasta
    > $SaveFolder/$val.fasta; done

}

# command line
#source ~/bashScriptCodes/downloadDataNCBI.sh; download /content/drive/MyDrive/OUCRUwork/RetrieveData/others/extraData/countries.txt /content/drive/MyDrive/RetrieveData/OldCountryFasta