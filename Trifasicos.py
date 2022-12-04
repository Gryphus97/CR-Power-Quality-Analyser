import pandas as pd
datos = []
for i in range(1,10):
    nom = f"T-000{i}-2018"
    datos.append(nom)
for i in range(10,14):
    nom = f"T-00{i}-2018"
    datos.append(nom)
datos.append("T-0099-2018")
datos.append("T-0100-2018")
datos.append("T-0101-2018")
datos.remove("T-0005-2018")
control = pd.read_csv('Test2.csv', delimiter=',', decimal=".")
coorN = []
coorO = []
for x in range(0,261):
    for i in range(0,15):
        if control.iloc[x, 0] == datos[i]:
            coorN.append(control.iloc[x, 8])
for x in range(0,261):
    for i in range(0,15):
        if control.iloc[x, 0] == datos[i]:
            coorO.append(control.iloc[x, 9])
n_listaN = []
n_listaO = []
for i in range(0,15):
    lista = list(coorN[i])
    if lista[0] == "N":
        lista.pop(0)
    n_listaN.append(''.join(lista))
for i in range(0, 15):
    lista = list(coorO[i])
    if lista[0] == "O":
        lista[0] = "-"
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
datos_completos = datos_completos.set_index('Date', append=False, drop=False)
datos_completos['Tiempo'] = datos_completos.Date.str.cat(datos_completos.Time, sep=' ')
datos_tiempo2 = datos_completos.loc[:,["Tiempo", "lat", "lon","'UL1_[V]'","'UL2_[V]'","'UL3_[V]'"]]
datos_tiempo = datos_tiempo2.drop_duplicates()
print(datos_tiempo)
tamaño = datos_tiempo.loc[:,"Tiempo"].size
timei =[]
for i in range(0, tamaño):
    lista = list(datos_tiempo.iloc[i, 0])
    lista.insert(0,"2018/")
    lista.pop(7)
    lista.pop(7)
    lista.pop(7)
    lista.pop(7)
    lista.pop(6)
    timei.append(''.join(lista))

for i in range(0, tamaño):
    lista = list(timei[i])
    d = lista[5]+lista[6]
    m = lista[8]+lista[9]
    lista[8]=d
    lista.pop(9)
    lista[5] = m
    lista.pop(6)
    timei[i] =''.join(lista)
print(datos_tiempo)
datos_tiempo.loc[:,"Tiempo"] = timei
n9 = []
n8 = []
n7 = []
for i in range (0, 15104):
    if float(datos_tiempo.iloc[i,3]) > 120*1.13 and float(datos_tiempo.iloc[i,4]) > 120*1.13 and float(datos_tiempo.iloc[i,5]) > 120*1.13:
        n9.append(datos_tiempo.iloc[i,:])
    elif (float(datos_tiempo.iloc[i,3]) and float(datos_tiempo.iloc[i,4]) and float(datos_tiempo.iloc[i,5])) <= 120*1.13 or (float(datos_tiempo.iloc[i,3]) and float(datos_tiempo.iloc[i,4]) and float(datos_tiempo.iloc[i,5]))> 120*1.09:
        n8.append(datos_tiempo.iloc[i, :])
    else:
        n7.append(datos_tiempo.iloc[i,:])
n7= pd.DataFrame(n7)
n8 = pd.DataFrame(n8)
n9 = pd.DataFrame(n9)
n7.to_excel(r'tn7.xlsx', index = False)
n8.to_excel(r'tn8.xlsx', index = False)
n9.to_excel(r'tn9.xlsx', index = False)
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, SaveFormat

workbook7 =  Workbook("tn7.xlsx")
workbook8 =  Workbook("tn8.xlsx")
workbook9 =  Workbook("tn9.xlsx")


workbook7.save("tn7.csv" , SaveFormat.CSV)
workbook8.save("tn8.csv" , SaveFormat.CSV)
workbook9.save("tn9.csv" , SaveFormat.CSV)


