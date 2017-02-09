#!/usr/bin/python
# -*- coding: latin-1 -*-
import sys
import os

if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)


 

import pyperclip
import simplejson as js
import random
import codecs
import urllib.request
import re

url = "https://dl.dropboxusercontent.com/u/13634494/No%20borrar/frases.json"

try:
    f = codecs.getreader("utf-8")(urllib.request.urlopen(url))


    
except Exception:
    f = codecs.open("frases.json", encoding= 'utf-8',mode= 'r') 



data = js.loads(f.read())
f.close()
p = re.compile('%([a-zA-Z0-9\ ]+)%')

frase=""
frase = data['frases'][random.randint(0,len(data['frases'])-1)]

for x in p.finditer(frase):
    for keyword in x.groups():

    
        parte = data[keyword][random.randint(0,len(data[keyword])-1)]
        frase=frase.replace("%"+keyword+"%",parte,1)


    



#print(frase)

if len(sys.argv) > 1:
    if sys.argv[1] == "poder":
        frase= frase.upper()
        frase = "¡¡¡¡¡¡" + frase[:-1] + "!!!!"



pyperclip.copy(frase)
