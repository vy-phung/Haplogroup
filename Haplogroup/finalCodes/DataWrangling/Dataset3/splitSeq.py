from Haplogroup.finalCodes.DataWrangling import openFile, saveFile
from Haplogroup.finalCodes.DataWrangling.Datatset3 import SummaryDataset3
class splitSeq:
  def __init__(self):
    pass
  def splitFastaSeq(self,UniqAccCountryList):
    for acc in UniqAccCountryList: #UniqAccCountryList is a dictionary
      country = UniqAccCountryList[acc][0]
      bigFile = openFile.openFile("/content/drive/MyDrive/RetrieveData/OldCountryFasta/"+country+".fasta")
      seq = ">" + acc + bigFile.split(acc)[1].split(">")[0]
      saveFile.saveFile("/content/drive/MyDrive/RetrieveData/Dataset3/"+country+"/"+acc+".fasta",seq)
    print("done")
  def getHaplo(self, accnum):
    haploFile = openFile.openFile("/content/drive/MyDrive/Haplogroup/finalCodes/others/Haplo_acc.txt")
    haplo = haploFile.split(accnum)[1].split("SampleId")[0].split('\t')[1].split('"')[1]
    return haplo
  def createNewName(self,nameSeq):
    # input example: /content/drive/MyDrive/RetrieveData/Dataset3/Brunei/KU131308.fasta
    # label: country.isolate.accnum.haplo
    country = nameSeq.split("/")[6]
    accnum = nameSeq.split("/")[7].split(".")[0]
    haplo = self.getHaplo(accnum)
    isolate = SummaryDataset3.SummaryDataset3(accnum).getIsolate()
    newName = country + "." + isolate + "." + accnum + "." + haplo

    #add new file of new name into dataset 3
    content = ">"+newName + "\n" + '\n'.join(openFile.openFile(nameSeq).split("\n")[1:])
    saveFile.saveFile("/content/drive/MyDrive/RetrieveData/Dataset3/"+country+"/"+newName+".fasta",content)
    return newName
  def mergeSeqsBasedOnCountry(self,AllNewSeqList,country):
    output = ""
    # example of 1 seqName: /content/drive/MyDrive/RetrieveData/Dataset3/Brunei/Brunei.BRU18.KU131308.M7c1c3.fasta
    for seq in AllNewSeqList:
      name = seq.split("/")[-1]
      countrySeq = name.split(".")[0]
      if countrySeq == country:
        output += openFile.openFile(seq)
    saveFile.saveFile("/content/drive/MyDrive/RetrieveData/Dataset3/"+country+"/"+country+"_NewBigFile.fasta",output)
    print(country, "done")
    return output