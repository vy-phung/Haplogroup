import saveFile, openFile
def removeControlReg(country):
  saveFile('country.txt',country)
  #!file=country.txt;for i in `cat $file`; do cat /content/drive/MyDrive/RetrieveData/Dataset1/$i/$i*seq_name.txt | grep "control region" > $i.txt; cp -r /content/drive/MyDrive/RetrieveData/Dataset2/$i/fasta /content/drive/MyDrive/RetrieveData/Dataset3/$i/fasta; done
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
    # fix this command line
    '''! bash remove.sh
    ! rm country.txt'''