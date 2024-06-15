import pandas as pd
# match the additional infomation from Changed_SEA_Haplogroup to the column at Isotab
def MatchSEAInfoToIso():
  IsoTab = pd.read_excel("/content/drive/MyDrive/RetrieveData/tables/IsolateExplanation.xlsx", index_col="ID")
  #IsoTab = IsoT.iloc[:10]
  SEA = pd.read_excel("/content/drive/MyDrive/RetrieveData/tables/Changed_SEA_haplogroups.xlsx")
  exSEALists = list(SEA.Explanation.unique())
  output = []
  for accnum in list(IsoTab.AccessionNumber.values):
    exIso = IsoTab.loc[IsoTab["AccessionNumber"]==accnum,["Explanation"]].values[0][0]
    country = IsoTab.loc[IsoTab["AccessionNumber"]==accnum,["Country"]].values[0][0]
    IsoLine = IsoTab.loc[IsoTab["AccessionNumber"]==accnum,:]
    # get exIso
    # there might be some explanations needed to be transformed to right format to be recognized in the SEA table, so we have to transform it
    #print(accnum, exIso)
    if exIso not in exSEALists:
      exIso = transformEx(exIso, exSEALists)
    if exIso != "explain not in SEAList":
      exSEATab = SEA.loc[SEA["Explanation"]==exIso,["Country","Ethnicity","Location","Language","Language family"]]
      exSEA = exSEATab.loc[exSEATab["Country"]==country,:]
      print(accnum, exIso)
      # fill the nan cell
      # create a Language family column on the right side of column "Population" manually
      for col in ["Ethnicity","Location","Language","Language family"]:
        if str(IsoLine[col].values[0]) == "nan":
          replacedVal = str(exSEA.loc[:,[col]].values[0][0])
          IsoLine[col].fillna(replacedVal, inplace = True)
    #print(IsoLine)
    output.append(IsoLine)
  df = pd.concat(output)
  return df
def transformEx(explanation, SEAList):
  '''['individual_A' : individual A,
 'individual_B' : individual B,
 'Borneo, Kota Kinabalu ': Kota Kinabalu (Borneo),
 'Mlabri',
 'Maniq',
 'Lue',
 'Yuan',
 'Viet Nam' : 'Vietnam,
 'VN' : Vietnam,
 'Tay-Nung' : 'Tay Nung]
 "Kravet": "Kravet (subgroup of Brao)"
 '''
  # specific case
  oldEx = ""
  alreadytransformed = "No"
  if alreadytransformed == "No":
    if explanation == "individual_A" or explanation == "individual_B": oldEx = explanation.replace("_"," ")
    elif explanation == "Borneo, Kota Kinabalu ": oldEx = "Kota Kinabalu (Borneo)"
    elif explanation in ["Viet Nam", "VN"]: oldEx = "Vietnam"
    elif explanation == "Tay-Nung": oldEx = "Tay Nung"
    # normal case: such as the difference is the white space such as "Brunei " and "Brunei"
    else:
      oldEx = ' '.join(explanation.split(" ")[:-1])
    alreadytransformed = "Yes"
  # check if the final output exists in the SEA
  if alreadytransformed == "Yes":
    if oldEx in SEAList: return oldEx
    else: return "explain not in SEAList"