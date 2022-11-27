import pandas as pd
datos = []
for i in range(56,76):
    nom = f"M-07{i}-2018"
    datos.append(nom)
datos.remove("M-0772-2018")
coor = []
control = pd.read_csv('Test1.csv', delimiter=',', decimal=".")
for x in range(0,1264):
    for i in range(0,19):
        if control.iloc[x, 0] == datos[i]:
            coor.append(control.iloc[x, 8])
n_listaN = []
n_listaO = []
for i in range(0,19):
    lista = list(coor[i])
    if lista[0] == "N":
        lista.pop(0)
        for i in range(0,10):
            lista.pop()
    n_listaN.append(''.join(lista))
for i in range(0, 19):
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
listo = pd.concat(list_data, ignore_index=True)

datos_completos = pd.DataFrame(listo)
datos_completos = datos_completos.set_index('Time', append=False, drop=False)
fecha_in = []
for i in range(0, 19960):
    lista = list(datos_completos.iloc[i, 0])
    for x in range(0,10):
        if lista[1] == str(x):
            for h in range(0, 3):
                for m in range(0,10):
                    if lista[12] == str(h) and lista[13] == str(m) and lista[15] == "0" and lista[16] == "0":
                        fecha_in.append(''.join(lista))

datos_tiempo = datos_completos.loc[fecha_in,["Time", "lat", "lon","Phase C-A Min Volts"]]
final = datos_completos.loc[fecha_in,"Time"]
final = final.to_numpy().tolist()
datos_tiempo.insert(1, "End", final, allow_duplicates=False)
tamaño = datos_tiempo.loc[:,"Time"].size
n_listaT = []
n_listaE = []
for i in range(0, tamaño):
    lista = list(datos_tiempo.iloc[i, 0])
    if lista[3] == "J" and lista[4] == "u" and lista[5] == "l":
        lista[3] = "07"
        lista.pop(4)
        lista.pop(5)
        lista[4] = "-"
    n_listaT.append(''.join(lista))
for i in range(0, tamaño):
    lista = list(datos_tiempo.iloc[i, 1])
    if lista[3] == "J" and lista[4] == "u" and lista[5] == "l":
        lista[3] = "07"
        lista.pop(4)
        lista.pop(5)
        lista[4] = "-"
    n_listaE.append(''.join(lista))

datos_tiempo.loc[:,"Time"] = n_listaT
datos_tiempo.loc[:,"End"] = n_listaE
n9 = []
n8 = []
for i in range (0, 59917):
    if float(datos_tiempo.iloc[i,4]) > 113:
        n9.append(datos_tiempo.iloc[i,:])
    else:
        n8.append(datos_tiempo.iloc[i,:])

n8 = pd.DataFrame(n8)
n9 = pd.DataFrame(n9)
n8.to_excel(r'n8.xlsx', index = False)
n9.to_excel(r'n9.xlsx', index = False)
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, SaveFormat

# Create a Workbook object with Excel file's path
workbook8 =  Workbook("n8.xlsx")
workbook9 =  Workbook("n9.xlsx")

# Save XLSX as CSV
workbook8.save("n8.csv" , SaveFormat.CSV)
workbook9.save("n9.csv" , SaveFormat.CSV)
