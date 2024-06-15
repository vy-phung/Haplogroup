from Haplogroup.finalCodes.DataWrangling import openFile, saveFile
def assignCountry():
  dataset3 = openFile.openFile("/content/drive/MyDrive/Haplogroup/finalCodes/others/UniqueAccNumForDataset3_4932.txt").split(",")
  list_acc_country = {}
  dup_acc_country = []
  for accnum in dataset3:
    accnum = accnum.split("\n")[0]
    for country in openFile.openFile("/content/drive/MyDrive/Haplogroup/finalCodes/others/countries.txt").split(","):
      if accnum in openFile.openFile("/content/drive/MyDrive/RetrieveData/OldCountryFasta/"+country+".fasta"):
        if accnum not in list_acc_country:
          list_acc_country[accnum] = [country]
        else:
          list_acc_country[accnum].append(country)
          dup_acc_country.append(accnum)
  return list_acc_country, list(set(dup_acc_country))