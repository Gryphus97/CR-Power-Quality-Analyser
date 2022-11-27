############### SHP file generation from code ###########################

#Imports n' modules
import pandas as pf
import fiona as gl
from pyproj import Transformer
########################################################

#Global
coords_src = '../Test1.xlsx'                    #Cambiar a servidor, por mientras es local
coords_dest= '../Q_Tests/SHP/' 
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

    return df

def Shp_generator(utility,year,df):
    schema = {
        'geometry':'Point',
        'properties':['Fecha']
    }
    ptShp = gl.open(coords_dest+utility+"_meds"+year+".shp",mode='w',driver='ESRI Shapefile',schema = schema, crs = "EPSG:5367")

#Main
#########################################################

coords = pf.read_excel(coords_src,index_col=0)    
coords=Coord_extract_n_transf(coords)    #A este punto ya se tienen las coordenadas separadas
print(coords.iloc[:,[7,8,9,10]])

#All records
#new_shp = gl.open(,)

