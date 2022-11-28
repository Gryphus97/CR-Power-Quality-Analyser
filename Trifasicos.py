import pandas as pd
datos = []
for i in range(1,10):
    nom = f"T-000{i}-2018E"
    datos.append(nom)
for i in range(10,14):
    nom = f"T-00{i}-2018E"
    datos.append(nom)
datos.append("T-0099-2018E")
datos.append("T-0100-2018E")
datos.append("T-0101-2018E")
datos.remove("T-0005-2018E")
coor = ["N10.65724 O85.61490","N09.95525 O85.04046","N10.63083 O85.43741","N09.98134 O85.31295","N10.54201 O85.71339","N10.54175 O85.70926","N10.57916 O85.65362","N10.52630 O85.64328", "N10.51254 O85.64801", "N10.51346 O85.64502", "N10.51708 O85.57236", "N10.51665 O85.57873", "N10.44874 O85.55193","N10.44805 O85.55356", "N10.51746 O85.64714", "N10.51515 O85.64752"]

n_listaN = []
n_listaO = []
for i in range(0,16):
    lista = list(coor[i])
    if lista[0] == "N":
        lista.pop(0)
        for i in range(0,10):
            lista.pop()
    n_listaN.append(''.join(lista))
for i in range(0, 16):
    lista = list(coor[i])
    if lista[10] == "O" or lista[10] == "N":
        lista[10] = "-"
        for i in range(0,9):
            lista.pop(0)
    n_listaO.append(''.join(lista))
list_data = []
i = 0
for filename in datos:
    data = pd.read_csv(f"{filename}.csv")
    data.insert(2, "lat", n_listaN[i], allow_duplicates=False)
    data.insert(3, "lon", n_listaO[i], allow_duplicates=False)
    list_data.append(data)
    i+=1
caida = pd.concat(list_data, ignore_index=True)

# del(interrupcion['dato des'])
# del(interrupcion['segundo dat'])
# del(interrupcion['0'])
del(caida['dato des'])
del(caida['segundo dat'])
del(caida['0'])
tamaño = caida.loc[:,"Hora inicio"].size
cai =[]
caf =[]
cae =[]
inti = []
intf = []
for i in range(0, tamaño):
    lista = list(caida.iloc[i, 3])
    lista.insert(0,"2018.")
    lista.pop(7)
    lista.pop(7)
    lista.pop(7)
    lista.pop(7)
    lista.pop(6)
    cai.append(''.join(lista))
for i in range(0, tamaño):
    lista = list(caida.iloc[i, 5])
    lista.insert(0,"2018.")
    lista.pop(7)
    lista.pop(7)
    lista.pop(7)
    lista.pop(7)
    lista.pop(6)
    caf.append(''.join(lista))
for i in range(0, tamaño):
    lista = list(caida.iloc[i, 0])
    lista[2] = "i"
    cae.append(''.join(lista))
# for i in range(0, tamaño):
#     lista = list(caida.iloc[i, 1])
#     lista.insert(0,"2018.")
#     lista.pop(7)
#     lista.pop(7)
#     lista.pop(6)
#     inti.append(''.join(lista))
# for i in range(0, tamaño):
#     lista = list(caida.iloc[i, 3])
#     lista.insert(0,"2018.")
#     lista.pop(7)
#     lista.pop(7)
#     lista.pop(7)
#     lista.pop(6)
#     intf.append(''.join(lista))
for i in range(0, tamaño):
    lista = list(cai[i])
    d = lista[5]+lista[6]
    m = lista[8]+lista[9]
    lista[8]=d
    lista.pop(9)
    lista[5] = m
    lista.pop(6)
    cai[i] =''.join(lista)
for i in range(0, tamaño):
    lista = list(caf[i])
    d = lista[5]+lista[6]
    m = lista[8]+lista[9]
    lista[8]=d
    lista.pop(9)
    lista[5] = m
    lista.pop(6)
    caf[i] =''.join(lista)
caida.loc[:,"Hora inicio"] = cai
caida.loc[:,"Hora final"] = caf
caida.loc[:,"Evento"] = cae
# caida.loc[:,"Hora inicio"] = inti
# caida.loc[:,"Hora final"] = intf
caida.to_excel(r'caida.xlsx', index = False)
# interrupcion.to_excel(r'interrupcion.xlsx', index = False)
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, SaveFormat

# Create a Workbook object with Excel file's path
workbook =  Workbook("caida.xlsx")
# workbook2 =  Workbook("interrupcion.xlsx")

# Save XLSX as CSV
workbook.save("caida.csv" , SaveFormat.CSV)
# workbook.save("interrupcion.csv" , SaveFormat.CSV)
