import pandas as pd
def table3(country):
  data = pd.read_csv('/content/drive/MyDrive/OUCRUwork/RetrieveData/tables/table3/'+country+'3.csv')
  data = data.replace('-',0)
  df = {'Haplogroup': [], 'Total':[]}
  bigTotal = data['Sample size'].sum()
  for col in data.columns[3:]:
    df['Haplogroup'].append(col)
    if data[col].dtypes != int:
      data[col] = data[col].astype(float)
      data[col] = data[col].astype(int)
    # frequency of each label group
    for name in list(set(data['Label'].values)):
      count = list(data.loc[data['Label']==name,col].values)
      total = list(data.loc[data['Label']==name,'Sample size'].values)
      freq = (sum(count)/sum(total)) * 100
      if name not in df:
        df[name] = [round(freq,2)]
      else: df[name].append(round(freq,2))
    # frequency of total sample size in that country dataset
    df['Total'].append(round((data[col].sum()/bigTotal)*100,3))
  output = pd.DataFrame(df)
  return output