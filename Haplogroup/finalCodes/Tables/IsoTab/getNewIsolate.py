import re
def getNewIsolate(oldIsolate):
    # Ex: Bes2; In276/IN101; PRY35; Smd2; WAI30; KK141; 10HMS110; 2HMSN; A1YU102;
    # PP101; Thai107; YN1_337; V206; VN014; VNM235
    # FTDNA_233764 but in translation file, it is written FTDNA 233764
    '''Only take 2 first letters
    HM: Hmong (ethnic); Y: IuMien (ethnic); MR, MB: Lahu (ethnic); LS: Lisu (ethnic);
    KSK3, KR: Karen (ethnic); SH2: Shan (ethnic); PT, PUT:
    My isolate read: HMS/HMSN/HMP'''
    '''SAk is SAK'''
    iso = ''
    if "FTDNA" in oldIsolate:
      iso = oldIsolate.replace("_"," ")
    elif "SAk" in oldIsolate:
      iso = "SAK"
    else:
      if len(re.findall('[A-Z|a-z]+',oldIsolate)) == 1:
        iso = re.findall('[A-Z|a-z]+',oldIsolate)[0]
      elif len(re.findall('[A-Z|a-z]+',oldIsolate))>1:
        iso = re.findall('[A-Z|a-z]+\d*[A-Z|a-z]+',oldIsolate)[0]
    return iso