import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Interfaz QGIS-Python")

tabControl = ttk.Notebook(root)

tmono = ttk.Frame(tabControl)
ttri = ttk.Frame(tabControl)

tabControl.add(tmono, text='Servicios monofásicos')
tabControl.add(ttri, text='Servicios trifásicos')
tabControl.pack(expand=1, fill="both")

ttk.Label(tmono, text="Acá se colocarán botones para servicios mono").grid(column=0,row=0,padx=50,pady=50)
ttk.Label(ttri, text="Acá se colocarán botones para servicios tri").grid(column=0,row=0,padx=50,pady=50)

root.mainloop()