################ Heatmap raster from code ###########################
import sys
from qgis.core import (QgsApplication,QgsProject, QgsField,QgsVectorLayer,QgsPathResolver)
#from qgis.gui import QgsLayerTreeMapCanvasBridge
from qgis.analysis import QgsNativeAlgorithms
from PyQt5.QtCore import QVariant

#Global
#####################################################################
tgt_lyr = "../Q_Tests/SHP/total_meds2022.shp"
tgt_prj = "../Mediciones_ARESEP_QGIS/GIS_2022_Med.qgs"
procss = '/usr/share/qgis/python/plugins'           #Change accordingly (processing plugins)


#Code
#####################################################################
#Sets settings to standalone script
qgs = QgsApplication.setPrefixPath("/usr", True)
qgs = QgsApplication([], True)

#Initializes qgis background
qgs.initQgis()

sys.path.append(procss)

import processing           #requires prior route to work
from processing.core.Processing import Processing

##Load specified QGIS project from path
proj_tgt = QgsProject.instance()
proj_tgt.read(tgt_prj)

#Load desired layer
vlayer = QgsVectorLayer(tgt_lyr,"Meds_2022","ogr")

#print(vlayer.fields().names())
#Adds new virtual field to help with the heatmap
newfld = vlayer.dataProvider()
newfld.addAttributes([QgsField("NC_num",QVariant.Int)])
vlayer.updateFields()
vlayer.startEditing()

features = vlayer.getFeatures()
for f in features:
    scale = 0
    id=f.id()                                       #id from row
    tipo_NC = f.attributes()[17]                    #gets value from column 17
    if tipo_NC == 'Poca Importancia':
        scale = 5
    elif tipo_NC == 'Importante':
        scale = 15
    elif tipo_NC == 'Muy Seria':
        scale = 30
    attr_value={18:scale}
    newfld.changeAttributeValues({id:attr_value})   #updates value   

vlayer.commitChanges()                              #commits update (now value is not NULL)

Processing.initialize()
QgsApplication.processingRegistry().addProvider(QgsNativeAlgorithms())
outpt = '/home/gryphus/Estructuras_datos/Proyecto_QGIS/Q_Tests/RAST/test.tiff'
pams = {'INPUT': tgt_lyr,
              'RADIUS':1000,
              'RADIUS_FIELD':'',
              'PIXEL_SIZE':50,
              'WEIGHT_FIELD':'NC_num',
              'KERNEL':0,
              'DECAY':-3,
              'OUTPUTVALUE': 1,
              'OUTPUT':outpt}                  

processing.run("qgis:heatmapkerneldensityestimation",pams)
#For later
#{ 'DECAY' : -3, 'INPUT' : '/home/gryphus/Estructuras_datos/Proyecto_QGIS/Q_Tests/SHP/total_meds2018.shp', 'KERNEL' : 0, 'OUTPUT' : 'TEMPORARY_OUTPUT', 'OUTPUT_VALUE' : 1, 'PIXEL_SIZE' : 50, 'RADIUS' : 500, 'RADIUS_FIELD' : None, 'WEIGHT_FIELD' : None }

###
newfld.deleteAttributes([18])       #deletes extra field
vlayer.updateFields()
qgs.exitQgis()                      #Frees qgis data from memory

#
##Load specified QGIS project from path
#proj_tgt = QgsProject.instance()
#proj_tgt.read("../Mediciones_ARESEP_QGIS/GIS_2022_Med.qgs")
#
##
##Load desired layer
#vlayer = QgsVectorLayer(tgt_lyr,"Meds_2018_htmp","ogr")
#if not vlayer.isValid():    #Checks if layer exists and could be loaded
#    print("No se pudo accesar a objeto")
#
#else:                       #Else proceeds to create heatmap object
#   heatmap = QgsHeatmapRenderer()
#   heatmap.setRadius(50)
#   colorrmp = QgsStyle().defaultStyle().colorRamp('Inferno')
#   heatmap.setColorRamp(colorrmp)
#   vlayer.setRenderer(heatmap)
#   vlayer.triggerRepaint()
#   print("Almost ready")
#   proj_tgt.addMapLayer(vlayer)    #add final product to project