from DataWrangling import *
from Dataset2_3 import *
import os
# fix the haplogroup file name
'''If it is D-loop sequence, take the already existed name of haplogroup from the papers instead of 
running again Haplogrep. If it is not D-loop which means the haplogroups' names are not known yet, then run haplogrep'''
def haplogroup(country):
  haplo, isolate, newName, newSeq = '','','',''
  DLoop = openFile('/content/drive/MyDrive/RetrieveData/Dataset1/' + country + '/' + country + '_seq_name.txt').split('\n')
  for l in DLoop:
    if "D-loop" in l: # if D-loop then change haplogroup but not then dont change
      line = l.split(": ")[0]
      haplo,isolate = line.split('.')[3], line.split('.')[1]
      # check if same haplogroup name or not
      if haplo != isolate.split('_')[-1]:
        # specify for cambodia; if not same halogroup then take the name from isolate
        newName = '.'.join(line.split('.')[:3]) + '.' + isolate.split('_')[-1]
        #print(line,newName)
        # change the name title in that fasta file and remove old file then save new file
        oldFile = openFile('/content/drive/MyDrive/RetrieveData/Dataset1/'+country+'/fasta/'+line+'.fasta').split('\n')
        newSeq = '>' + newName + '\n' + '\n'.join(oldFile[1:])
        saveFile('name.txt','/content/drive/MyDrive/RetrieveData/Dataset1/'+country+'/fasta/'+line+'.fasta')
        # command line
        os.system('''file=name.txt;for i in `cat $file`; do rm $i; done
        ! rm name.txt''')
        saveFile('/content/drive/MyDrive/RetrieveData/Dataset1/'+country+'/fasta/'+newName+'.fasta',newSeq)
        # write a bash to remove the old file
        bash = '''#!/bin/bash
        #for val in "/content/drive/MyDrive/RetrieveData/Dataset1/''' + country + "/fasta/" + line + '''.fasta"; do rm $val;done'''
        saveFile('remove.sh',bash)
        os.system("bash remove.sh")
        os.system("rm remove.sh")