from DataWrangling import *
from Dataset1 import *
import os
def createName(name):
  AccNum, ethnic, haplo = '','',''
  # command line
  os.system("ls /content/drive/MyDrive/OUCRUwork/RetrieveData/others/AccessNumber > list.txt")
  for words in name.split(' '):
    # AccessNumber
    if name.split(' ').index(words) == 0:
      AccNum = words.split('.')[0]
      # create access number summary
      lis = openFile('list.txt')
      if AccNum not in lis:
        saveFile('accnum.txt',AccNum)
        # command line
        os.system('file=accnum.txt;for id in `cat $file`; do ${HOME}/edirect/esummary -db nuccore -id $id -format medline | egrep "AUTHORS|TITLE|JOURNAL|LOCUS|PUBMED|isolate|ORGANISM" > /content/drive/MyDrive/OUCRUwork/RetrieveData/others/AccessNumber/$id.txt;done')
      else:
        if len(openFile('/content/drive/MyDrive/OUCRUwork/RetrieveData/others/AccessNumber/' + AccNum + '.txt')) == 0:
          saveFile('accnum.txt',AccNum)
          # command line
          os.system('file=accnum.txt;for id in `cat $file`; do ${HOME}/edirect/esummary -db nuccore -id $id -format medline | egrep "AUTHORS|TITLE|JOURNAL|LOCUS|PUBMED|isolate|ORGANISM" > /content/drive/MyDrive/OUCRUwork/RetrieveData/others/AccessNumber/$id.txt;done')
      refName,isolate,organism = ReadSummary('/content/drive/MyDrive/OUCRUwork/RetrieveData/others/AccessNumber/' + AccNum + '.txt')
    # Haplogroups
    if words == 'haplogroup':
      haplo = name.split(' ')[name.split(' ').index(words) + 1]
  return AccNum, isolate, haplo, refName, organism