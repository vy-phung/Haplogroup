import openFile, saveFile
def ReadSummary(file): # making the reference name (Kutanan et al. (2017)) and get isolate
  summary = openFile(file)
  isolate,author,title,year,pubID,organism = '','','','','',''
  temporaryMem = {}
  # getting author and title and isolate
  authors = summary.split('AUTHORS')[1].split('\n')[0].split()
  title = ' '.join(summary.split('TITLE')[1].split('\n')[0].split())
  # fix the command line 
  #!ls /content/drive/MyDrive/OUCRUwork/RetrieveData/others/pubmed > pubList.txt
  # list in pubmed
  if 'PUBMED' in summary: # PubmedID.title.isolate.refName
    pubID = summary.split('PUBMED')[1].split()[0]
    if pubID not in openFile('pubList.txt'):
      saveFile('pubmed.txt',pubID)
      # fix the command line
      #!file=pubmed.txt;for id in `cat $file`; do ${HOME}/edirect/esummary -db pubmed -id $id | grep "PubDate" | head -n1 > /content/drive/MyDrive/OUCRUwork/RetrieveData/others/pubmed/$id.txt; done
      if pubID not in temporaryMem:
        year = openFile('/content/drive/MyDrive/OUCRUwork/RetrieveData/others/pubmed/' + pubID + '.txt').split('<PubDate>')[1].split()[0]
        temporaryMem[pubID] = year
    else:
      if len(openFile('/content/drive/MyDrive/OUCRUwork/RetrieveData/others/pubmed/'+pubID+'.txt'))==0:
        if pubID in temporaryMem:
          year = temporaryMem[pubID]
        else:
          saveFile('pubmed.txt',pubID)
          # fix the command line
          #!file=pubmed.txt;for id in `cat $file`; do ${HOME}/edirect/esummary -db pubmed -id $id | grep "PubDate" | head -n1 > /content/drive/MyDrive/OUCRUwork/RetrieveData/others/pubmed/$id.txt; done
          if pubID not in temporaryMem:
            year = openFile('/content/drive/MyDrive/OUCRUwork/RetrieveData/others/pubmed/' + pubID + '.txt').split('<PubDate>')[1].split()[0]
            temporaryMem[pubID] = year
  else: # Unpublised(orJournalorNothing).title.isolate.refName
    if 'Unpublished' in summary:  pubID = 'Unpublished'
    year = summary.split('LOCUS')[1].split('\n')[0].split()[-1].split('-')[-1]
  # getting the isolate
  if 'isolate' in summary:
    if '/isolate=' in summary:
      isolate = summary.split('/isolate=')[1].split('"')[1]
    else:
      isolate = summary.split('isolate')[1].split()[0]
    if ":" in isolate:  isolate.split(":")[-1]
    if  "." in isolate: isolate = isolate.replace('.','_')
    if " " in isolate:  isolate = isolate.replace(' ','_')
    if '\n' in isolate: isolate = isolate.replace('\n','')
  # Identify what kind of organism:
  organism = ' '.join(summary.split('ORGANISM')[1].split('\n')[0].split())
  # create ref name
  if len(authors) > 0:
    refName = authors[0].split(',')[0] + ' et al. ' + '(' + year +')'
  else: refName = authors[0].split(',')[0] + ' (' + year + ')'
  # name of file
  namefile = pubID + '.' + title + '.' + isolate + '.' + refName
  return namefile, isolate, organism