def noIso(accnum,trans):
  output,ethnic = '',''
  if "no isolate" in trans:
    output = trans.split(accnum)[1].split(": ")[1]
    if ")" in output: # ")" mean the end
      if "ethnic" in output:
        output = output.split(' (ethnic)')[0]
        ethnic = "ethnic: " + output
      else: output = output.split(')')[0]
    elif ";" in output: # mean not the only one
      output = output.split(";")[0]
  return output,ethnic