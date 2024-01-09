##FUENTE: https://es.wikibooks.org/wiki/Python/Interfaz_gr%C3%A1fica_con_Tkinter/Gesti%C3%B3n_de_ventanas


#  método 'iconify' en un botón para minimizar la ventana cuando se haga click sobre él

# import tkinter
# from test_convertpdf import seleccionar_rutas


# root = tkinter.Tk()
# boton = tkinter.Button(root, text="Minimizar", command=root.iconify)
# boton.pack()
# root.mainloop()



# abre otra ventana y minimiza la ventana padre

# import tkinter

# def funcion():
#     otra_ventana = tkinter.Toplevel(root)
#     root.iconify()

# root = tkinter.Tk()
# boton = tkinter.Button(root, text="Abrir otra ventana", command=funcion)
# boton.pack()
# root.mainloop()


# geometry del tamaño y lugar de la ventana

# import tkinter
# import time

# def funcion():
#     root.iconify()
#     time.sleep(5)
#     root.deiconify()

# root = tkinter.Tk()
# root.title("test ventanas")
# root.geometry("600x600+100+50")
# boton = tkinter.Button(root, text="Minimizar", command=funcion)
# boton.pack()
# root.mainloop()



# #posición de 2 ventanas
# import tkinter

# # Primera ventana con valores positivos
# primer_ventana = tkinter.Tk()
# primer_ventana.geometry("300x300+0+0")

# #Medidas máximas
# primer_ventana.maxsize(500, 500)
# primer_ventana.minsize(500, 500)


# # A modo estetico le di un titulo
# primer_ventana.title("Posicion x=+0 y=+0")
# # Este tambien es estetico y no influye en el uso del metodo
# etiqueta = tkinter.Label(primer_ventana, text="Posicion x=+0 y=+0", width=100, height=100, anchor="center")
# etiqueta.pack()

# # Segunda ventana con valores negativos
# segunda_ventana = tkinter.Tk()
# segunda_ventana.geometry("200x300-0-0")
# segunda_ventana.maxsize(200, 300)
# segunda_ventana.minsize(200, 300)

# segunda_ventana.title("Posicion x=-0 y=-0")
# etiqueta = tkinter.Label(segunda_ventana, text="Posicion x=-0 y=-0", width=100, height=100, anchor="center")
# etiqueta.pack()

# primer_ventana.mainloop()
# segunda_ventana.mainloop()


# import tkinter
# import time

# def funcion():
#     root.state(newstate='normal')
#     time.sleep(5)
#     root.state(newstate='normal')

# # "normal"
# # "withdraw"
# # "iconic"

# root = tkinter.Tk()
# boton = tkinter.Button(root, text="Probando el metodo state", command=funcion)
# boton.pack()
# root.mainloop()