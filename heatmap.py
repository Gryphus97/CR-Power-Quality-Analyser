################ Heatmap raster from code ###########################
import sys

#Global
#####################################################################
tgt_lyr = "../Q_Tests/SHP/total_meds2018.shp"
tgt_prj = "../Mediciones_ARESEP_QGIS/GIS_2022_Med.qgs"
outpt = '/home/gryphus/Estructuras_datos/Proyecto_QGIS/Q_Tests/RAST/test.tiff' #archivo destino

procss     = '/usr/share/qgis/python/plugins'            #Especificar (processing plugins)
qgis_libs  = '/usr/lib/python3/dist-packages'            #Especificar (QGIS core libraries)
qgis_libs2 = '/usr/lib'

#Como no son propias de Python, se deben indicar por aparte estas librerias
sys.path.append(procss)                                  #add elements to python path
sys.path.append(qgis_libs)
sys.path.append(qgis_libs2)

from qgis.core import (QgsApplication,QgsProject, QgsField,QgsVectorLayer,QgsPathResolver)
from qgis.analysis import QgsNativeAlgorithms
from PyQt5.QtCore import QVariant
import processing        
from processing.core.Processing import Processing

#Code
#####################################################################

#Se crea simula una ejecución de qgis
QgsApplication.setPrefixPath("/usr", True)
qgs = QgsApplication([], True)

#Se inicializa, por lo que ya se tiene acceso a objetos del programa
qgs.initQgis()

#Se carga proyecto
proj_tgt = QgsProject.instance()
proj_tgt.read(tgt_prj)

#Se carga capa 
vlayer = QgsVectorLayer(tgt_lyr,"Meds_2022","ogr")

#Se crea nuevo campo temporal
newfld = vlayer.dataProvider()
newfld.addAttributes([QgsField("NC_num",QVariant.Int)])
vlayer.updateFields()   #inserte campo vacío
vlayer.startEditing()

features = vlayer.getFeatures()     #Se obtienen características de registros
for f in features:
    scale = 0                       #por defecto no hay peso
    id=f.id()                                       #id from row
    tipo_NC = f.attributes()[17]                    #se guarda valor de tipo de NC
    if tipo_NC      == 'Poca Importancia':
        scale = 5
    elif tipo_NC    == 'Importante':
        scale = 15
    elif tipo_NC    == 'Muy Seria':
        scale = 30
    attr_value={18:scale}               
    newfld.changeAttributeValues({id:attr_value})   #se actualiza valor en campo vacío   

vlayer.commitChanges()                              #se guarda cambio

Processing.initialize()
QgsApplication.processingRegistry().addProvider(QgsNativeAlgorithms())  #Se cargan procesos a pila

#Se especifican parámetros para el heatmap
pams = {'INPUT': tgt_lyr,
              'RADIUS':1000,
              'RADIUS_FIELD':'',
              'PIXEL_SIZE':50,
              'WEIGHT_FIELD':'NC_num',
              'KERNEL':0,
              'DECAY':-3,
              'OUTPUTVALUE': 1,
              'OUTPUT':outpt}                  
#Se ejecuta y guarda archivo
processing.run("qgis:heatmapkerneldensityestimation",pams)

###
newfld.deleteAttributes([18])       #se borra campo extra
vlayer.updateFields()
qgs.exitQgis()                      #Se quitan elementos de qgis de memoria