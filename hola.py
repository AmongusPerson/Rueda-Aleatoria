from tkinter import *
te = Tk()
te.title("Serie")
te.geometry("500x500")
titulo = Label(te, text="Serie de Adicion")
titulo.place(relx=0.5, rely=0.03, anchor=CENTER)
hola = Label(te, text="hola")
hola.place(relx=0.5, rely=0.08, anchor=CENTER)
def fun():
    sere1 = [1,2,3]
    serie2 = sere1[0]
    serie3 = serie2 + 1
    hola["text"] = serie3
    
boton = Button(te, text="adios", command=fun, bg="#e9c46a")
boton.place(relx=0.5, rely=0.15, anchor=CENTER,)
te.mainloop()