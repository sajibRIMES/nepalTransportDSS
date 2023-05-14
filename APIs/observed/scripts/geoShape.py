import geopandas as gpd

# bdGeo=returnShape()
# print(bdGeo.crs)

# import faulthandler
# faulthandler.enable()

import numpy as np
import xarray as xr
import rioxarray as rxr

import geopandas as gpd
# from geoShape import returnShape

from bokeh.plotting import figure
from bokeh.models import LinearColorMapper, ColorBar,HoverTool

from bokeh.embed import json_item

def lon_to_web_mercator(lon,k = 6378137):return lon * (k * np.pi / 180.0)
def lat_to_web_mercator(lat,k = 6378137):return np.log(np.tan((90 + lat) * np.pi / 360.0)) * k


def returnShape():

    bdShapePath = '/Volumes/dssDevelopment/djangular/APIs/observed/bdShapefile/bangladesh-whole.shp'
    bdGeo = gpd.read_file(bdShapePath)
    bdGeo['geometry'] = bdGeo['geometry'].to_crs(epsg=3857)
    
    return bdGeo


def generateGeotiff():

    # ncPath='../enacts/Daily_Tmax/2018-2021_tmax.nc'
    ncPath='../enacts/Daily_Tmax/1981-2021_tmax.nc'

    dataset=xr.open_dataset(ncPath)
    # print(dataset.data_vars)
    dataArray=dataset['temp']
    dataArray.rio.write_crs(4326, inplace=True)

    meanAnnualTemp=dataArray.mean(dim='time')
    meanAnnualTemp_Reversed=meanAnnualTemp.reindex(Lat=list(reversed(meanAnnualTemp.Lat)))
    meanAnnualTemp_Reversed.rio.to_raster('../enacts/Daily_Tmax//meanAnnualTemp.tif')


# def initializeFigure():
#     bdLinWSG84=[87.50,93.50,20.50,26.75]
#     x_range, y_range = (
#         (lon_to_web_mercator(bdLinWSG84[0]), lon_to_web_mercator(bdLinWSG84[1])),
#         (lat_to_web_mercator(bdLinWSG84[2]), lat_to_web_mercator(bdLinWSG84[3])))

#     p = figure(
#         x_range=x_range, y_range=y_range,x_axis_type="mercator", 
#         y_axis_type="mercator",active_scroll = "wheel_zoom",
#         width=500,height=500)
#     p.toolbar_location = None
#     p.add_tile('CARTODBPOSITRON')

#     # chart_item=json_item(p)
#     # return chart_item
#     return p


# generateGeotiff()

# def addClimateArray(tiffPath):

#     # dataarray_mercator = xr.open_dataset(tiffPath, engine="rasterio")
#     dataarray_mercator = rxr.open_rasterio(tiffPath).rio.reproject('EPSG:3857')

#     xValues=dataarray_mercator.x.values
#     yValues=dataarray_mercator.y.values

#     xMin,xMax=xValues.min(),xValues.max()
#     yMin,yMax=yValues.min(),yValues.max()

#     dataValues=dataarray_mercator.values[0,:,:]


#     print(dataarray_mercator.crs)
#     return dataValues,xMin,xMax,yMin,yMax


# def produceClimateFigure(p):

#     tiffPath='/Volumes/dssDevelopment/djangular/APIs/observed/enacts/Daily_Tmax/meanAnnualTemp.tif'
#     dataValues,xMin,xMax,yMin,yMax=addClimateArray(tiffPath)


#     maxValue,minValue=np.nanmax(dataValues),np.nanmin(dataValues)

#     color = LinearColorMapper(palette = "Spectral11",low = minValue-1 , high =maxValue+1 )

#     p.title='Projected Climatology of Mean-Temperature'
#     tas_renderer = p.image(
#         image = [np.flipud(dataValues)],x=xMin,y=yMin,dw=xMax-xMin,dh=yMax-yMin,color_mapper = color)
               
#     tas_tool = HoverTool(tooltips=[(
#         'Mean-Temperature', '@image{0.00} °C')],
#         point_policy = 'follow_mouse',attachment='right',show_arrow=False,renderers=[tas_renderer])

#     p.add_tools(tas_tool)

#     color_bar = ColorBar(title = 'TEMPERATURE (°C)',color_mapper = color, location = (0,0))
#     p.add_layout(color_bar, 'right')

#     chart_item=json_item(p)
#     return chart_item


# def main():
#     bdShapePath = '/Volumes/dssDevelopment/djangular/APIs/observed/bdShapefile/bangladesh-whole.shp'
#     bdGeo = gpd.read_file(bdShapePath)
#     # p=initializeFigure()
#     # chart_item=produceClimateFigure(p)
#     # return chart_item


# if __name__=='__main__':
#     main()
