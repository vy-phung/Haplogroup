import openFile,saveFile
# fix the haplogroup file name
'''Nếu là D-loop, thì lấy tên Haplogroup theo tên họ đã tìm thấy và đặt ra trước,
không cần chạy lên trên haplogrep nữa. Còn nếu không phải D-loop thì lấy tên chạy lại trên
haplogrep cho chính xác'''
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
        # fix this command line
        '''!file=name.txt;for i in `cat $file`; do rm $i; done
        ! rm name.txt'''
        saveFile('/content/drive/MyDrive/RetrieveData/Dataset1/'+country+'/fasta/'+newName+'.fasta',newSeq)
        # write a bash to remove the old file
        #bash = '''#!/bin/bash
        #for val in "/content/drive/MyDrive/RetrieveData/Dataset1/''' + country + "/fasta/" + line + '''.fasta"; do rm $val;done'''
        #saveFile('remove.sh',bash)
        #! bash remove.sh
        #! rm remove.sh'''