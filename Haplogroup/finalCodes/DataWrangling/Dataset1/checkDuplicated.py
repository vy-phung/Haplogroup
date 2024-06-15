from Haplogroup.finalCodes.DataWrangling import openFile, saveFile
def checkDuplicated():
 allSeqFile = openFile.openFile("/content/drive/MyDrive/Haplogroup/finalCodes/others/allSeq.txt")
 uniqueList = []
 duplicatedList = []
 for string in allSeqFile.split(">"):
  if len(string) > 0:
    accnum = string.split('.')[0]
    if accnum not in uniqueList:
      uniqueList.append(accnum)
    else:
      duplicatedList.append(accnum)
 return uniqueList, duplicatedList