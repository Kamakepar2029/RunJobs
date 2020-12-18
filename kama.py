import json

class Kama():
  def __init__(self,folder):
    self.folder = folder

  def render_k(self,template,ks,stri):
    pill = open(self.folder+'/'+template,'r').read()
    args = json.loads(ks)
    stro = ''
    for key in args:
      pill = pill.replace('%'+key+'%',args[key])
    return pill.replace('%stri%',stri)
