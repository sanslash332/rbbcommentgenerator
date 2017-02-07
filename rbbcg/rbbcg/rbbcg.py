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

f = codecs.open("frases.json", encoding= 'utf-8',mode= 'r')
data = js.loads(f.read())
f.close()

frase=""
frase = data['frases'][random.randint(0,len(data['frases'])-1)]

for x in range(1,6):
    if "%"+str(x) in frase:
        parte = data["arg"+str(x)][random.randint(0,len(data["arg"+str(x)])-1)]
        frase=frase.replace("%"+str(x),parte)


    


#print(frase)

pyperclip.copy(frase)
