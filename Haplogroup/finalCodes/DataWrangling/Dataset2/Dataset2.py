from Haplogroup.finalCodes.DataWrangling import openFile, saveFile
def Dataset2():
  UniqListDataset1 = openFile.openFile("/content/drive/MyDrive/Haplogroup/finalCodes/others/UniqueAccNumForDataset1.txt").split(",")
  Dataset1 = openFile.openFile("/content/drive/MyDrive/Haplogroup/finalCodes/others/Dataset1_accnumInfo.txt")
  Dataset2 = ""
  RemovedData = {}
  UniqListDataset2 = []
  for pos in range(len(UniqListDataset1)):
    accnum = UniqListDataset1[pos]
    if pos == len(UniqListDataset1)-1:
      info = Dataset1.split(accnum)[1]
    else:
      nextAccnum = UniqListDataset1[pos+1]
      info = Dataset1.split(accnum)[1].split(nextAccnum)[0]
    # 3 cases: nonHomosapiens, refSeq, D-loop
    orga = info.split("ORGANISM")[1].split("\n")[0]
    if "Homo sapiens" in orga:
      # Homosapien but can be refSeq or D-loop
      if "_" not in accnum: # HomoSapien and not RefSeq
        if "D-loop" not in info:
          if "D-Loop" not in info: # HomoSapien and not RefSeq and not D-loop
            Dataset2 += accnum + "\n" + info
            UniqListDataset2.append(accnum)
        else:
          RemovedData["HomoNotRefButDLoop"] = accnum
      else:
        RemovedData["HomoButRefSeq"] = accnum
    else: # it is nonHomoSapien
      RemovedData["nonHomoSapiens"] = accnum
  saveFile.saveFile("/content/drive/MyDrive/Haplogroup/finalCodes/others/Dataset2_accnumInfo.txt",Dataset2)
  saveFile.saveFile("/content/drive/MyDrive/Haplogroup/finalCodes/others/UniqueAccNumForDataset2.txt", ",".join(UniqListDataset2))
  return UniqListDataset2, RemovedData