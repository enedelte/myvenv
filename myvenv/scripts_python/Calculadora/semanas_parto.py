import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta

class CalculadoraGestacionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Gestación")

        self.label_fecha_eco = ttk.Label(root, text="Fecha ECO (dd/mm/yyyy):")
        self.label_fecha_eco.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_fecha_eco = ttk.Entry(root)
        self.entry_fecha_eco.grid(row=0, column=1, padx=5, pady=5)

        self.label_semanas_eco = ttk.Label(root, text="Semanas ECO:")
        self.label_semanas_eco.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_semanas_eco = ttk.Entry(root)
        self.entry_semanas_eco.grid(row=1, column=1, padx=5, pady=5)

        self.label_fecha_parto = ttk.Label(root, text="Fecha de Parto (dd/mm/yyyy):")
        self.label_fecha_parto.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_fecha_parto = ttk.Entry(root)
        self.entry_fecha_parto.grid(row=2, column=1, padx=5, pady=5)

        self.result_label = ttk.Label(root, text="")
        self.result_label.grid(row=3, column=0, columnspan=2, pady=10)

        self.calcular_button = ttk.Button(root, text="Calcular", command=self.calcular)
        self.calcular_button.grid(row=4, column=0, columnspan=2, pady=10)

    def calcular(self):
        fecha_eco = self.entry_fecha_eco.get()
        semanas_eco = self.entry_semanas_eco.get()
        fecha_parto = self.entry_fecha_parto.get()

        calculadora = CalculadoraGestacion(fecha_eco, semanas_eco, fecha_parto)

        resultado = (
            f"Semanas hasta el parto: {calculadora.calcular_semanas_hasta_parto()} semanas\n"
            f"Fecha probable de parto: {calculadora.calcular_fecha_probable_parto()}\n"
            f"Fecha a las 38 semanas: {calculadora.calcular_fecha_38_semanas()}"
        )

        self.result_label.config(text=resultado)

class CalculadoraGestacion:
    def __init__(self, fecha_eco, semanas_eco, fecha_parto):
        self.fecha_eco = datetime.strptime(fecha_eco, "%d/%m/%Y")
        self.semanas_eco = int(semanas_eco)
        self.fecha_parto = datetime.strptime(fecha_parto, "%d/%m/%Y")

    def calcular_semanas_hasta_parto(self):
        semanas_hasta_parto = (self.fecha_parto - self.fecha_eco).days // 7
        return semanas_hasta_parto

    def calcular_fecha_probable_parto(self):
        fecha_probable_parto = self.fecha_eco + timedelta(weeks=40)
        return fecha_probable_parto.strftime("%d/%m/%Y")

    def calcular_fecha_38_semanas(self):
        fecha_38_semanas = self.fecha_eco + timedelta(weeks=38)
        return fecha_38_semanas.strftime("%d/%m/%Y")

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraGestacionGUI(root)
    root.mainloop()
