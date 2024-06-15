from Haplogroup.finalCodes.DataWrangling import openFile, saveFile
class SummaryDataset3:
  def __init__(self, accnum):
    readFile = openFile.openFile("/content/drive/MyDrive/Haplogroup/finalCodes/others/Dataset3_accnumInfo.txt")
    accnumList = openFile.openFile("/content/drive/MyDrive/Haplogroup/finalCodes/others/UniqueAccNumForDataset3.txt").split(",")
    if accnum in accnumList[-1]:
      accPos = len(accnumList)-1
      self.summary = readFile.split(accnum)[1]
    else:
      accPos = accnumList.index(accnum)
      nextAcc = accnumList[accPos+1]
      self.summary = readFile.split(accnum)[1].split(nextAcc)[0]
    self.accnum = accnum
  def getIsolate(self):
    # getting the isolate
    isolate=""
    if 'isolate' in self.summary:
      if '/isolate=' in self.summary:
        isolate = self.summary.split('/isolate=')[1].split('"')[1]
      else:
        isolate = self.summary.split('isolate')[1].split()[0]
      if ":" in isolate:  isolate.split(":")[-1]
      if  "." in isolate: isolate = isolate.replace('.','_')
      if " " in isolate:  isolate = isolate.replace(' ','_')
      if '\n' in isolate: isolate = isolate.replace('\n','')
    return isolate
  def getAuthors(self,year):
    authors = self.summary.split('AUTHORS')[1].split('\n')[0].split()
    if len(authors) > 0:
      refName = authors[0].split(',')[0] + ' et al. ' + '(' + year +')'
    else: refName = authors[0].split(',')[0] + ' (' + year + ')'
    return refName
  def getYears(self):
    File = openFile.openFile("/content/drive/MyDrive/Haplogroup/finalCodes/others/YEAR_Data3.txt")
    typeYear = File.split(self.accnumaccnum)[0].split("\n")[-1]
    if "LOCUS" in typeYear:
      year =  File.split(self.accnum)[1].split("\n")[0].split("\t")[-1].split("-")[-1]
    elif "PUBDATE" in typeYear:
      year = File.split(self.accnum)[1].split("\n")[0].split("\t")[-1].split("-")[0]  
    return year
  def getTitle(self):
    title = ' '.join(self.summary.split('TITLE')[1].split('\n')[0].split())
    return title
  def getPubMedID(self):
    s = SummaryDataset3(self.accnum)
    title = s.getTitle()
    if 'PUBMED' in self.summary: # PubmedID.title.isolate.refName
      pubID = self.summary.split('PUBMED')[1].split()[0]
    else:
      if title != "Direct Submission":
        pubID = "Unpublished"
      else: pubID = ""  
    return pubID
  def getPoly(self):
    polyFile = openFile.openFile("/content/drive/MyDrive/Haplogroup/finalCodes/others/FixNameHaplo_acc_extendReport.txt")
    poly = polyFile.split(self.accnum)[1].split("\n")[0].split("\t")[-1].split('"')[1]
    return poly
