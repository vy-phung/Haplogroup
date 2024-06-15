from Haplogroup.finalCodes.DataWrangling.Dataset3 import summaryForDataset3
from Haplogroup.finalCodes.DataWrangling import openFile, saveFile
class YearFor4932:
  def __init__(self):
    accnumList = openFile.openFile("/content/drive/MyDrive/Haplogroup/finalCodes/others/UniqueAccNumForDataset3_4932.txt").split(",")
    accnumList[-1] = accnumList[-1].split("\n")[0]
    self.accnumList = accnumList
  def createYearInfo4932(self):
    pubID, noID, pubList = {},[], []
    for acc in self.accnumList:
      s = summaryForDataset3.SummaryDataset3(acc)
      pub = s.getPubMedID()
      if pub == "Unpublished" or len(pub) == 0: # will run LOCUS for this
        noID.append(acc)
      else: # will run pubDate for this
        pubID[acc] = pub
        pubList.append(pub)
    saveFile.saveFile("/content/drive/MyDrive/Haplogroup/finalCodes/others/PubIDForPubDate.txt",','.join(list(set(pubList))))
    saveFile.saveFile("/content/drive/MyDrive/Haplogroup/finalCodes/others/AccNumForLOCUS.txt",','.join(noID))
    return pubID, noID
  def createYearFile(self,pubID):
    output = openFile.openFile("/content/drive/MyDrive/Haplogroup/finalCodes/others/LOCUS_Data3.txt")
    pubDate = openFile.openFile("/content/drive/MyDrive/Haplogroup/finalCodes/others/Pubdate_Data3.txt")
    for acc in pubID:
      id = pubID[acc]
      line = pubDate.split(id)[1].split("<PubDate>")[1].split("</PubDate>")[0]
      output += '\n'+ "PUBDATE" + '\t' + acc + '\t' + line.replace(" ","-")
    saveFile.saveFile("/content/drive/MyDrive/Haplogroup/finalCodes/others/YEAR_Data3.txt",output)
    print("done")