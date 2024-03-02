import saveFile, openFile
def createHaplo(seq,name):
  saveFile(name,seq)
  saveFile('nameSeq.txt',name)
  # Run Haplogrep Classification
  #fix this
  #!file=nameSeq.txt; for i in `cat $file`; do ./haplogrep classify --in $i --format fasta --output $i.txt;done
  haplo = openFile(name+'.txt').split('\n')[1].split('\t')[1].split('"')[1]
  #fix this
  #!file=nameSeq.txt;for j in `cat $file`; do rm $j*;done
  return haplo