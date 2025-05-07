import PySimpleGUI as org
from tkinter import messagebox
 
# Izkārtojuma definīcija
saraksts=[['File',['Close']], ['Help'],['About']]

jautajumi = [
    {"jautajums": "Oculus?", 
     "atbildes": ["acis", "sirds", "plaušas"],
     "pareizā_atbilde": "acis"},

    {"jautajums": "Hepaticophyta?", 
     "atbildes": ["Nieres", "Sirds", "Aknas"], 
     "pareizā_atbilde": "Aknas"},

    {"jautajums": "Cutis",
     "atbildes": ["Āda", "Sirds", "Acis"], 
     "pareizā_atbilde": "Āda"},

    {"jautajums": "Cor", 
     "atbildes": ["Plaušas", "Sirds", "Aknas"], 
     "pareizā_atbilde": "Sirds"},

    {"jautajums": "Pulmo", 
     "atbildes": ["Plaušas", "Deguns", "Smadzenes"], 
     "pareizā_atbilde": "Plaušas"},

     {"jautajums": "Pancreas", 
     "atbildes": ["Aizkuņģa dziedzeris", "Kaulu smadzenes", "Smadzenes"], 
     "pareizā_atbilde": "Aizkuņģa dziedzeris"},

    {"jautajums": "Cerebrum", 
     "atbildes": ["Acis", "Kaulu smadzenes", "Smadzenes"], 
     "pareizā_atbilde": "Smadzenes"},

    {"jautajums": "larynx?", 
     "atbildes": ["Mutē", "Vēderā", "Balsenē"], 
     "pareizā_atbilde": "Balsene"}
]

index = 0

max_punkti = len(jautajumi)

organs = [
        [org.Menu(saraksts)],
        [org.Text(jautajumi[index]["jautajums"], key='-jaut-')],
        [org.T("                   "), org.Radio(jautajumi[index]["atbildes"][0], 'Radio1', default=False, key='-atb0-')],
        [org.T("                   "), org.Radio(jautajumi[index]["atbildes"][1], 'Radio1', default=False, key='-atb1-')],
        [org.T("                   "), org.Radio(jautajumi[index]["atbildes"][2], 'Radio1', default=False, key='-atb2-')],
        [org.Text(f"Tavi punkti: 0/{max_punkti}", key='-punkt-')],
        [org.Button("Pareizi/Nepareizi!"), org.Button("Nākamais jautājums!")],
        [org.Text("     ", key='-teksts-')]








    ]  


logs = org.Window("MINĒŠANAS SPĒLE - ORGĀNI", organs, size=(900,650))

punkti = 0

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
    if jautajumi[index]["atbildes"][izvele] == jautajumi[index]["pareiza_atbilde"]:
        logs['-eee-'].update("Jautājums atbildēts pareizi!", background_color= "green")
        punkti +=1
        logs['-punkt-'].update(f"Tavi punkti:{punkti}/{max_punkti}")
    else:
        logs["-teksts-"].update("Jautājums atbildēts nepareizi!", background_color="red" )



logs.close()
