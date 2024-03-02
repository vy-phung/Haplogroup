import pandas as pd
import transCode
from DataWrangling import openFile, saveFile
def table1(country):
  saveFile('country.txt',country)
  # fix this command line
  #!file=country.txt;for i in `cat $file`; do ls /content/drive/MyDrive/RetrieveData/Dataset3/$i/fasta > list.txt; done
  isolate, accnum, accIso, total, haplo = '','', '',0,''
  refName = openFile('/content/drive/MyDrive/RetrieveData/Dataset1/'+country+'/'+country+'_refname.txt')
  refers, explains, location, population, ethnic, lang, size, countries = [], [] ,[],[],[], [], [] , []
  haplos = {} # haplos = {haploName: {posOfExplain: count}}
  for line in openFile('list.txt').split('\n'):
    if len(line) >0:
      total += 1
      isolate, accnum, haplo = line.split('.')[1], line.split('.')[2], line.split('.')[3]
      accIso = accnum + '.' + isolate
      ref = '.'.join(refName.split(accnum)[1].split('\n')[0].split('.')[4:])
      if len(refName.split(accnum)[1].split('\n')[0].split('.')[1]) == 0 or refName.split(accnum)[1].split('\n')[0].split('.')[1] == "Unpublished":
        ref = 'Unpublished (' + ref + ')'
      if "</PubDate>" in ref:
        ref = ''.join(ref.split('</PubDate>'))
      explain, locate, popu, ethn, lan = transCode(accIso, ref, country)
      # check the unique explain
      if explain not in explains:
        explains.append(explain)
        size.append(1)
        if "Unpublished" in ref:
          refers.append("Unpublished")
        else: refers.append(ref)
        countries.append(country)
        # For the signal: (signal: location, population, ethnic, language)
        if len(locate) > 0: location.append(locate.split("location: ")[1])
        else: location.append("-")
        if len(popu) > 0: population.append(popu.split("population: ")[1])
        else: population.append("-")
        if len(ethn) > 0: ethnic.append(ethn.split("ethnic: ")[1])
        else: ethnic.append("-")
        if len(lan) > 0: lang.append(lan.split("language: ")[1])
        else: lang.append("-")
        # for the haplogroup
        if haplo not in haplos: # not exist haplogroup
          haplos[haplo] = {}
        haplos[haplo][explains.index(explain)] = 1 # same haplogroup but not exist explanation
        #print(explain, ref, accIso)
      else:
        size[explains.index(explain)] += 1
        # for the haplogroup (same and different)
        if haplo in haplos:
          if explains.index(explain) not in haplos[haplo]:
            haplos[haplo][explains.index(explain)] = 1
          else: haplos[haplo][explains.index(explain)] += 1
        else:
          haplos[haplo] = {}
          haplos[haplo][explains.index(explain)] = 1
        # the same explain name but different ref
        if ref not in refers[explains.index(explain)]:
          refers[explains.index(explain)] += ', ' +  ref
  # create table
  data = {'Country': countries,
          'References': refers,
          'Explanation': explains,
          'Ethnicity': ethnic,
          'Location': location,
          'Population': population,
          'Language': lang,
          'Sample size': size }
  df = pd.DataFrame(data)
  # create Haplo table
  for haplo in haplos:
    col = ["-"] * len(explains)
    for pos in haplos[haplo]:
      col[pos] = haplos[haplo][pos]
    haplos[haplo] = col
  haplogroup = pd.DataFrame(haplos)
  # merge table
  total = pd.concat([df,haplogroup], axis = 1)
  return total