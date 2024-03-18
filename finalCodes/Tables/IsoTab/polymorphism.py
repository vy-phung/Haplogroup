from DataWrangling import saveFile, openFile
import pandas as pd
import os, re
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

def groupHaplo(table):
  table = table.sort_index()
  data = {'Haplogroup':[], 'Haplo':[]}
  haplo = ''
  for h in list(table.index):
    Cap = re.findall('[A-Z]+',h)[0]
    if len(Cap) > 1:
    # 1>Cap (len2-3)
      haplo = Cap
    else:  # 1Cap
      CapNum = re.findall('[A-Z]+\d*',h)[0]
      if len(CapNum) == 2:
    # 1 Cap + 1Num + 1Let (len3)
        haplo = re.findall('[A-Z]+\d+[a-z]{0,1}',h)[0]
      else:
    # 1Cap + >1Num (len3-4) or 1Cap
        haplo = CapNum
    data['Haplogroup'].append(h)
    data['Haplo'].append(haplo)
  # create table
  output = pd.DataFrame(data)
  output = output.set_index(['Haplogroup'])
  return output