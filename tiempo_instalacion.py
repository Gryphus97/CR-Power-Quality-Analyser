import pandas as pd
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, SaveFormat

#Se convierte el archivo Test.xlsx a formato .csv
workbook =  Workbook("Test1.xlsx")
workbook.save("Test1.csv", SaveFormat.CSV)
#Se crea un dataframe con el archivo creado
datos = pd.read_csv('Test1.csv', delimiter=',', decimal=".")
datos_completos = pd.DataFrame(datos)
#Se escogen las columnas a analizar
datos_tiempo = datos_completos.loc[:,["Fecha_de_instalación","Hora_instalación","Fecha_de_desinstalación", "Hora_desinstalación", "N° de equipo"]]
coor = datos_completos.loc[:,"Coordenadas"]
tamaño = datos_completos.loc[:,"Coordenadas"].size
#Se convierten las coordenadas a un formato aceptable en Qgis
n_listaN = []
n_listaO = []
for i in range(0,1264):
    lista = list(coor.iloc[i])
    if lista[0] == "N":
        lista.pop(0)
        for i in range(0,10):
            lista.pop()
    n_listaN.append(''.join(lista))
    print(lista)
for i in range(0, 1264):
    lista = list(coor.iloc[i])
    if lista[10] == "O" or lista[10] == "N":
        lista[10] = "-"
        for i in range(0,9):
            lista.pop(0)
    n_listaO.append(''.join(lista))
datos_tiempo = datos_tiempo.drop(1264,axis=0)
datos_tiempo.insert(3, "lon", n_listaO, allow_duplicates=False)
datos_tiempo.insert(4, "lat", n_listaN, allow_duplicates=False)
datos_tiempo['Fecha de instalacion'] = datos_tiempo.Fecha_de_instalación.str.cat(datos_tiempo.Hora_instalación, sep=' ')
datos_tiempo['Fecha de desinstalacion'] = datos_tiempo.Fecha_de_desinstalación.str.cat(datos_tiempo.Hora_desinstalación, sep=' ')
datos_tiempo = datos_tiempo.drop(columns=["Fecha_de_instalación", "Hora_instalación", "Fecha_de_desinstalación", "Hora_desinstalación"])
#Se convierten los datos a un archivo .xlsl y porteriormente a uno .csv
datos_tiempo.to_excel(r'tiempo_ins.xlsx', index = False)


# Create a Workbook object with Excel file's path
workbook =  Workbook("tiempo_ins.xlsx")

# Save XLSX as CSV
workbook.save("tiempo_ins.csv" , SaveFormat.CSV)
