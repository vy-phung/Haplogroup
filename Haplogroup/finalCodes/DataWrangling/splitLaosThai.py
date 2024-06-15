# for the special case, i have to split up Lao and Thai into their original file and add only non-existed sequences
from Haplogroup.finalCodes.DataWrangling import openFile, saveFile
def splitLaosThai(fileName):
  LaosFile = openFile.openFile("/content/drive/MyDrive/RetrieveData/OldCountryFasta/Laos.fasta")
  ThaiFile = openFile.openFile("/content/drive/MyDrive/RetrieveData/OldCountryFasta/Thailand.fasta")
  t = 0
  for string in openFile.openFile(fileName).split(">"):
    if len(string) > 0:
      name = string.split("\n")[0]
      accnum = name.split(".")[0]
      if "LUA" in name or "VIE" in name:
        if accnum not in LaosFile:
          LaosFile += ">" + string
      else:
        if accnum not in ThaiFile:
          ThaiFile += ">" + string
  saveFile.saveFile("/content/drive/MyDrive/RetrieveData/OldCountryFasta/Laos.fasta",LaosFile)
  saveFile.saveFile("/content/drive/MyDrive/RetrieveData/OldCountryFasta/Thailand.fasta",ThaiFile)