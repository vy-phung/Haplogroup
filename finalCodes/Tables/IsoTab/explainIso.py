import transCode
from DataWrangling import saveFile, openFile
import pandas as pd
# country, isolate, explanation, ethnicity, language, language family
def explainIso(country):
  saveFile('country.txt',country)
  # fix this command line
  #!file=country.txt;for i in `cat $file`; do ls /content/drive/MyDrive/OUCRUwork/RetrieveData/Dataset3/$i/fasta > list.txt; done
  isolate, accnum, accIso = '','', ''
  refName = openFile('/content/drive/MyDrive/OUCRUwork/RetrieveData/Dataset1/'+country+'/'+country+'_refname.txt')
  output = ''
  # create table
  table = {'Country':[],
           'Isolate':[],
           'AccessionNumber':[],
           'Explanation':[]}
  for line in openFile('list.txt').split('\n'):
    if len(line) >0:
      isolate, accnum = line.split('.')[1], line.split('.')[2]
      accIso = accnum + '.' + isolate
      ref = '.'.join(refName.split(accnum)[1].split('\n')[0].split('.')[4:])
      explain, locate, popu, ethn, lan = transCode(accIso, ref, country)
      table['Country'].append(country)
      table['Isolate'].append(isolate)
      table['AccessionNumber'].append(accnum)
      table['Explanation'].append(explain)
  # create dataframe
  #if str(len(table['Country'])) == openFile('/content/drive/MyDrive/OUCRUwork/RetrieveData/others/lengthReport.txt').split(country)[1].split('\n')[0].split(', ')[1]:
  output = pd.DataFrame(table)
  output = output.set_index(['Country'])
  return output