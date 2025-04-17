import PySimpleGUI as org
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

     {"jautajums": "Kurš orgāns palīdz regulēt cukura līmeni asinīs?", 
     "atbildes": ["Aizkuņģa dziedzeris", "Kaulu smadzenes", "Smadzenes"], 
     "pareizā_atbilde": "Aizkuņģa dziedzeris"},

    {"jautajums": "Kurš orgāns atrodas galvaskausā un vada ķermeņa funkcijas?", 
     "atbildes": ["Acis", "Kaulu smadzenes", "Smadzenes"], 
     "pareizā_atbilde": "Smdzenes"},

    {"jautajums": "Kur atrodas balss saites?", 
     "atbildes": ["Mutē", "Vēderā", "Balsenē"], 
     "pareizā_atbilde": "Balsenē"}
]

index = 0

max_punkti = len(jautajumi)

organs = [
        [org.Menu(saraksts)],
        [org.Text(jautajumi[index]["jautajums"], key='-jaut-')],
        [org.T("                   "), org.Radio(jautajumi[index]["atbildes"][0], 'Radio1', default=False, key='-atb0-')],
        [org.T("                   "), org.Radio(jautajumi[index]["atbildes"][1], 'Radio1', default=False, key='-atb1-')],
        [org.T("                   "), org.Radio(jautajumi[index]["atbildes"][2], 'Radio1', default=False, key='-atb2-')],
        [org.Text(f"Tavi punkti: 0/{max_punkti}", key='-punkt-')]
        [org.Button("Pareizi/Nepareizi!"), org.Button("Nākamais jautājums!")],
        [org.Text("     ", key='-teksts-')]








    ]  


logs = org.Window("MINĒŠANAS SPĒLE - ORGĀNI", organs, size=(900,650))


while True:
    event, values = logs.read()
 
    # Kā IZET, ja logs tiek aizvērts
    if event == org.WINDOW_CLOSED or event=='Close':
        break
    elif event=='About':
        org.popup('Autori: Emīls Ronis un Evelīna Ģelze')

    elif event=="Pareizi/Nepareizi!":
        for i in range(3):
            if values[f"-atb{i}-"]:
             izvele = i




logs.close()
