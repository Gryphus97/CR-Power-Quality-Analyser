import pandas as pd

datos1 = pd.read_csv('M-0565-2022.csv', delimiter=',', decimal=".")
datos2 = pd.read_csv('M-0566-2022.csv', delimiter=',', decimal=".")
datos3 = pd.read_csv('M-0567-2022.csv', delimiter=',', decimal=".")
datos4 = pd.read_csv('M-0568-2022.csv', delimiter=',', decimal=".")
datos1.insert(2, "lat", "9.848634400644745", allow_duplicates=False)
datos1.insert(3, "lon", "-84.31491096137044", allow_duplicates=False)
datos2.insert(2, "lat", "10.71553", allow_duplicates=False)
datos2.insert(3, "lon", "-85.62812", allow_duplicates=False)
datos3.insert(2, "lat", "09.95461", allow_duplicates=False)
datos3.insert(3, "lon", "-85.03797", allow_duplicates=False)
datos4.insert(2, "lat", "09.99357", allow_duplicates=False)
datos4.insert(3, "lon", "-85.28716", allow_duplicates=False)
datos5 = pd.concat([datos1, datos2, datos3, datos4])

datos_completos = pd.DataFrame(datos5)
datos_completos = datos_completos.set_index('Time', append=False, drop=False)
fecha_in = []
fecha_in = []
lista = list(datos_completos.iloc[3,0])
for i in range(0, 1439):
    lista = list(datos_completos.iloc[i, 0])
    for x in range(0,10):
        if lista[1] == str(x):
            for h in range(0, 3):
                for m in range(0,10):
                    if lista[12] == str(h) and lista[13] == str(m) and lista[15] == "0" and lista[16] == "0":
                        fecha_in.append(''.join(lista))
datos_tiempo = datos_completos.loc[fecha_in,["Time", "lat", "lon","Phase C-A Avg Volts"]]
final = datos_completos.loc[fecha_in,"Time"]
final = final.to_numpy().tolist()
datos_tiempo.insert(1, "End", final, allow_duplicates=False)
tamaño = datos_tiempo.loc[:,"Time"].size
n_listaT = []
n_listaE = []
for i in range(0, tamaño):
    lista = list(datos_tiempo.iloc[i, 0])
    if lista[3] == "O" and lista[4] == "c" and lista[5] == "t":
        lista[3] = "10"
        lista.pop(4)
        lista.pop(5)
        lista[4] = "-"
    elif lista[3] == "N" and lista[4] == "o" and lista[5] == "v":
        lista[3] = "11"
        lista.pop(4)
        lista.pop(5)
        lista[4] = "-"
    n_listaT.append(''.join(lista))
for i in range(0, tamaño):
    lista = list(datos_tiempo.iloc[i, 1])
    if lista[3] == "O" and lista[4] == "c" and lista[5] == "t":
        lista[3] = "10"
        lista.pop(4)
        lista.pop(5)
        lista[4] = "-"
    elif lista[3] == "N" and lista[4] == "o" and lista[5] == "v":
        lista[3] = "11"
        lista.pop(4)
        lista.pop(5)
        lista[4] = "-"
    n_listaE.append(''.join(lista))

datos_tiempo.loc[:,"Time"] = n_listaT
datos_tiempo.loc[:,"End"] = n_listaE

n9 = []
n8 = []
for i in range (0, 953):
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


