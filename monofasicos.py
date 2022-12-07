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
    data = pd.read_csv(f"./Mono/{filename}.csv")
    data.insert(2, "lat", n_listaN[i], allow_duplicates=False)
    data.insert(3, "lon", n_listaO[i], allow_duplicates=False)
    list_data.append(data)
    i+=1
listo = pd.concat(list_data, ignore_index=True)
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
n7 = []
n6 = []
n5 = []
n4 = []
n3 = []
n2 = []
n1 = []
for i in range (0, 19960):
    if float(datos_finales.iloc[i,3]) > 120*1.07 and float(datos_finales.iloc[i,3]) <= 120*1.09:
        n7.append(datos_finales.iloc[i, :])
    elif float(datos_finales.iloc[i,3]) > 120*1.05 and float(datos_finales.iloc[i,3]) <= 120*1.07:
        n6.append(datos_finales.iloc[i, :])
    elif float(datos_finales.iloc[i,3]) >= 120*0.95 and float(datos_finales.iloc[i,3]) <= 120*1.05:
        n5.append(datos_finales.iloc[i, :])
    elif float(datos_finales.iloc[i,3]) > 120*0.93 and float(datos_finales.iloc[i,3]) < 120*0.95:
        n4.append(datos_finales.iloc[i, :])
    elif float(datos_finales.iloc[i,3]) > 120*0.91 and float(datos_finales.iloc[i,3]) <= 120*0.93:
        n3.append(datos_finales.iloc[i, :])
    elif float(datos_finales.iloc[i,3]) > 120*0.87 and float(datos_finales.iloc[i,3]) <= 120*0.91:
        n2.append(datos_finales.iloc[i, :])
    else:
        n1.append(datos_finales.iloc[i,:])
#Se crean los archivos que se utilizarán en Qgis
n7 = pd.DataFrame(n7)
n6 = pd.DataFrame(n6)
n5 = pd.DataFrame(n5)
n4 = pd.DataFrame(n4)
n3 = pd.DataFrame(n3)
n2 = pd.DataFrame(n2)
n1 = pd.DataFrame(n1)
n7.to_excel(r'./Mono/n7.xlsx', index = False)
n6.to_excel(r'./Mono/n6.xlsx', index = False)
n5.to_excel(r'./Mono/n5.xlsx', index = False)
n4.to_excel(r'./Mono/n4.xlsx', index = False)
n3.to_excel(r'./Mono/n3.xlsx', index = False)
n2.to_excel(r'./Mono/n2.xlsx', index = False)
n1.to_excel(r'./Mono/n1.xlsx', index = False)
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, SaveFormat

#Se crea un objeto Workbook para la creaci]on del .csv
workbook7 =  Workbook("./Mono/n7.xlsx")
workbook6 =  Workbook("./Mono/n6.xlsx")
workbook5 =  Workbook("./Mono/n5.xlsx")
workbook4 =  Workbook("./Mono/n4.xlsx")
workbook3 =  Workbook("./Mono/n3.xlsx")
workbook2 =  Workbook("./Mono/n2.xlsx")
workbook1 =  Workbook("./Mono/n1.xlsx")
# Se guarda el .xlsx como .csv
workbook7.save("./Mono/n7.csv" , SaveFormat.CSV)
workbook6.save("./Mono/n6.csv" , SaveFormat.CSV)
workbook5.save("./Mono/n5.csv" , SaveFormat.CSV)
workbook4.save("./Mono/n4.csv" , SaveFormat.CSV)
workbook3.save("./Mono/n3.csv" , SaveFormat.CSV)
workbook2.save("./Mono/n2.csv" , SaveFormat.CSV)
workbook1.save("./Mono/n1.csv" , SaveFormat.CSV)
