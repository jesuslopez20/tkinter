import tkinter as tk
ventana=tk.Tk()
ventana.geometry("400x500")
ventana.title("aplicacion")



c1 = tk.Label(ventana, text= "Calificación 1", bg="#ffb74d", fg="white")
c1.pack(padx=5, pady=4, ipadx=5, ipady=5, fill=tk.X)
entrada1 = tk.Entry(ventana)
entrada1.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)


c2 = tk.Label(ventana, text= "Calificación 2", bg="#ffb74d", fg="white")
c2.pack(padx=5, pady=4, ipadx=5, ipady=5, fill=tk.X)
entrada2 = tk.Entry(ventana)
entrada2.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)


c3= tk.Label(ventana, text= "Calificación 3", bg="#ffb74d", fg="white")
c3.pack(padx=5, pady=4, ipadx=5, ipady=5, fill=tk.X)
entrada3 = tk.Entry(ventana)
entrada3.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

ef= tk.Label(ventana, text= "examen final", bg="#ffb74d", fg="white")
ef.pack(padx=5, pady=4, ipadx=5, ipady=5, fill=tk.X)
entrada4 = tk.Entry(ventana)
entrada4.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

tf= tk.Label(ventana, text= "trabajo final", bg="#ffb74d", fg="white")
tf.pack(padx=5, pady=4, ipadx=5, ipady=5, fill=tk.X)
entrada3 = tk.Entry(ventana)
entrada3.pack(padx=5, pady=5, ipadx=5, ipady=5, fill=tk.X)

class CalificacionFinal():
    def __init__(self):
        self.ope=prom=(c1 + c2 + c3)/3
        self.ope= ppar = prom * 0.55
        self.ope=pef = ef * 0.30
        self.ope=ptf = tf * 0.15
        self.ope=cf = ppar + pef + ptf

resultado= tk.Label(ventana, textvariable = float, padx = 5, pady= 5, width = 50)
resultado.pack()
boton1 = tk.Button(ventana, text= "Resultado", bg = "#42a5f5", command = CalificacionFinal)
boton1.pack(side= tk.TOP)



ventana.mainloop()