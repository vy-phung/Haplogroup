from DataWrangling import *
from Dataset2_3 import *
import os
# remove mRNA, D-loop, non homo sapiens
def remove(countryFolder, country):
  saveFile('country.txt',countryFolder)
  # command line
  os.system=('file=country.txt; for i in `cat $file`; do ls $i > output.txt; done')
  file = openFile('output.txt')
  removeList = []
  for line in file.split('\n'):
    if len(line) > 0:
      accnum = line.split('.')[2]
      if 'nonHomoSapiens' in line: # remove non homo sapiens by the word "nonHomoSapiens" in haplogroup
        removeList.append('/content/drive/MyDrive/OUCRUwork/RetrieveData/ChinaTaiwan/Dataset2/'+country+'/fasta/'+line)
      else:
        if '_' in accnum: # remove mRNA by the '_' in AccessNumber
          removeList.append('/content/drive/MyDrive/OUCRUwork/RetrieveData/ChinaTaiwan/Dataset2/'+country+'/fasta/'+line)
        # remove D-loop by the appearance of this word on title or definition, ex: DEFINITION  Homo sapiens isolate ET202 D-loop, complete sequence;
        seqName = '.'.join(line.split('.')[:-1]) + ': '
        definition = openFile('/content/drive/MyDrive/OUCRUwork/RetrieveData/ChinaTaiwan/Dataset1/' + country + '/' + country + '_seq_name.txt').split(seqName)[1].split('\n')[0]
        if 'D-loop' in definition:
          removeList.append('/content/drive/MyDrive/OUCRUwork/RetrieveData/ChinaTaiwan/Dataset2/'+country+'/fasta/'+line)
  saveFile('removeList.txt',','.join(removeList))
  script = '''#!/bin/bash
    DataList=removeList.txt
    Field_Separator=$IFS
    IFS=,
    for val in `cat $DataList`
    do rm $val
    done'''
  saveFile('dataset2.sh',script)
  #command line
  os.system('bash dataset2.sh')
  os.system('rm dataset2.sh')
  print('finish')