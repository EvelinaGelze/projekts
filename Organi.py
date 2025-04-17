import PySimpleGUI as org
import random
from tkinter import messagebox
 
# Izkārtojuma definīcija
saraksts=[['File',['Close']], ['Help'],['About']]
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
