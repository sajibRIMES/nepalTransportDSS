import pandas as pd
import geopandas as gpd

from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, save,show
from bokeh.io import push_notebook,show,output_notebook

from bokeh.models import HoverTool, LogColorMapper, LinearColorMapper, ColorBar
from bokeh.palettes import Greys256, Inferno256, Magma256, Plasma256,Bokeh3
from bokeh.palettes import Viridis256, Cividis256, Turbo256,Spectral11,YlGnBu9,PuBu9,GnBu9


from bokeh.embed import json_item

def returnGeoDataFrame():
    df = gpd.read_file('/Volumes/dssDevelopment/djangular/APIs/observed/worldCover/BD_District_WorldCover.shp')
    gdf = df.to_crs(4326)

    gdf=gdf.astype({'VALUE_10':'int64','VALUE_20':'int64','VALUE_30':'int64','VALUE_40':'int64',
            'VALUE_50':'int64','VALUE_60':'int64','VALUE_80':'int64',
            'VALUE_90':'int64','VALUE_95':'int64'})

    return gdf

def getGeometryCoords(row, geom, coord_type, shape_type):
    """
    Returns the coordinates ('x' or 'y') of edges of a Polygon exterior.
    
    :param: (GeoPandas Series) row : The row of each of the GeoPandas DataFrame.
    :param: (str) geom : The column name.
    :param: (str) coord_type : Whether it's 'x' or 'y' coordinate.
    :param: (str) shape_type
    """
    
    # Parse the exterior of the coordinate
    if shape_type == 'polygon':
        if row[geom].geom_type=='MultiPolygon': 
            exterior = row[geom].geoms[0].exterior
        elif row[geom].geom_type=='Polygon':
            exterior = row[geom].exterior
        if coord_type == 'x':
            # Get the x coordinates of the exterior
            return list( exterior.coords.xy[0] )    
        
        elif coord_type == 'y':
            # Get the y coordinates of the exterior
            return list( exterior.coords.xy[1] )

def convert_GeoPandas_to_Bokeh_format(gdf):
    """
    Function to convert a GeoPandas GeoDataFrame to a Bokeh
    ColumnDataSource object.
    
    :param: (GeoDataFrame) gdf: GeoPandas GeoDataFrame with polygon(s) under
                                the column name 'geometry.'
                                
    :return: ColumnDataSource for Bokeh.
    """
    gdf_new = gdf.drop('geometry', axis=1).copy(deep=True)
    gdf_new['x'] = gdf.apply(getGeometryCoords, 
                             geom='geometry', 
                             coord_type='x', 
                             shape_type='polygon', 
                             axis=1)
    
    gdf_new['y'] = gdf.apply(getGeometryCoords, 
                             geom='geometry', 
                             coord_type='y', 
                             shape_type='polygon', 
                             axis=1)
    
    return gdf_new,ColumnDataSource(gdf_new)



def produceMap(gdf_new,geoSource,variable,variableClass):


    p = figure(title="Bangladesh")

    minValue=min(gdf_new[variable])
    maxValue=max(gdf_new[variable])

    color = LinearColorMapper(palette = "Spectral11",low = minValue-1 , high =maxValue+1 )
    color_mapper = LogColorMapper(palette="Spectral11")

    # p.patches('x', 'y', source=geoSource,line_color="black", line_width=1.5)

    p.patches('x', 'y', source=geoSource,fill_color = {'field': f'{variable}','transform': color_mapper},
    #          fill_color={'field': 'VALUE_10', 'transform': color_mapper},
            fill_alpha=1.0, line_color="black", line_width=1.5)



    color_bar = ColorBar(title = 'Values',color_mapper = color, location = (0,0))
    p.add_layout(color_bar, 'right')

    tooltip = HoverTool()
    tooltip.tooltips = [
        (f'{variableClass}', f'@{variable}'),
        ('District','@Dist_name'),
        ('Shape Area','@Shape_Area')
    ]
    p.add_tools(tooltip)


    chart_item=json_item(p)

    return chart_item


def worldCoverFigure():

    gdf=returnGeoDataFrame()
    gdf_new,geoSource = convert_GeoPandas_to_Bokeh_format(gdf)

    class_dict={
        'VALUE_10':'Tree Cover',
        'VALUE_20':'Shrubland',
        'VALUE_30':'Grassland',
        'VALUE_40':'Cropland',
        'VALUE_50':'Built-up',
        'VALUE_60':'Sparse Vegetation',
        'VALUE_80':'Permanent Water Bodies',
        'VALUE_90':'Herbaceous Wetland',
        'VALUE_95':'Mangroves',
        
    }

    variable='VALUE_30'
    variableClass=class_dict[variable]

    chart_item=produceMap(gdf_new,geoSource,variable,variableClass)

    return chart_item



