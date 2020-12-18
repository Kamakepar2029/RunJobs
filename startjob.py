import json
from colorama import Fore
from all_search_api import yandex
from all_search_api import google
from all_search_api import bing
from datetime import datetime
import os
import requests as r

def mkdir(directory):
  os.system('mkdir '+directory)

def download_logs(logs,directory):
  try:
    text_m = logs.split('/')
    text = text_m[len(text_m)-1]
    if '?' in text:
      text_mass = text.split('?')
      text = text_mass[0]
    content = r.get(logs).text
    print(Fore.BLUE+text)
    if ('.' in text):
      text = text
    else:
      if text == '':
        text = text_m[len(text_m)-2]+'.html'
      else:
        text = text_m[len(text_m)-1]+'.html'
    mkdir(directory+'/'+text_m[2])
    f = open(directory+'/'+text_m[2]+'/'+text,'w')
    f.write(content)
    f.close()
    print(Fore.GREEN+'Log '+text+' downloaded and saved successfully.')
    pass
  except Exception as e:
    print(Fore.RED+'Exception: '+str(e))
    pass


def save_results(mass,filename):
  print(mass)
  f = open(filename,'w')
  f.write(str(mass).replace("'",'"'))
  f.close()

#keywords_search = 'allintext:password filetype:log after:2019'

#keywords_search = str(input('Enter google dork: '))

keywords_search = open('config_words.txt','r').read().replace('\n','')
lol = datetime.now()
print(lol.strftime("%Y-%m-%d-%H-%M-%S"))
nowtimedate = str(lol.strftime("%Y-%m-%d-%H-%M-%S"))
mass = ['10','20','30','40','50','60','70']
mapl = []
for star in mass:
  google_search = google(keywords_search+'&start='+star)
  mkdir('found/'+nowtimedate)
  mkdir('found/'+nowtimedate+'/search')
  mkdir('found/'+nowtimedate+'/logs')
  save_results(google_search,
  'found/'+nowtimedate+'/search/'+star+':start-google_search-'+nowtimedate+'.txt')
  mapl.append(google_search)
  start = 0
  end = len(google_search)-1
  while start<end:
    download_logs(google_search[start][0],'found/'+nowtimedate+'/logs')
    start+=1
save_results(mapl,lastres.txt)