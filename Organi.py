import PySimpleGUI as org
 
# Izkārtojums
saraksts=[['File',['Close']], ['Help'],['About']]

# saraksti ar latīnisko nosaukumu un atbildēm un pareizo atbildi
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
# maksimālie punkti ir jautājumu daudzums
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


logs = org.Window("MINĒŠANAS SPĒLE - ORGĀNI", organs, size=(600,250), icon="ikona.ico")

punkti = 0

while True:
    event, values = logs.read()
 
    # Kā iziet, ja logs tiek aizvērts
    if event == org.WINDOW_CLOSED or event=='Close':
        break
    elif event=='About':
        org.popup('Autori: Emīls Ronis un Evelīna Ģelze')


    # ja tiek nospiesta poga "Nākamais jautājums!" tad
    elif event=="Nākamais jautājums!":
        for i in range(3):
            if values[f"-atb{i}-"]:
                izvele = i
    
    # ja tiek atbildēts pareizi tad parādās, ka atbildēts pareizi
    if jautajumi[index]["atbildes"][izvele] == jautajumi[index]["pareiza_atbilde"]:
       logs['-teksts-'].update("Jautājums atbildēts pareizi!", background_color= "green")
       # pieskaita punktu klāt par pareizu atbildi
       punkti +=1
       logs['-punkt-'].update(f"Tavi punkti:{punkti}/{max_punkti}")
       # ja atbildēts nepareizi parādās ziņa
    else:
        logs["-teksts-"].update("Jautājums atbildēts nepareizi!", background_color="red" )
    # ja atbild uz jautājumu nomainās jautājums un atbildes
    index += 1 
    if index < max_punkti:
        logs['-jaut-'].update(jautajumi[index]["jautajums"])
        for i in range(3):
            logs[f'-atb{i}-'].update(text=jautajumi[index]["atbildes"][i])
    # savādāk aizveras logs un attaisās cits logs kas parāda cik punkti ir no maksimāliem punktiem
    else:
        logs.close()

        img = "happy2.png"

        layout = [
            [org.Menu(saraksts)],
            [org.Text("Spēles beigas!", background_color="red")],
            [org.Text(f"Tu ieguvi {punkti} punktus no {max_punkti}! Yeyyyy ")],
            [org.Image(img)]
        ]
        logs = org.Window("MINĒŠANAS SPĒLE - ORGĀNI", layout, size=(750,550), icon="ikona.ico")
        

                                   
logs.close()