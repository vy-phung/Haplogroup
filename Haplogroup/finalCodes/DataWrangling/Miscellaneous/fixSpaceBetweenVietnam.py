from Haplogroup.finalCodes.DataWrangling import openFile, saveFile
def fixSpaceBetweenVietnam():
  bigFile = openFile.openFile("/content/drive/MyDrive/RetrieveData/Dataset3/Viet Nam/Viet Nam_NewBigFile.fasta")
  for line in openFile.openFile("/content/drive/MyDrive/Haplogroup/finalCodes/others/FixVietnam.txt").split("\n")[:-1]:
    newLine = line.replace("Viet Nam","Vietnam")
    newName = newLine.split("/")[-1].split(".fasta")[0]
    oldName = line.split("/")[-1].split(".fasta")[0]
    oldFile = openFile.openFile(line)
    if "NewBigFile" not in line:
      newFile = oldFile.replace(oldName,newName)
      bigFile = bigFile.replace(oldName,newName)
      saveFile.saveFile("/content/drive/MyDrive/RetrieveData/Dataset3/Vietnam/" + newName + ".fasta",newFile)  
  saveFile.saveFile("/content/drive/MyDrive/RetrieveData/Dataset3/Vietnam/Vietnam_NewBigFile.fasta",bigFile)    
  print("done")