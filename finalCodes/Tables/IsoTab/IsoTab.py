import pandas as pd
def IsoTab(table, country):
  table = pd.read_excel('/content/drive/MyDrive/OUCRUwork/RetrieveData/tables/IsolateExplanation.xlsx')
  SEA = pd.read_excel('/content/drive/MyDrive/OUCRUwork/RetrieveData/tables/table1/Changed_SEA_haplogroups.xlsx')
  data = SEA.loc[SEA['Country']==country,['Country','Explanation',	'Ethnicity',	'Language',	'Language family', 'Location']]
  tabCountry = table.loc[table['Country']==country,['Explanation']]
  output = {'Country':[],'Explanation':[], 'Location':[]}
  for explain in list(tabCountry['Explanation'].values):
    output['Explanation'].append(explain)
    #print(explain)
    if explain not in list(data['Explanation'].values):
      for val in list(data['Explanation'].values):
        if country == 'Vietnam':
          if val == 'Viet Nam':
            explain = val
          elif val == 'VN':
            explain = val
          elif val == 'Tay Nung':
            explain = val
        if ',' in explain:
          explain = explain.split(',')[0]
        if ' ' in explain:
          explain = explain.split(' ')[0]
        if '-' in explain:
          explain = explain.split('-')[0]
        if explain in val:
          explain = val
          break
    output['Location'].append(list(data.loc[data['Explanation']==explain,'Location'].values)[0])
    output['Country'].append(list(data.loc[data['Explanation']==explain,'Country'].values)[0])
  output = pd.DataFrame(output)
  return output