import pandas as pd
def createTable3ad(country, groups, file, classify):
  table = pd.read_csv(file, index_col="Unnamed: 0")
  groupData = table.loc[:,groups]
  autoData = table.loc[:,'Sample size':]
  data = pd.concat([groupData,autoData],axis=1)
  data = data.loc[data['Country']==country,:]
  data = data.replace('-',0)
  df = {'Haplogroup':[], 'Total':[]}
  bigTotal = data['Sample size'].sum()
  for col in data.columns[3:]:
    df['Haplogroup'].append(col)
    if data[col].dtypes != int:
      data[col] = data[col].astype(float)
      data[col] = data[col].astype(int)
    # frequency of each label group
    for name in list(set(data[classify].values)):
      count = list(data.loc[data[classify]==name,col].values)
      total = list(data.loc[data[classify]==name,'Sample size'].values)
      freq = (sum(count)/sum(total)) * 100
      if name not in df:
        df[name] = [round(freq,2)]
      else: df[name].append(round(freq,2))
    # frequency of total sample size in that country dataset
    df['Total'].append(round((data[col].sum()/bigTotal)*100,3))
  output = pd.DataFrame(df)
  header = {}
  title = []
  for i in range(len(output.columns)):
    if output.columns[i] == 'Haplogroup':
      index = 'Haplogroup'
    else: index = country+str(i)
    header[index] = [output.columns[i]]
    title.append(index)
  head = pd.DataFrame(header)
  output.columns = title
  output = pd.concat([head, output], ignore_index=True, sort=False)
  return output