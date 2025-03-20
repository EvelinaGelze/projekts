import PySimpleGUI as org
 
 
# Izkārtojuma definīcija
saraksts=[['File',['Close']], ['Help'],['About']]
organs = [
        [org.Menu(saraksts)],
        
     ]  
logs = org.Window("ORGĀNU SPĒLE", organs, size=(900,650))


while True:
    event, values = logs.read()
 
    # Kā IZET, ja logs tiek aizvērts
    if event == org.WINDOW_CLOSED or event=='Close':
       break
    elif event=='About':
        org.popup('Autori: Emīls Ronis un Evelīna Ģelze')