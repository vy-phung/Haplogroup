import pandas as pd
import re
from DataWrangling import openFile, saveFile
import ham_dis, noIso
# ref \n Country: Isolate1: explanation1; Isolate2: explanation2 (signal: location, population, ethnic, language)
# isolate name (ex: , method (take all means doing nothing))
# no isolate (replace with accnum)
def transCode(accIso, ref, country):
  if '</PubDate>' in ref:
    ref = ''.join(ref.split('</PubDate>'))
  trans = openFile('/content/drive/MyDrive/OUCRUwork/RetrieveData/others/translation.txt').split(ref)[1].split(country+": ")[1].split('\n')[0]
  iso, accnum, genIso = accIso.split('.')[1], accIso.split('.')[0], ''
  output, notice , explain, term, locate, popu, ethnic, lang= '','','','', '', '','',''
  if len(iso) > 0: # have isolate
    if "isolate name" in trans:
      if "re.split('\d+',word)[0]" in trans:
        output = re.split('\d+',iso)[0]
      elif "' '.join(word.split('_')[1:-1])" in trans:
        output = ' '.join(iso.split('_')[1:-1])
      elif "take all" in trans:
        output = iso
      elif '''re.findall("[A-Z]*[a-z]*|d+",word)[0]''' in trans:
        output = re.findall("[A-Z]*[a-z]*|d+",iso)[0]
      elif "word.split('_')[-1]" in trans:
        output = iso.split('_')[-1]
      elif "word.split('-')[0]" in trans:
        output = iso.split('-')[0]
    else:  # specify translation code
      if iso not in trans: # for specific case
        iso = ham_dis(trans,iso)
      if len(iso) > 0:
        output = ': '.join(iso.join(trans.split(iso)[1:]).split("; ")[0].split(": ")[1:])
        # if the explain having (signal: location, population, ethnic, language)
        # location
        if "location" in output:
          if ":" not in output.split('location')[1]: # the explain is also the notice
            locate = 'location: ' + ' '.join(output.split(' ')[:-1])
            output = ' '.join(output.split(' ')[:-1])
          else:
            term = output.split('location: ')[1].split(',')[0]
            if ")" in term: term = term.split(')')[0]
            locate = "location: " + term
            output = '('.join(output.split('(')[:-1])
        # population
        if "population" in output:
          if ":" not in output.split('population')[1]: # the explain is also the notice
            popu = 'population: ' + ' '.join(output.split(' ')[:-1])
            output = ' '.join(output.split(' ')[:-1])
          else:
            term = output.split('population: ')[1].split(',')[0]
            if ")" in term: term = term.split(')')[0]
            popu = "population: " + term
            output = '('.join(output.split('(')[:-1])
        # ethnic
        if "ethnic" in output:
          if ":" not in output.split('ethnic')[1]: # the explain is also the notice
            ethnic = 'ethnic: ' + ' '.join(output.split(' ')[:-1])
            output = ' '.join(output.split(' ')[:-1])
          else:
            term = output.split('ethnic: ')[1].split(',')[0]
            if ")" in term: term = term.split(')')[0]
            ethnic = "ethnic: " + term
            output = '('.join(output.split('(')[:-1])
        # language
        if "language" in output:
          if ":" not in output.split('language')[1]: # the explain is also the notice
            lang = 'language: ' + ' '.join(output.split(' ')[:-1])
            output = ' '.join(output.split(' ')[:-1])
          else:
            term = output.split('language: ')[1].split(',')[0]
            if ")" in term: term = term.split(')')[0]
            lang = "language: " + term
            output = '('.join(output.split('(')[:-1])
      else:
        # for "no isolate" already exist in file
        output, ethnic = noIso(accnum,trans)
        # for isolate not exist yet in file
        isoList = re.split('\d+',accIso.split('.')[1])
        for word in isoList:
          if len(word) > 0:
            output = word
            break
  else: # no isolate
    output, ethnic = noIso(accnum,trans)
  return output, locate, popu, ethnic, lang