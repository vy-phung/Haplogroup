import saveFile
import openFile
''' This is a function that splits a big country fasta file including multiple sequences into each fasta file containing only 1 sequence.
When splitting, it also labels, and figures out if there is any sequence doesnt have haplogroup and run
haplogrep for that unhaplogroup sequence, save it and then move on to next sequence until there is no sequence in that country fasta file.'''
def SplitSeq(nameFile, country,seqFolder,seqNameFolder,newCountryFasta, exist):
  file = openFile(nameFile)
  seqs = file.split('>')
  dic = ''
  newCountryFile = ''
  refName, accnum = '', ''
  if exist == 'Yes':
    saveFile('seqFolder.txt',seqFolder)
    # fix this code here into python instead of command line
    #!file=seqFolder.txt;for i in `cat $file`; do ls $i > Seqlist.txt; done
  else: saveFile('Seqlist.txt','')
  for seq in seqs:
    if len(seq) > 0:
      name = seq.split('\n')[0]
      accnum = name.split('.')[0]
      if accnum in openFile('Seqlist.txt') and len(openFile('/content/drive/MyDrive/OUCRUwork/RetrieveData/others/AccessNumber/' + accnum + '.txt')) > 0:
        AccNum = accnum
        ethnic = openFile('Seqlist.txt').split(accnum)[0].split('\n')[-1].split('.')[1]
        haplo = openFile('Seqlist.txt').split(accnum)[1].split('\n')[0].split('.')[1]
        ref,isolate,organism = ReadSummary('/content/drive/MyDrive/OUCRUwork/RetrieveData/others/AccessNumber/' + AccNum + '.txt')
      else:
        AccNum, ethnic, haplo, ref, organism = createName(name)
        # Vietnam.Ethnic(nếu có).Accessnumber.Haplogroup
        if haplo == '':
          if organism not in ['Homo sapiens', 'Homo Sapiens']:
            haplo = 'nonHomoSapiens'
          elif '_' in AccNum: haplo = 'ref'
          elif 'mRNA' in name:  haplo = 'mRNA'
          else:
            nameHaplo = seqNameFolder + AccNum + '.fasta'
            sequence = '>' + seq
            haplo = createHaplo(sequence,nameHaplo)
            print(haplo,name)
      newName = country + '.' + ethnic + '.' + AccNum + '.' + haplo
      # translation name
      dic += newName + ': ' + name + '\n'
      refName += country + '.' + AccNum + '.' + ref + '\n'
      # create file country.ethnic.
      # change name of this file
      headTitle = '>' + newName
      newSeq = headTitle + '\n' + '\n'.join(seq.split('\n')[1:])
      # save each seq file
      nameSeq = seqFolder + newName + '.fasta'
      saveFile(nameSeq,newSeq)
      # add into new country file
      newCountryFile += newSeq
  # Save file name of each sequence
  seqNameFold = seqNameFolder + country + '_seq_name.txt'
  saveFile(seqNameFold,dic)
  # Save RefName file
  Ref = seqNameFolder + country + '_refname.txt'
  saveFile(Ref,refName)
  # Save new Country file
  nameFasta = newCountryFasta + country + '.fasta'
  saveFile(nameFasta,newCountryFile)