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

url = "https://dl.dropboxusercontent.com/u/13634494/No%20borrar/frases.json"

try:
    f = codecs.getreader("utf-8")(urllib.request.urlopen(url))


    
except Exception:
    f = codecs.open("frases.json", encoding= 'utf-8',mode= 'r') 



data = js.loads(f.read())
f.close()

frase=""
frase = data['frases'][random.randint(0,len(data['frases'])-1)]

for x in range(1,6):
    while "%"+str(x) in frase:
        parte = data["arg"+str(x)][random.randint(0,len(data["arg"+str(x)])-1)]
        frase=frase.replace("%"+str(x),parte,1)


    



#print(frase)

if len(sys.argv) > 1:
    if sys.argv[1] == "poder":
        frase= frase.upper()
        frase = "¡¡¡¡¡¡" + frase[:-1] + "!!!!"



pyperclip.copy(frase)
