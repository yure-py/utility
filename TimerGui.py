#!/usr/bin/env python3
import os
import time
import timeit
import tkinter as tk
from tkinter import ttk
from playsound import playsound

class Settings:
    def __init__(self):
        self.comboboxes = {
            "width": 3,
            "font": ("Arial", 18),
            "state": "readonly",
            "justify": "center",
            "values": [f"0{x}" if x < 10 else str(x) for x in range(24)],
        }
        self.button = {
            "bg": "white",
            "relief": "solid",
        }
        self.labels = {
            "text": ":",
            "font": ("Arial", 12),
            "relief": "flat",
            "bg": "white",
        }

        self.var1 = tk.StringVar(value="00")
        self.var2 = tk.StringVar(value="00")
        self.var3 = tk.StringVar(value="00")

        self.style = ttk.Style()

class Main(Settings):
    def __init__(self, root):
        super().__init__()
        self.root = root
        self.pause = False

        # widgets
        self.f_clock = tk.Frame(root, bg="white", relief="solid", bd=1, pady=5, padx=5)

        self.hour = ttk.Combobox(self.f_clock, textvariable=self.var1, **self.comboboxes)
        self.minute = ttk.Combobox(self.f_clock, textvariable=self.var2, **self.comboboxes)
        self.second = ttk.Combobox(self.f_clock, textvariable=self.var3, **self.comboboxes)

        self.label1 = tk.Label(self.f_clock, **self.labels)
        self.label2 = tk.Label(self.f_clock, **self.labels)

        self.button_start = tk.Button(root, command=self.clock, text=u"\u25b6", **self.button)
        self.button_pause = tk.Button(root, text=u"\u25FB", command=self.pausecommand, **self.button)

        self.configuration_and_grid()
        self.style_configure()
        self.binding_clear_selection()

    def style_configure(self):
        self.style.layout(
            "NoIndicator.TCombobox",
            [
                (
                    "Combobox.border",
                    {"children": [("Combobox.padding", {"children": [("Combobox.textarea", {"sticky": "nswe"})]})]},
                ),
            ],
        )
        self.style.configure("NoIndicator.TCombobox", background="white")

    def configuration_and_grid(self):
        self.minute["values"] = [f"0{x}" if x < 10 else str(x) for x in range(60)]
        self.second["values"] = [f"0{x}" if x < 10 else str(x) for x in range(60)]

        self.hour.grid(row=0, column=0)
        self.minute.grid(row=0, column=2)
        self.second.grid(row=0, column=4)

        self.hour["style"] = "NoIndicator.TCombobox"
        self.minute["style"] = "NoIndicator.TCombobox"
        self.second["style"] = "NoIndicator.TCombobox"

        self.button_start.grid(row=0, column=0, pady=7, padx=(10, 0), ipady=0, ipadx=12)
        self.button_pause.grid(row=0, column=1, padx=(0, 10), ipady=0, ipadx=12)

        self.f_clock.grid(row=1, columnspan=2, pady=(0, 20), padx=9, sticky="nsew")

        self.label1.grid(row=0, column=1, sticky="ns")
        self.label2.grid(row=0, column=3, sticky="ns")

    def binding_clear_selection(self):
        def helper(widget):
            return widget.bind("<<ComboboxSelected>>", lambda e: widget.selection_clear())

        helper(self.hour)
        helper(self.minute)
        helper(self.second)

    def pausecommand(self):
        self.pause = not self.pause

    def clock(self):
        h, m, s = [int(x) for x in [self.var1.get(), self.var2.get(), self.var3.get()]]
        self.update_combos(h, m, s)

    def update_combos(self, h, m, s):
        def update_var(widget, var):
            if var >= 10:
                widget.set(str(var))
            else:
                widget.set(f"0{var}")

        if s >= 0 and not self.pause:
            update_var(self.second, s)
            update_var(self.minute, m)
            update_var(self.hour, h)

            if s == 0:
                if m > 0:
                    s = 60
                    m -= 1
                else:
                    if h > 0:
                        h -= 1
                        m = 59
                        s = 60

            self.second.after(1000, lambda: self.update_combos(h, m, s - 1))

            if s == 0 and m == 0 and h == 0:
                playsound("a.mp3")
        self.pause = False




if __name__ == "__main__":
    root = tk.Tk()
    root.title("Cronometro.py")
    root.geometry("+1500-700")
    root.resizable(False, False)
    root.configure(bg="white")

    start = Main(root)
    root.mainloop()
