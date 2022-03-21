import tkinter as ui #sempre que formos modificar a ui agora, estaremos modificando o tkinder módulo
import time #importando o tempo atual
window = ui.Tk() #Tk tem que ser maiúsculo

def update_clock(): #Aqui estamos inserindo horas, minutos, segundos e dia ou noite (am-pm)
    hours = time.strftime('%I')
    minutes = time.strftime('%M') #a % deixará o relógio no formato americano (12 Hours)
    seconds = time.strftime ('%S')
    am_or_pm = time.strftime ('%p')
    time_text = hours + ':' + minutes + ':' + seconds + '' + am_or_pm
    digital_clock_lbl.config(text=time_text)
    digital_clock_lbl.after(1000, update_clock)#Depois de 1000 milesegundos(valor igual à 1 segundo) o relógio será atualizado
digital_clock_lbl = ui.Label (window, text="00:00:00",
                              font= "helvetica 72 bold") #Aqui será incluída a janela de display e o tempo, font facilitará a leitura dos números

digital_clock_lbl.pack () #Acrescenta os valores '00:00:00' acima

update_clock()#Atualizar o relógio em tempo real

window.mainloop() #Essa função diz ao python que todo o código relacionado ao window, está vindo da criação da janela da window e a main loop function

