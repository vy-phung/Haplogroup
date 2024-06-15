import re
class Haplo:
  def __init__(self, haplo):
    self.haplo = haplo
  def haplo1(self):
    # only first letter
    return re.findall("[A-Z]",self.haplo)[0]
  def haplo2(self):
    # first letter with first numerical value (13 counts as firt nuemerical value)
    return re.findall("[A-Z]*\d*",self.haplo)[0]
  def haplo3(self):
    return re.findall("[A-Z]*\d*[a-z]*",self.haplo)[0]