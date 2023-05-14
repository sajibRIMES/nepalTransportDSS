import geopandas as gpd
from shapely.geometry import mapping

import numpy as np
import xarray as xr
import rioxarray as rxr

import geopandas as gpd
# from geoShape import returnShape

from bokeh.plotting import figure
from bokeh.models import LinearColorMapper, ColorBar,HoverTool
from bokeh.colors import RGB

from bokeh.embed import json_item


def lon_to_web_mercator(lon,k = 6378137):return lon * (k * np.pi / 180.0)
def lat_to_web_mercator(lat,k = 6378137):return np.log(np.tan((90 + lat) * np.pi / 360.0)) * k

def initializeFigure():
    bdLinWSG84=[87.50,93.50,20.50,26.75]
    x_range, y_range = (
        (lon_to_web_mercator(bdLinWSG84[0]), lon_to_web_mercator(bdLinWSG84[1])),
        (lat_to_web_mercator(bdLinWSG84[2]), lat_to_web_mercator(bdLinWSG84[3])))

    p = figure(
        x_range=x_range, y_range=y_range,x_axis_type="mercator", 
        y_axis_type="mercator",active_scroll = "wheel_zoom",
        width=500,height=500)
    p.toolbar_location = None
    # p.add_tile('CARTODBPOSITRON')

    # chart_item=json_item(p)
    # return chart_item
    return p

def addClimateArray(tiffPath):

    # dataarray_mercator = xr.open_dataset(tiffPath, engine="rasterio")
    dataarray_mercator = rxr.open_rasterio(tiffPath).rio.reproject('EPSG:3857')
    # print(dataarray_mercator.rio.crs)

    xValues=dataarray_mercator.x.values
    yValues=dataarray_mercator.y.values

    xMin,xMax=xValues.min(),xValues.max()
    yMin,yMax=yValues.min(),yValues.max()
    
    dataValues=dataarray_mercator.values[0,:,:]


   
    return dataarray_mercator,dataValues,xMin,xMax,yMin,yMax

def returnFolder(parameter):
    if parameter == 'tmax': folderName='Daily_Tmax'
    elif parameter=='tmin':folderName='Daily_tmin'
    elif parameter=='rr':folderName='Daily_Rainfall'

    return folderName

def produceClimateFigure(p,parameter,yearStart,yearEnd):

    folderName=returnFolder(parameter)
    tiffPath=f'/Volumes/dssDevelopment/djangular/APIs/observed/enacts/{folderName}/{yearStart}-{yearEnd}_{parameter}_mean.tif'

    # tiffPath='/Volumes/dssDevelopment/djangular/APIs/observed/enacts/Daily_Tmax/meanAnnualTemp.tif'
    # tiffPath='/Volumes/dssDevelopment/djangular/APIs/observed/enacts/Daily_Tmax/meanAnnualTempShaped.tif'

    dataarray_mercator,dataValues,xMin,xMax,yMin,yMax=addClimateArray(tiffPath)
    # print(dataarray_mercator.rio.crs)


    maxValue,minValue=np.nanmax(dataValues),np.nanmin(dataValues)

    color = LinearColorMapper(palette = "Spectral11",low = minValue-1 , high =maxValue+1 )

    p.title=f'Observed Climatology of Mean-{parameter}'
    tas_renderer = p.image(
        image = [np.flipud(dataValues)],x=xMin,y=yMin,dw=xMax-xMin,dh=yMax-yMin,
        color_mapper = color)
    
    #Making outshide shape (NaN) value transparent
    tas_renderer.glyph.color_mapper.nan_color = (0, 0, 0, 0)
               
    tas_tool = HoverTool(tooltips=[(
        f'Mean-{parameter}', '@image{0.00} °C')],
        point_policy = 'follow_mouse',attachment='right',show_arrow=False,renderers=[tas_renderer])

    p.add_tools(tas_tool)

    if parameter !='rr':
        color_bar = ColorBar(title = f'TEMPERATURE (°C)',color_mapper = color, location = (0,0))
    elif parameter =='rr':
         color_bar = ColorBar(title = f'RAINFALL (mm)',color_mapper = color, location = (0,0))
    
    p.add_layout(color_bar, 'right')

    chart_item=json_item(p)
    return chart_item




def returnEnacts():

    p=initializeFigure()
    parameter,yearStart,yearEnd='tmax',1981,2021
    chart_item=produceClimateFigure(p,parameter,yearStart,yearEnd)
    # cropExtent()
    return chart_item

# if __name__=='__main__':main()