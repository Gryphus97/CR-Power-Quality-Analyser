import sys 
import tkinter as tk
from tkinter import ttk, messagebox
import layer_generator as lg

#Interfaz gráfica básica creada con tkinter
if __name__ == "__main__":
    
    root = tk.Tk()

    root.geometry("500x300")
    root.title("Calidad eléctrica Costa Rica")
    
    tabControl = ttk.Notebook(root)
    
    tmono = ttk.Frame(tabControl)
    ttri = ttk.Frame(tabControl)
    
    tabControl.add(tmono, text='Servicios monofásicos')
    tabControl.add(ttri, text='Servicios trifásicos')
    tabControl.pack(expand=1, fill="both")
    
    #Servs mono
    
    lyr1 = tk.Label(tmono, text = 'Indicar año de estudio')
    lyr1.place(relx=0.3,rely=0.1)
    inptxt1 = tk.Text(tmono,height=1.5, width=10)
    inptxt1.place(relx=0.37,rely=0.2)
    bloadlyr = tk.Button(tmono, text='Cargar archivo de\n coordenadas mono.')
    bloadlyr.place(relx=0.1,rely=0.4,width=160)
    bheatmp = tk.Button(tmono, text='Generar mapa de calor\n de mediciones')
    bheatmp.place(relx=0.5,rely=0.4, width=160)
    btimel = tk.Button(tmono, text='Visualizar semana de \n mediciones')
    btimel.place(relx=0.3,rely=0.7 , width=160)
    
    # Servs tri
    #ttk.Label(ttri, text="Acá se colocarán botones para servicios tri").grid(column=0,row=0,padx=50,pady=50)
    
    lyr3 = tk.Label(ttri, text = 'Indicar año de estudio')
    lyr3.place(relx=0.3,rely=0.1)
    inptxt3 = tk.Text(ttri,height=1.5, width=10)
    inptxt3.place(relx=0.37,rely=0.2)
    bloadlyr3 = tk.Button(ttri, text='Cargar archivo de\n coordenadas tri.')
    bloadlyr3.place(relx=0.1,rely=0.4,width=160)
    bheatmp3 = tk.Button(ttri, text='Generar mapa de calor\n de mediciones')
    bheatmp3.place(relx=0.5,rely=0.4, width=160)
    btimel3 = tk.Button(ttri, text='Visualizar semana de \n mediciones')
    btimel3.place(relx=0.3,rely=0.7 , width=160)

    root.mainloop()
    