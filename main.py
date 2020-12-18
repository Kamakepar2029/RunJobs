from flask import Flask, render_template
import os
from multiprocessing import Process
from kama import Kama
app = Flask(__name__, template_folder="templates")

def shablon(directory):
  directory_mass = directory.split('/')
  directory = directory_mass[len(directory_mass)-1]
  string = '<div class="panel profit db mbm"><div class="panel-body"><p class="icon"><i class="icon fa fa-shopping-cart"></i></p><h4 class="value"><span data-counter="" data-start="10" data-end="50" data-step="1" data-duration="0">'+directory+'</span><span> Job</span></h4></div></div>'
  return string

class CustomProcess(Process):
   def __init__(self, limit):
       Process.__init__(self)
       self._limit = limit
   def run(self):
       os.system('./ngrok http 2056')           

class StartJob(Process):
   def __init__(self, limit):
       Process.__init__(self)
       self._limit = limit
   def run(self):
       os.system('python3 startjob.py')

k = Kama('templates')

@app.route('/')
def index():
  count_projects = open('count.txt','r').read()
  lastres = open('lastres.txt','r').read()
  projects = (os.listdir('found/'))
  start = 0
  end = len(projects)
  string = ''
  while start<end:
    string = string+shablon(projects[start]).replace('"',"'")
    start+=1
  jso = '{"runprojects":"'+count_projects+'","lastres":"'+lastres+'","allpr":"'+string+'"}'
  return (k.render_k('index.php',jso))

@app.route('/newjob')
def newj():
  cp = StartJob(3)
  cp.start()
  return ('Job Started')


if __name__ == "__main__":
  cpr = CustomProcess(3)
  cpr.start()
  app.run(host="0.0.0.0",port=2056)