import pandas as pd
# table 1 only needs country, explanation, ethnicity, location, language, language family, sample size, original haplogroups
def createTable1(country, fullTable):
  table = fullTable.loc[fullTable["name"].str.contains(country),["ID","Author(s)","year","Explanation","Ethnicity","Location","Language","Language family","haplo"]]
  data = {'Country': [],
           'References':[],
           'Explanation': [],
           'Ethnicity': [],
           'Location':[],
           'Language':[],
           'Language family':[],
           'Sample size':[]}
  haplos = {}         
  for id in list(table["ID"].values):
    explain = table.loc[table["ID"]==id,["Explanation"]].values[0][0]
    haplo = table.loc[table["ID"]==id,["haplo"]].values[0][0]
    refers = []
    refer = table.loc[table["ID"]==id, ["Author(s)"]].values[0][0] + " (" + str(table.loc[table["ID"]==id, ["year"]].values[0][0]) + ")"
    if explain not in data["Explanation"]:
      data["Country"].append(country)
      data["Explanation"].append(explain)
      data["Sample size"].append(1)
      data["References"].append(refer)
      ethnic = table.loc[table["Explanation"]==explain,["Ethnicity"]].values[0][0]
      locate = table.loc[table["Explanation"]==explain,["Location"]].values[0][0]
      lang = table.loc[table["Explanation"]==explain,["Language"]].values[0][0]
      langFam = table.loc[table["Explanation"]==explain,["Language family"]].values[0][0]
      data["Ethnicity"].append(ethnic)
      data["Location"].append(locate)
      data["Language"].append(lang)
      data["Language family"].append(langFam)
      if haplo not in haplos:
        haplos[haplo] = {}
      haplos[haplo][data["Explanation"].index(explain)] = 1

    else:
      data["Sample size"][data["Explanation"].index(explain)] += 1
      if refer not in data["References"][data["Explanation"].index(explain)]:
        data["References"][data["Explanation"].index(explain)] += ", " + refer
      # for haplogroup
      if haplo in haplos: # same haplo name but different explanation
        if data["Explanation"].index(explain) not in haplos[haplo]:
          haplos[haplo][data["Explanation"].index(explain)] = 1
        else:
          haplos[haplo][data["Explanation"].index(explain)] += 1
      else:
        haplos[haplo] = {}
        haplos[haplo][data["Explanation"].index(explain)] = 1
  # create output table
  df = pd.DataFrame(data)
  # create Haplo table
  for haplo in haplos:
    col = ["-"] * len(data["Explanation"])
    for pos in haplos[haplo]:
      col[pos] = haplos[haplo][pos]
    haplos[haplo] = col
  haplogroup = pd.DataFrame(haplos)
  # merge table
  total = pd.concat([df,haplogroup], axis = 1)
  return total