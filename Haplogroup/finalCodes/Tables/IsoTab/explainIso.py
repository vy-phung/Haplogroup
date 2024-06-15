from Haplogroup.finalCodes.DataWrangling.Dataset3 import summaryForDataset3
from Haplogroup.finalCodes.DataWrangling import openFile
from Haplogroup.finalCodes.Tables.IsoTab import getNewIsolate, TransCode, Haplo
import pandas as pd
def explainIso(listOfNames):
  output, id = '', -1
  # create table
  table = {'ID': [],
           'Reference': [],
           'pubmedID': [],
           'title':[],
           'year':[],
           'Author(s)':[],
           'AccessionNumber':[],
           'name':[],
           'Country':[],
           'Isolate':[],
           'Explanation':[],
           'Ethnicity':[],
           'Location': [],
           'Language': [],
           'Population': [],
           'haplo':[],
           'haplogroup1': [],
           'haplogroup2': [],
           'haplogroup3': [],
           "Polymorphism":[]}         
  for name in listOfNames:
    id += 1
    loc, lan, eth, popu = '','','',''
    country, isolate, accnum, haplo = '','','',''
    # example of name: Brunei.BRU18.KU131308.M7c1c3
    country, isolate, accnum, haplo = name.split(".")[0],name.split(".")[1],name.split(".")[2],name.split(".")[3]
    originalIsolate = name.split(".")[1]
    s = summaryForDataset3.SummaryDataset3(accnum)
    year = s.getYears()
    ref = s.getAuthors(year)
    print(name, listOfNames.index(name))
    '''fix Isotab
    1. Use exact time, if it is wrong or not exist => move to same ref authors
    2. Try original isolate => not have => new isolate => not have =>also that new isolate but decrease # of letter such as 3 to 2 and then 2 to 1
    3. Nothing then keep isolate name
    - Isotab: Vietnam but FullTab: VN or Viet Nam
    - duplicate seqs'''
    # get isolate to do explanation
    if len(isolate) > 0:
      if len(getNewIsolate.getNewIsolate(isolate))>0:
        transFile = openFile.openFile("/content/drive/MyDrive/Haplogroup/finalCodes/Tables/translation.txt")
        if ref.split(" (")[0] in transFile:
          trans = TransCode.transCode(ref, country, accnum, isolate)
          # first original isolate
          getInfo, isolate = trans.getGeneralInfo("No", isolate)[0], trans.getGeneralInfo("No", isolate)[1]
          #print(getInfo)
          #print(getInfo, isolate)
          if getInfo == "Try new iso":
            isolate = getNewIsolate.getNewIsolate(isolate)
            getInfo, isolate = trans.getGeneralInfo("Yes", isolate)[0], trans.getGeneralInfo("Yes", isolate)[1]
            #print(getInfo)
          typeOfExplain = trans.checkWhichKindOfExplain(getInfo)
          if len(typeOfExplain) == 0:
            explain, option, info = trans.explain(getInfo,isolate)
          elif typeOfExplain[0] == "same pattern":  explain, option, info = trans.samePattern(getInfo, originalIsolate)
          elif typeOfExplain[0] == "no change": explain, option, info = trans.noChange(getInfo, originalIsolate)
          elif typeOfExplain[0] == "no isolate": explain, option, info = trans.noIsolate(getInfo)
          if len(option) > 0:
            for o in option:
              if o == "location": loc = trans.getLocation(option,explain,info)
              elif o == "language": lan = trans.getLanguage(option,explain,info)
              elif o == "ethnic": eth = trans.getEthnic(option,explain,info)
              elif o == "population": popu = trans.getPopulation(option,explain,info)
        else:
          explain = isolate
      else:
        explain = "Unknown"
    else:
      explain = "Unknown"
    # for the summary of dataset 3
    pubId = s.getPubMedID()
    title = s.getTitle()
    #print(pubId, title, ref)
    if title == "Direct Submission":
      reference = title + " " + ref
    else: reference = pubId + " " + title + " " + ref
    poly = s.getPoly()
    # classify haplo from original haplogroup
    h = Haplo.Haplo(haplo)
    haplo1 = h.haplo1()
    haplo2 = h.haplo2()
    haplo3 = h.haplo3()
    if len(explain)==0:
      break
    # add into the table
    table['ID'].append(str(id))
    table['Reference'].append(reference)
    table['pubmedID'].append(pubId)
    table['title'].append(title)
    table['year'].append(year)
    table['Author(s)'].append(ref)
    table['AccessionNumber'].append(accnum)
    table['name'].append(name)
    table['Country'].append(country)
    table['Isolate'].append(originalIsolate)
    table['Explanation'].append(explain)
    table['Ethnicity'].append(eth)
    table['Location'].append(loc)
    table['Language'].append(lan)
    table['Population'].append(popu)
    table['haplo'].append(haplo)
    table['haplogroup1'].append(haplo1)
    table['haplogroup2'].append(haplo2)
    table['haplogroup3'].append(haplo3)
    table["Polymorphism"].append(poly)
  # create dataframe
  output = pd.DataFrame(table)
  output = output.set_index(['ID'])
  return output