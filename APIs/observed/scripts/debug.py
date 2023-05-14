
import geopandas as gpd
import xarray as xr
import rioxarray as rxr
import pandas as pd

# def returnFolder(parameter):
#     if parameter == 'tmax': folderName='Daily_Tmax'
#     elif parameter=='tmin':folderName='Daily_tmin'
#     elif parameter=='rr':folderName='Daily_Rainfall'

#     return folderName

# def computeShapeMean(parameter,yearStart,yearEnd):

#     folderName= returnFolder(parameter)

#     ncPath=f'../enacts/{folderName}/{yearStart}-{yearEnd}_{parameter}.nc'
#     dataset=xr.open_dataset(ncPath)
#     dataVariable=list(dataset.data_vars)[0]

#     dataArray=dataset[dataVariable]

def shapeArea():

    bdShapePath = "../bdShapefile/bangladesh-whole.shp"
    bdGeo = gpd.read_file(bdShapePath)

    return bdGeo

bdGeo=shapeArea()