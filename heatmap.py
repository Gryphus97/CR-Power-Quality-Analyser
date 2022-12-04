################ Heatmap raster from code ###########################
from qgis.core import *
#import pandas as pf
#from Fiona import *



qgs = QgsApplication.setPrefixPath("/usr", True)
qgs = QgsApplication([], True)

qgs.initQgis()

qgs.exitQgis()


#import pandas as pd
#from datashader.tiles import render_tiles
#import geopandas as gpd
#import datashader as ds, pandas as pd, colorcet
#import datashader.transfer_functions as tf
#from PIL import ImageDraw
#
#
#def read_uk_accidents():
#    # Read UK Accidents Point csvs
#    uk_accidents_1 = pd.read_csv('csvs/uk_accidents_2005_to_2007.tar.xz', low_memory=False)
#    uk_accidents_2 = pd.read_csv('csvs/uk_accidents_2009_to_2011.tar.xz', low_memory=False)
#    uk_accidents_3 = pd.read_csv('csvs/uk_accidents_2012_to_2014.tar.xz', low_memory=False)
#
#    uk_accidents = pd.concat([uk_accidents_1, uk_accidents_2, uk_accidents_3])
#
#    # Convert Long Lat into numeric type
#    uk_accidents['Longitude'] = pd.to_numeric(uk_accidents['Longitude'])
#    uk_accidents['Latitude'] = pd.to_numeric(uk_accidents['Latitude'])
#
#    # Convert Long Lat into Point Geometry
#    uk_accidents = gpd.GeoDataFrame(geometry = gpd.points_from_xy(x=uk_accidents['Longitude'], y=uk_accidents['Latitude']))
#    uk_accidents = uk_accidents.set_crs('EPSG:4326')
#
#    # Reprojecting to 3857 coordinate system
#    uk_accidents = uk_accidents.to_crs('EPSG:3857')
#    uk_accidents['value'] = 1
#    uk_accidents = uk_accidents[uk_accidents.is_valid]
#    uk_accidents = uk_accidents[~uk_accidents.is_empty]
#
#    # Get x, y coordinates
#    uk_accidents['x'] = uk_accidents.geometry.x
#    uk_accidents['y'] = uk_accidents.geometry.y
#
#    df = uk_accidents[['x', 'y']]
#
#    return [df, tuple(uk_accidents.total_bounds)]
#
#def load_data_func(x_range, y_range):
#        global df
#        return df
#
#def rasterize_func(df, x_range, y_range, height, width):
#    # aggregate
#    cvs = ds.Canvas(x_range=x_range, y_range=y_range, plot_height=height, plot_width=width)
#    agg = cvs.points(df, 'x', 'y')
#    return agg
#
#
#def shader_func(agg, span=None):
#    # shader func
#    img = tf.shade(agg, cmap=colorcet.fire, how='log')
#    img = tf.spread(img, px=1, shape='circle', how='add', mask=None, name=None)        
#    img = tf.set_background(img, None)
#    return img
#
#
#
#def post_render_func(img, **kwargs):
#    # Create tiles
#    draw = ImageDraw.Draw(img)
#    draw.text((5, 5), '', fill='rgb(255, 255, 255)')
#    return img
#
#
#
#if __name__ == "__main__":
#    global df
#    
#    df, map_extent = read_uk_accidents()
#
#    render_tiles(map_extent,
#    levels=range(11),
#    output_path='tiles',
#    load_data_func=load_data_func,
#    rasterize_func=rasterize_func,
#    shader_func=shader_func,
#    post_render_func=post_render_func)