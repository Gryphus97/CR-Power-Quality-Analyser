############### SHP file generation from code ###########################

#Imports n' modules
import pandas as pf
import fiona as gl
from pyproj import Transformer
########################################################

#Global
coords_src = '../test22.xlsx'                    #Input
coords_dest= '../Q_Tests/SHP/'                   #Output
#########################################################

#Methods
#########################################################
def Coord_extract_n_transf(df):    
    transf = Transformer.from_crs("EPSG:4326","EPSG:5367",always_xy=True) #WGS84 to CRTM05

    df.insert(8,"Longitud",None,False)
    df.insert(9,"Coordenada_Y",None,False)
    df.insert(10,"Coordenada_X",None,False)
    df = df.rename(columns={"Coordenadas":"Latitud"})
    index = df.index.tolist()

    for i in range(len(df.index)):
        aux=df.at[index[i],'Latitud'].split(" ")
        lon = "-"+aux[1][1:]
        lat = aux[0][1:]
        df.at[index[i],'Longitud'] = lon
        df.at[index[i],'Latitud'] = lat
        df.at[index[i],'Coordenada_X'],df.at[index[i],'Coordenada_Y'] = transf.transform(lon,lat)
        df.at[index[i],'Fecha de instalación'] = str(df.at[index[i],'Fecha de instalación'])+' '+str(df.at[index[i],'Hora instalación'])+":00"
        df.at[index[i],'Fecha de desinstalación'] = str(df.at[index[i],'Fecha de desinstalación'])+' '+str(df.at[index[i],'Hora desinstalación'])+":00"
    
    df.drop(columns=['Hora instalación','Hora desinstalación','Observaciones'],inplace=True)    

    return df

def Shp_generator(utility,year,df):
    schema = {
        'geometry':'Point',
        'properties':[('Consecutivo','str'),
                      ('Fecha de instalación','str'),
                      ('Fecha de desinstalación','str'), 
                      ('N de equipo','str'),
                      ('Medidor','str'),
                      ('Empresa Distribuidora','str'),
                      ('Latitud','float'),
                      ('Longitud','float'),
                      ('Coordenada_Y','float'), 
                      ('Coordenada_X','float'),
                      ('Provincia','str'),
                      ('Cantón','str'),
                      ('Distrito','str'),
                      ('Servicio Eléctrico','str'),
                      ('Conformidad Medición','str'),
                      ('Conformidad Artículo 6','str'),
                      ('Conformidad Artículo 10','str'),
                      ('Tipo NC Artículo 10','str')]
    }
    ptShp = gl.open(coords_dest+utility+"_meds"+year+".shp",mode='w',driver='ESRI Shapefile',schema = schema, crs = "EPSG:5367",encoding='utf-8')
    
    for index, row in df.iterrows():
     #   print(index)
        medrow = {
            'geometry':{'type':'Point',
                        'coordinates':(row['Coordenada_X'],row['Coordenada_Y'])},
            'properties': {'Consecutivo':index,
                          'Fecha de instalación':row['Fecha de instalación'],
                          'Fecha de desinstalación':row['Fecha de desinstalación'], 
                          'N de equipo':row['N° de equipo'],
                          'Medidor':row['Medidor'],
                          'Empresa Distribuidora':row['Empresa Distribuidora'],
                          'Latitud':row['Latitud'],
                          'Longitud':row['Longitud'],
                          'Coordenada_Y':row['Coordenada_Y'], 
                          'Coordenada_X':row['Coordenada_X'],
                          'Provincia':row['Provincia'],
                          'Cantón':row['Cantón'],
                          'Distrito':row['Distrito'],
                          'Servicio Eléctrico':row['Servicio Eléctrico'],
                          'Conformidad Medición':row['Conformidad Medición'],
                          'Conformidad Artículo 6':row['Conformidad Artículo 6'],
                          'Conformidad Artículo 10':row['Conformidad Artículo 10'],
                          'Tipo NC Artículo 10':row['Tipo NC Artículo 10']}
        }
        ptShp.write(medrow)
    ptShp.close()
#Main
#########################################################

coords = pf.read_excel(coords_src,index_col=0)    
coords=Coord_extract_n_transf(coords)    #A este punto ya se tienen las coordenadas separadas

#All records
Shp_generator('total','2022',coords)

