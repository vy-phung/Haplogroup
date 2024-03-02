from DataWrangling import saveFile, openFile
import pandas as pd
import os
def polymorphism(Input): # the dataset 3: 4932 seq and put them in a 4932-table
  listInput = ','.join(openFile(Input).split('\n')[:-1])
  saveFile('listInput.txt',listInput)
  script = '''#!/bin/bash
    DataList=listInput.txt
    Field_Separator=$IFS
    IFS=,
    for val in `cat $DataList`
    do ./haplogrep classify --in $val --format fasta --extend-report --output $val.txt
    done'''
  saveFile('/content/drive/MyDrive/OUCRUwork/RetrieveData/others/codes/4932polymorphism.sh',script)
  # command line
  os.system('bash /content/drive/MyDrive/OUCRUwork/RetrieveData/others/codes/4932polymorphism.sh')

def tablePoly(inputFile):
  df = {'AccessionNumber':[],'Polymorphism':[]}
  # get the polymorphism
  for i in openFile(inputFile).split('\n')[:-1]:
    accNum = i.split('/')[-1].split('.')[2]
    poly = openFile(i + '.txt').split('\t')[-1].split('"')[1]
    df['AccessionNumber'].append(accNum)
    df['Polymorphism'].append(poly)
  output = pd.DataFrame(df)
  return output