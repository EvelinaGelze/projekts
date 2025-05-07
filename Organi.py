import PySimpleGUI as org
 
# Izkārtojuma definīcija
saraksts=[['File',['Close']], ['Help'],['About']]

jautajumi = [
    {"jautajums": "Oculus", 
     "atbildes": ["acis", "sirds", "plaušas"],
     "pareiza_atbilde": "acis"},

    {"jautajums": "Hepaticophyta", 
     "atbildes": ["Nieres", "Sirds", "Aknas"], 
     "pareiza_atbilde": "Aknas"},

    {"jautajums": "Cutis",
     "atbildes": ["Āda", "Sirds", "Acis"], 
     "pareiza_atbilde": "Āda"},

    {"jautajums": "Cor", 
     "atbildes": ["Plaušas", "Sirds", "Aknas"], 
     "pareiza_atbilde": "Sirds"},

    {"jautajums": "Pulmo", 
     "atbildes": ["Plaušas", "Deguns", "Smadzenes"], 
     "pareiza_atbilde": "Plaušas"},

     {"jautajums": "Pancreas", 
     "atbildes": ["Aizkuņģa dziedzeris", "Kaulu smadzenes", "Smadzenes"], 
     "pareiza_atbilde": "Aizkuņģa dziedzeris"},

    {"jautajums": "Cerebrum", 
     "atbildes": ["Acis", "Kaulu smadzenes", "Smadzenes"], 
     "pareiza_atbilde": "Smdzenes"},

    {"jautajums": "larynx", 
     "atbildes": ["Mute", "Vēders", "Balsene"], 
     "pareiza_atbilde": "Balsene"}
]

index = 0

max_punkti = len(jautajumi)

organs = [
        [org.Menu(saraksts)],
        [org.Text("Ir dots latīniskais nosaukums orgānam un atbildi kā ir latviski!")],
        [org.Text(jautajumi[index]["jautajums"], key='-jaut-')],
        [org.T("                   "), org.Radio(jautajumi[index]["atbildes"][0], 'Radio1', default=False, key='-atb0-')],
        [org.T("                   "), org.Radio(jautajumi[index]["atbildes"][1], 'Radio1', default=False, key='-atb1-')],
        [org.T("                   "), org.Radio(jautajumi[index]["atbildes"][2], 'Radio1', default=False, key='-atb2-')],
        [org.Text(f"Tavi punkti: 0/{max_punkti}", key='-punkt-')],
        [org.Button("Nākamais jautājums!")],
        [org.Text("     ", key='-teksts-')]








    ]  


logs = org.Window("MINĒŠANAS SPĒLE - ORGĀNI", organs, size=(600,250))

punkti = 0

while True:
    event, values = logs.read()
 
    # Kā iziet, ja logs tiek aizvērts
    if event == org.WINDOW_CLOSED or event=='Close':
        break
    elif event=='About':
        org.popup('Autori: Emīls Ronis un Evelīna Ģelze')


    elif event=="Nākamais jautājums!":
        for i in range(3):
            if values[f"-atb{i}-"]:
                izvele = i
    
    if jautajumi[index]["atbildes"][izvele] == jautajumi[index]["pareiza_atbilde"]:
       logs['-teksts-'].update("Jautājums atbildēts pareizi!", background_color= "green")
       punkti +=1
       logs['-punkt-'].update(f"Tavi punkti:{punkti}/{max_punkti}")
    else:
        logs["-teksts-"].update("Jautājums atbildēts nepareizi!", background_color="red" )

    index += 1 
    if index < max_punkti:
        logs['-jaut-'].update(jautajumi[index]["jautajums"])
        for i in range(3):
            logs[f'-atb{i}-'].update(text=jautajumi[index]["atbildes"][i])
    else:
        logs.close()
        layout = [
            [org.Menu(saraksts)],
            [org.Text("Spēles beigas!", font=("Helvetica", 16), background_color="red")],
            [org.Text(f"Tu ieguvi {punkti} punktus no {max_punkti}! Yeyyyy ", background_color="pink")]
        ]
        logs = org.Window("MINĒŠANAS SPĒLE - ORGĀNI", layout, size=(350,150))
        

                                   



logs.close()
