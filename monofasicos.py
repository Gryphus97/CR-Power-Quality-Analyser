import pandas as pd
#Se crea una lista con los nombres de los archivos
datos = []
for i in range(56,76):
    nom = f"M-07{i}-2018"
    datos.append(nom)
datos.remove("M-0772-2018")
#Se crea una lista con las coordenadas correspondientes a cada archivo
coor = []
control = pd.read_csv('Test1.csv', delimiter=',', decimal=".")
for x in range(0,1264):
    for i in range(0,19):
        if control.iloc[x, 0] == datos[i]:
            coor.append(control.iloc[x, 8])
#Se transforman las coordenadas al formato requerido por Qgis
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
#Se convierten los datos en un dataframe y se unen todos los archivos
list_data = []
i = 0
for filename in datos:
    data = pd.read_csv(f"{filename}.csv")
    data.insert(2, "lat", n_listaN[i], allow_duplicates=False)
    data.insert(3, "lon", n_listaO[i], allow_duplicates=False)
    list_data.append(data)
    i+=1
listo = pd.concat(list_data, ignore_index=True)
#Se seleccionan los datos de cada hora
datos_completos = pd.DataFrame(listo)
datos_completos = datos_completos.set_index('Time', append=False, drop=False)
#Se escogen las columnas requeridas para el analisis
datos_tiempo = datos_completos.loc[:,["Time", "lat", "lon","Phase C-A Min Volts"]]
tamaño = datos_tiempo.loc[:,"Time"].size
#Se convierten los datos de las fechas en uno que Qgis pueda interpretar
n_listaT = []
for i in range(0, tamaño):
    lista = list(datos_tiempo.iloc[i, 0])
    if lista[3] == "J" and lista[4] == "u" and lista[5] == "l":
        lista[3] = "07"
        lista.pop(4)
        lista.pop(5)
        lista[4] = "-"
    n_listaT.append(''.join(lista))
datos_tiempo.loc[:,"Time"] = n_listaT
datos_finales = datos_tiempo.drop_duplicates()
#Se clasifican los voltajes minimos
n9 = []
n8 = []
n7 = []
for i in range (0, 3327):
    if float(datos_finales.iloc[i,3]) > 120*1.13:
        n9.append(datos_finales.iloc[i,:])
    elif float(datos_finales.iloc[i,3]) > 120*1.09 or float(datos_finales.iloc[i,3]) <= 120*1.13:
        n8.append(datos_finales.iloc[i, :])
    else:
        n7.append(datos_finales.iloc[i,:])
#Se crean los archivos que se utilizarán en Qgis
n8 = pd.DataFrame(n8)
n9 = pd.DataFrame(n9)
n7 = pd.DataFrame(n9)
n8.to_excel(r'n8.xlsx', index = False)
n9.to_excel(r'n9.xlsx', index = False)
n7.to_excel(r'n7.xlsx', index = False)
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, SaveFormat

#Se crea un objeto Workbook para la creaci]on del .csv
workbook8 =  Workbook("n8.xlsx")
workbook9 =  Workbook("n9.xlsx")
workbook7 =  Workbook("n7.xlsx")
# Se guarda el .xlsx como .csv
workbook8.save("n8.csv" , SaveFormat.CSV)
workbook9.save("n9.csv" , SaveFormat.CSV)
workbook9.save("n7.csv" , SaveFormat.CSV)
