# create translation Code class to read translation text
from Haplogroup.finalCodes.DataWrangling import openFile, saveFile
from Haplogroup.finalCodes.Tables.IsoTab import getNewIsolate
import re
class transCode:
  def __init__(self, ref, country, accnum, isolate):
    self.transFile = openFile.openFile("/content/drive/MyDrive/Haplogroup/finalCodes/Tables/translation.txt")
    self.ref = ref
    self.country = country
    self.accnum = accnum
    self.isolate = isolate
    self.optionals = ["location", "ethnic", "language", "population"]

  # This get newIsolate is the special case of existing isolate but still cannot
  # read in the translation file
  def getGeneralInfo(self, isThatNewIso, iso):
    info = ''
    '''if self.ref not in self.transFile:
        # ex: AY963572 which is Macaulay et al. (2005) but the locus time is 2016 => Macaulay et al. (2016)
        # to fix that, only take author without year
      self.ref = self.ref.split(" (")[0]'''
    '''Firstly still do with the exact ref has the exact time
    If they not exist, then move onto the next having the same authors name but different years'''
    newRefAuthors = self.ref.split(" (")[0]
    generalInfos = self.transFile.split(newRefAuthors)[1:]
    # find the exact same ref first
    if self.ref in self.transFile: # has the exact ref
      genInfo = self.transFile.split(self.ref)[1].split("(Ref)")[0]
      #print(info)
      # find iso in info
      output = self.findIsoInGeneralInfo([genInfo],iso,self.country)
      if len(output) == 1: # has iso
        info = genInfo.split(self.country + ": ")[1].split("\n")[0]
        return [info, iso]
      elif len(output) == 0: # has no iso but still exist exact ref
        # try get new isolate
        if isThatNewIso == "No":
          return ["Try new iso", iso]
        elif isThatNewIso == "Yes":
          # try again the exact info but reducing the number of letter
          newIso = iso[:len(iso)]
          while len(newIso) != 1 and len(output)==0:
            newIso = newIso[:len(newIso)-1]
            output = self.findIsoInGeneralInfo([genInfo],newIso,self.country)
          if len(newIso) == 1 and len(output) == 0:
            # already checked exact ref but still not exist
            output =  self.findIsoInGeneralInfo(generalInfos,iso,self.country)
            # try new iso but still not work then try again until len(iso) is only 1
            newIso = iso[:len(iso)]
            if len(output) == 0:
              while len(newIso) != 1 and len(output)==0:
                newIso = newIso[:len(newIso)-1]
                output = self.findIsoInGeneralInfo(generalInfos,newIso,self.country)
              if len(newIso) == 1 and len(output) == 0:
                if len(generalInfos)==1:
                  output = [generalInfos[0].split("(Ref)")[0]]
                else:
                  for inf in generalInfos:
                    if self.country in inf.split("(Ref)")[0]:
                      output = [inf.split("(Ref)")[0]]
                newIso = iso
          return [output[0], newIso]
    else: # dont have the exact ref
      output = self.findIsoInGeneralInfo(generalInfos,iso,self.country)
      if len(output) == 1:
          return [output[0],iso]
      else:
        if isThatNewIso == "No":
          return ["Try new iso", iso]
        elif isThatNewIso == "Yes":
          output =  self.findIsoInGeneralInfo(generalInfos,iso,self.country)
          # try new iso but still not work then try again until len(iso) is only 1
          newIso = iso[:len(iso)]
          if len(output) == 0:
            while len(newIso) != 1 and len(output)==0:
              newIso = newIso[:len(newIso)-1]
              output = self.findIsoInGeneralInfo(generalInfos,newIso,self.country)
            if len(newIso) == 1 and len(output) == 0:
              if len(generalInfos)==1:
                output = [generalInfos[0].split("(Ref)")[0]]
              else:
                for inf in generalInfos:
                  if self.country in inf.split("(Ref)")[0]:
                    output = [inf.split("(Ref)")[0]]
              newIso = iso
          return [output[0], newIso]

  # Helper method to find Iso in Info
  def findIsoInGeneralInfo(self,infos,iso, country):
    output = []
    for i in infos:
      if len(iso) >0:
        if country in i:
          if iso in i.split(country + ": ")[1].split("\n")[0]:
            output.append(i.split(country + ": ")[1].split("\n")[0])
    return output

  def checkWhichKindOfExplain(self, generalInfo):
    typeOfExplain = ["same pattern", "no change", "no isolate"]
    Type = list(filter(lambda x: x in generalInfo, typeOfExplain))
    return Type
  def explain(self, generalInfo, iso): # general explanation
    #iso = self.isolate
    info = ''
    if iso in self.country:
      # that means when we spit the info based on iso, the iso name overlapped with the info so when spliting
      # the new info disappear and there for not in the original info
      # ex: IN, In: Indonesia
      generalInfo = iso + generalInfo.split(iso)[-1]
      info = generalInfo.split(";")[0]
    else:
      '''if iso not in generalInfo:
        iso = getNewIsolate(iso)'''
      if iso not in generalInfo or iso == "":
        # after getting new iso it still not found, then it doesnt exist
        info = iso
      else:
        if len(re.findall(r'\b%s\b' % iso,generalInfo)) > 0:
          info = ': '.join(list(filter(lambda x: ":" in x, re.split(r'\b%s\b' % iso,generalInfo)[1:]))[0].split(";")[0].split(": ")[1:])
        else:
          info  = ": ".join(list(filter(lambda x: ":" in x, generalInfo.split(iso)[1:]))[0].split(";")[0].split(": ")[1:])
          if len(info) == 0:
            info = getNewIsolate.getNewIsolate(self.isolate)
    option = list(filter(lambda x: x in info, self.optionals))
    if len(option) > 0:
      explain = "(".join(info.split(option[0])[0].split("(")[:-1])
    else:
      explain = info
    return explain, option, info
  # for special case of explanation
  def samePattern(self, generalInfo, originalIsolate):
    if "re.split('\d+',word)[0]" in generalInfo:
      explain = re.split('\d+',originalIsolate)[0]
    elif "' '.join(word.split('_')[1:-1])" in generalInfo:
      explain = ' '.join(originalIsolate.split('_')[1:-1])
    elif '''re.findall("[A-Z]*[a-z]*|d+",word)[0]''' in generalInfo:
      explain = re.findall("[A-Z]*[a-z]*|d+",originalIsolate)[0]
    elif "word.split('_')[-1]" in generalInfo:
      explain = originalIsolate.split('_')[-1]
    elif "word.split('-')[0]" in generalInfo:
      explain = originalIsolate.split('-')[0]
    option = list(filter(lambda x: x in generalInfo, self.optionals))
    return explain, option, generalInfo
  def noChange(self, generalInfo, originalIsolate):
    explain = originalIsolate
    option = list(filter(lambda x: x in generalInfo, self.optionals))
    return explain, option, generalInfo
  def noIsolate(self, generalInfo):
    explain = generalInfo.split(self.accnum)[1].split(": ")[1].split(",")[0].split(")")[0]
    option = list(filter(lambda x: x in generalInfo, self.optionals))
    return explain, option, generalInfo
  # fucntions for optionals
  def getLocation(self, option, explain, info):
    if "location" in option:
      if ":" in info.split("location")[1]:
        loc = info.split("location")[1].split(": ")[1].split(",")[0].split(")")[0]
      else:
        loc = explain
    return loc
  def getEthnic(self, option, explain, info):
    if "ethnic" in option:
      if ":" in info.split("ethnic")[1]:
        eth = info.split("ethnic")[1].split(": ")[1].split(",")[0].split(")")[0]
      else: eth = explain
    return eth
  def getLanguage(self, option, explain, info):
    if "language" in option:
      if ":" in info.split("language")[1]:
        lan = info.split("language")[1].split(": ")[1].split(",")[0].split(")")[0]
      else: lan = explain
    return lan
  def getPopulation(self, option, explain, info):
    if "population" in option:
      if ":" in info.split("population")[1]:
        popu = info.split("population")[1].split(": ")[1].split(",")[0].split(")")[0]
      else: popu = explain
    return popu