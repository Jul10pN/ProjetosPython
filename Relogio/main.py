from tkinter import *
import tkinter
from datetime import datetime

cor1 = "#fafcff" # Cor Braca
cor2 = "#3d3d3d" # Cor Preta

fundo = cor1
cor = cor2

# Janela principal
janela = Tk()
janela.title("Relogio digital")
janela.geometry("440x180")
janela.resizable(width = FALSE, height = FALSE)
janela.configure(bg = cor1)


tempo = datetime.now()

# Pegar hora e data do meu pc
hora = tempo.strftime("%H:%M:%S")
dia_semana = tempo.strftime("%A")
dia = tempo.day
mes = tempo.strftime("%B")
ano = tempo.strftime("%Y")

# função do relogio

def relogio():
    hora = tempo.strftime("%H:%M:%S")
    dia_semana = tempo.strftime("%A")
    dia = tempo.day
    mes = tempo.strftime("%B")
    ano = tempo.strftime("%Y")

    l1.config(text = hora)
    l1.after(200, relogio)
    l2.config(text = dia_semana + " " + str(dia) + "/" + str(mes) + "/" + str(ano))

l1 = Label(janela, text = "", font = ("Arial 80"), bg = fundo, fg = cor)
l1.grid(row=0, column = 0, sticky=NW, padx=5)

l2 = Label(janela, text = "", font = ("Arial 20"), bg = fundo, fg = cor)
l2.grid(row=1, column = 0, sticky=NW, padx=5)

relogio()

janela.mainloop()

