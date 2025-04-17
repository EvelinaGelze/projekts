import PySimpleGUI as org
import random
from tkinter import messagebox
 
# Izkārtojuma definīcija
saraksts=[['File',['Close']], ['Help'],['About']]

jautajumi = [
    {"jautajums": "Redzes orgāns?", 
     "atbildes": ["acis", "sirds", "plaušas"],
     "pareizā_atbilde": "acis"},

    {"jautajums": "Bez šī orgāna tavs ķermenis nespētu attīrīt asinis un izvadīt toksīnus.", 
     "atbildes": ["Nieres", "Sirds", "Aknas"], 
     "pareizā_atbilde": "Aknas"},

    {"jautajums": "Kurš ir cilvēka lielākais orgāns?",
     "atbildes": ["Āda", "Sirds", "Acis"], 
     "pareizā_atbilde": "Āda"},

    {"jautajums": "Kurš orgāns sūknē asinis pa visu ķermeni?", 
     "atbildes": ["Plaušas", "Sirds", "Aknas"], 
     "pareizā_atbilde": "Sirds"},

    {"jautajums": "Kurš orgāns veic elpošanu?", 
     "atbildes": ["Plaušas", "Deguns", "Smadzenes"], 
     "pareizā_atbilde": "Plaušas"},
]

organs = [
        [org.Menu(saraksts)],
        [org.Text("Ar ko cilvēks redz?")],
        [org.T("                   "), org.Radio('Degunu', 'Radio1', default=False, key='-jaa-')],
        [org.T("                   "), org.Radio('Acīm', 'Radio1', default=False, key='-nee-')],
        [org.T("                   "), org.Radio('Rokām', 'Radio1', default=False, key='-nee-')],
        [org.Button("Pareizi/Nepareizi!")],








    ]  


logs = org.Window("MINĒŠANAS SPĒLE - ORGĀNI", organs, size=(900,650))


while True:
   event, values = logs.read()
 
    # Kā IZET, ja logs tiek aizvērts
   if event == org.WINDOW_CLOSED or event=='Close':
       break
   elif event=='About':
        org.popup('Autori: Emīls Ronis un Evelīna Ģelze')



logs.close()
