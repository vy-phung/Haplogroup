import pandas as pd
# create table2: haplo, numOfIn, Fre(num/total)
def table2(fileCSV):
  df = pd.read_csv(fileCSV)
  haplos, counts, freq = [],[],[]
  total, fre = 4932, 0
  for haplo in df.columns[2:]:
    haplos.append(haplo)
    haplogroup = df.loc[:,haplo]
    counts.append(haplogroup.sum())
    fre = (haplogroup.sum()/total)*100
    freq.append(round(fre,3))
  # create table2
  data = {'Haplogroup': haplos,
          'Number of Individuals': counts,
          'Frequency (%)': freq }
  table = pd.DataFrame(data)
  return table