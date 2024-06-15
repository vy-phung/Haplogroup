from Haplogroup.finalCodes.DataWrangling import openFile, saveFile
import copy
def uniqAccCountry(listAcc,InfoFile, dupAcc):
  uniqAcc = copy.deepcopy(listAcc)
  info = openFile.openFile(InfoFile)
  for acc in dupAcc:
    country = info.split(acc)[1].split("/country=")[1].split("\n")[0].split('"')[1]
    uniqAcc[acc] = [country]
  return uniqAcc