from DataWrangling import *
from Dataset2_3 import *
import os
def removeControlReg(country):
  saveFile('country.txt',country)
  os.system('file=country.txt;for i in `cat $file`; do cat /content/drive/MyDrive/RetrieveData/Dataset1/$i/$i*seq_name.txt | grep "control region" > $i.txt; cp -r /content/drive/MyDrive/RetrieveData/Dataset2/$i/fasta /content/drive/MyDrive/RetrieveData/Dataset3/$i/fasta; done')
  if len(openFile(country + '.txt')) > 0:
    # create remove list
    removeList = ''
    for line in openFile(country + '.txt').split('\n'):
      if len(line)>0:
        removeList += '/content/drive/MyDrive/RetrieveData/Dataset3/' + country + '/fasta/' + line.split(": ")[0] + ','
    saveFile('removeList.txt',removeList)
    bash = '''#!/bin/bash
            DataList=removeList.txt
            Field_Separator=$IFS
            IFS=,
            for val in `cat $DataList`; do rm $val; done'''
    # run bash
    saveFile('remove.sh',bash)
    # command line
    os.system('''bash remove.sh
    rm country.txt''')