import re 
# BD: Bidayuh (ethnic); JH: Jehai (ethnic); SL: Seletar (ethnic); TM: Temuan (ethnic) BDF
def ham_dis(trans,iso):
  length, output = 0, ''
  newTrans, newIso = '', ''
  for l in trans.split(';'): # clean trans into newTrans
    newTrans += l.split(":")[0] + ','
  # clean iso into new Iso
  isoList = re.split('\d+',iso)
  for isolate in isoList:
    if len(isolate) > 0:
      newIso = isolate
      break
  for line in newTrans.split(', '):
    if len(line)>0:
      same, count= '', 0
      for i, j in zip(line.split(":")[0].split()[0], newIso):
        if i == j:
          same += i
          count += 1
        else: break
      if count > length:
        length = count
        output = same
  return output