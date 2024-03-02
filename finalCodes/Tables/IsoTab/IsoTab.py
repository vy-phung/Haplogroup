import pandas as pd
def IsoTab(table, country):
  SEA = pd.read_excel('/content/drive/MyDrive/OUCRUwork/RetrieveData/tables/table1/Changed_SEA_haplogroups.xlsx', index_col='Unnamed: 0')
  data = SEA.loc[SEA['Country']==country,['Country','Explanation',	'Ethnicity',	'Language',	'Language family', 'Location']]
  tabCountry = table.loc[table['Country']==country,['Explanation']]
  output = {'Explanation':[], 'Location':[]}
  for explain in list(tabCountry['Explanation'].values):
    output['Explanation'].append(explain)
    if explain not in list(data['Explanation'].values):
      for val in list(data['Explanation'].values):
        if explain in val:
          explain = val
          break
        elif country == 'Vietnam':
          if val == 'Viet Nam':
            explain = val
          elif val == 'VN':
            explain = val
          elif val == 'Tay Nung':
            explain = val
    output['Location'].append(list(data.loc[data['Explanation']==explain,'Location'].values)[0])
  output = output.set_index(['Explanation'])
  # check again this code below
  #output = pd.concat([,output],axis=1)
  return output