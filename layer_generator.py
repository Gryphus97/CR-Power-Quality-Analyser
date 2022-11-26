############### SHP file generation from code ###########################

#Imports n' modules
import pandas as pf
############################

#Global
coords_addr = '../Test1.xlsx'          #Cambiar a servidor, por mientras es local
#############################

#Methods
#############################
def Coord_extract(df):
    df.insert(8,"Coordenada_X",None,False)
    df = df.rename(columns={"Coordenadas":"Coordenada_Y"})
    #df.at['M-0001-2018','Coordenada_Y']
    index = df.index.tolist()

    for i in range(len(df.index)):
        aux=df.at[index[i],'Coordenada_Y'].split(" ")
        df.at[index[i],'Coordenada_X'] = "-"+aux[0][1:]
        df.at[index[i],'Coordenada_Y'] = aux[1][1:]

    return df


#Main
#############################

coords = pf.read_excel(coords_addr,index_col=0)    

coords=Coord_extract(coords)    #A este punto ya se tienen las coordenadas separadas
print(coords.iloc[:,[0,7,8]])

