import pandas as pd
# create table2: haplo, numOfIn, Fre(num/total) from table1
def Table2(fileCSV1):
  df = pd.read_csv(fileCSV1, index_col="Unnamed: 0")
  haplos, counts, freq = [],[],[]
  total, fre = df['Sample size'].sum(), 0
  index = list(df.columns).index("Sample size")
  for haplo in df.columns[index+1:]:
    haplos.append(haplo)
    haplogroup = df.loc[:,haplo]
    haplogroup = haplogroup.replace("-",0)
    haplogroup = haplogroup.astype(float)
    counts.append(int(haplogroup.sum()))
    fre = (haplogroup.sum()/total)*100
    freq.append(round(fre,3))
  # create table2
  data = {'Haplogroup': haplos,
          'Number of Individuals': counts,
          'Frequency (%)': freq }
  table = pd.DataFrame(data)
  return table