import PySimpleGUI as org
from tkinter import messagebox
 
# Izkārtojuma definīcija
saraksts=[['File',['Close']], ['Help'],['About']]
organs = [
        [org.Menu(saraksts)],
        [org.Text( )],
        [org.T("                   "), org.Radio( 'Radio1', default=False, key='-atb0-')],
        [org.T("                   "), org.Radio( 'Radio1', default=False, key='-atb1-')],
        [org.T("                   "), org.Radio( 'Radio1', default=False, key='-atb2-')],
        [org.Button("Pareizi/Nepareizi!"), org.Button("Nākamais jautājums!")],









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
