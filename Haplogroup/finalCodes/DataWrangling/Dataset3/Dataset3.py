from Haplogroup.finalCodes.DataWrangling import openFile, saveFile
def Dataset3():
  UniqListDataset2 = openFile.openFile("/content/drive/MyDrive/Haplogroup/finalCodes/others/UniqueAccNumForDataset2.txt").split(",")
  Dataset2 = openFile.openFile("/content/drive/MyDrive/Haplogroup/finalCodes/others/Dataset2_accnumInfo.txt")
  Dataset3 = ""
  RemovedData = {}
  UniqListDataset3 = []
  for pos in range(len(UniqListDataset2)):
    accnum = UniqListDataset2[pos]
    if pos == len(UniqListDataset2)-1:
      info = Dataset2.split(accnum)[1]
    else:
      nextAccnum = UniqListDataset2[pos+1]
      info = Dataset2.split(accnum)[1].split(nextAccnum)[0]
    if "control" not in info: # which means the others are not control or complete genome
      Dataset3 += accnum + "\n" + info
      UniqListDataset3.append(accnum)
    else:
        RemovedData["control region"] = accnum
  saveFile.saveFile("/content/drive/MyDrive/Haplogroup/finalCodes/others/Dataset3_accnumInfo.txt",Dataset3)
  saveFile.saveFile("/content/drive/MyDrive/Haplogroup/finalCodes/others/UniqueAccNumForDataset3.txt", ",".join(UniqListDataset3))
  return UniqListDataset3, RemovedData