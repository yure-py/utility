#!/usr/bin/env python3

import tkinter as tk
import re

root = tk.Tk()
root.configure(padx=10, pady=10, bg="white")

# VAR
h1 = tk.IntVar()

labels = {
    "text": ":",
    "font": ("Arial", 12),
    "relief": "flat",
    "bg": "white",
}

hora1_var = tk.StringVar()
hora2_var = tk.StringVar()
minute1_var = tk.StringVar()
minute2_var = tk.StringVar()

# WIDGETS
# hora1

hora1 = tk.Label(root, text="Hora1:", bd=1, bg="white", pady=5, padx=5, relief="flat")

entrada_h1 = tk.Entry(root, width=2, relief="solid", bg="white", selectborderwidth=0, selectbackground="white",
                      highlightbackground="white", font=30, textvariable=hora1_var)

tk.Label(root, **labels).grid(row=1, column=2)

entrada_m1 = tk.Entry(root, width=2, relief="solid", bg="white", selectborderwidth=0, selectbackground="white",
                      highlightbackground="white", font=30, textvariable=minute1_var)

# hora 2
hora2 = tk.Label(root, text="Hora2:", bd=1, bg="white", pady=5, padx=5, relief="flat")

entrada_h2 = tk.Entry(root, width=2, relief="solid", bg="white", selectborderwidth=0, selectbackground="white",
                      highlightbackground="white", font=30, textvariable=hora2_var)

tk.Label(root, **labels).grid(row=2, column=2)

entrada_m2 = tk.Entry(root, width=2, relief="solid", bg="white", selectborderwidth=0, selectbackground="white",
                      highlightbackground="white", font=30, textvariable=minute2_var)


# Button and calculate
def calcular_tempo():
    if hora1_var.get() and hora2_var.get():
        h1 = int(hora1_var.get())
        h2 = int(hora2_var.get())

        if not(minute2_var.get() and minute2_var.get()):
            m1 = 0
            m2 = 0
        else:
            m1 = int(minute1_var.get())
            m2 = int(minute2_var.get())

        # Converter as horas e minutos em objetos datetime
        from datetime import datetime, timedelta
        hora1 = datetime(2023, 1, 1, h1, m1)
        hora2 = datetime(2023, 1, 1, h2, m2)

        # Tratamento para caso de horários cruzarem a meia-noite
        if hora1 > hora2:
            hora2 += timedelta(days=1)

        # Calcular a diferença entre as horas
        diferenca = hora2 - hora1

        # Extrair a diferença em horas e minutos
        diferenca_em_horas = diferenca.seconds // 3600  # 3600 segundos em uma hora
        diferenca_em_minutos = (diferenca.seconds // 60) % 60

        total.configure(text=str(diferenca))
        total.grid()




tk.Button(root, text="CALCULAR", bd=1, bg="white", pady=5, padx=5, relief="flat",
          command=calcular_tempo).grid(row=3, columnspan=4, sticky="WE", pady=(10, 0))

total = tk.Label(root, text="", bd=1, bg="white", font=(20), relief="flat")

# GRID
hora1.grid(row=1, column=0)
entrada_m1.grid(row=1, column=3)

hora2.grid(row=2, column=0)
entrada_m2.grid(row=2, column=3)

entrada_h1.grid(row=1, column=1)
entrada_h2.grid(row=2, column=1)

total.grid(row=99, column=0, columnspan=99, pady=10, padx=10)
total.grid_remove()

root.mainloop()



