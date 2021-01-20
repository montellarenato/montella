import guizero
import string
import numpy as np
import matplotlib.pyplot as plt



# apriamo il file in lettura
f = open("dati.txt", 'r')

# usiamo il metodo readlines 
# per ottenere una lista di righe del file

# stampiamo la prima riga
# print(f.readline()) 

# possiamo fare un ciclo e prendere riga per riga 

coordX = []
coordY = []

# da notare che posso fare un ciclo all'interno di un file
# direttamente sulle righe



from guizero import App, Text, TextBox, PushButton

def tasto0():
    output.append for riga in f:
        valori = str(f.readline())  # converto in stringa la riga
        Nval = len(valori)          # conto il numero di caratteri
        valori = valori.strip('\n') # elimino i lterminatore di riga
        valori = valori.split(',')  # separo la stringa in due numeri
        valori = list(valori)       # converto in lista
        print(valori)
        coordX.append(int(valori[0])) # aggiungo la coordinata X
        coordY.append(int(valori[1])) # aggiungo la coordinata Y
    f.close()  # chiudiamo il file

def tasto1():
    print ("X: ",coordX)
    print ("Y: ",coordY)
    coordX.sort()
    coordY.sort()
    print("liste ordinate:")
    print ("X: ",coordX)
    print ("Y: ",coordY)
    print(type(coordX))
    print(type(coordY))


def tasto2():
    plt.scatter(coordX,coordY)
    plt.plot(coordX,coordY)
    plt.ylabel('some numbers')
    plt.show()

app = App(title='interfaccia-grafico')

grafico_text = Text(app, text='Grafico', font = 'arial', size=40)

whatever = TextBox(app, width=50, multiline=True, height=2)
whatever.value='Interfaccia grafico'

push1 =PushButton(app, text='definire le coordinate', command=tasto0)

push2 =PushButton(app, text='coordinate', command=tasto1)

push3 = PushButton(app, text='grafico', command=tasto2)

app.bg="#000000"

grafico_text.text_color ="#FFFFFF"

whatever.bg="#FFFFFF"

push1.bg="#E52B50"

push2.bg="#CC9966"

push3.bg="#5E86C1"


