import os
import sys
from functools import partial

import numpy as np
import netCDF4
import rioxarray 
import xarray as xr


def _preprocess(x, lat_bnds,lon_bnds):return x.sel(Lat=slice(*lat_bnds),Lon=slice(*lon_bnds))

def readMultipleNC(ncPath,min_lat = 20,max_lat = 27,min_lon = 87,max_lon = 94):

    lat_bnds,lon_bnds = (min_lat, max_lat),(min_lon, max_lon)

    partial_func = partial(_preprocess, lon_bnds=lon_bnds, lat_bnds=lat_bnds)
    dataset = xr.open_mfdataset(ncPath, concat_dim="time", combine='nested',preprocess=partial_func)

    return dataset


def generateGeotiff(parameter,yearStart,yearEnd,folderName):

    # ncPath='../enacts/Daily_Tmax/2018-2021_tmax.nc'
    ncPath=f'../enacts/{folderName}/{yearStart}-{yearEnd}_{parameter}.nc'

    dataset=xr.open_dataset(ncPath)
    dataVariable=list(dataset.data_vars)[0]

    dataArray=dataset[dataVariable]
    dataArray.rio.write_crs(4326, inplace=True)

    meanAnnual=dataArray.mean(dim='time')
    meanAnnual_Reversed=meanAnnual.reindex(Lat=list(reversed(meanAnnual.Lat)))
    meanAnnual_Reversed.rio.to_raster(f'../enacts/{folderName}//{yearStart}-{yearEnd}_{parameter}_mean.tif')


def returnFolder(parameter):
    if parameter == 'tmax': folderName='Daily_Tmax'
    elif parameter=='tmin':folderName='Daily_tmin'
    elif parameter=='rr':folderName='Daily_Rainfall'

    return folderName
# print(dataset.coords)

def main(parameter,yearStart,yearEnd):

    folderName=returnFolder(parameter)

    #reading multiple NC and merging them
    ncPath=f'../enacts/{folderName}/merge_{parameter}_*.nc'
    dataset=readMultipleNC(ncPath)

    #saving merged NC file
    ncFileName=f"../enacts/{folderName}/{yearStart}-{yearEnd}_{parameter}.nc"
    print ('Saving to .... ', ncFileName)
    dataset.to_netcdf(path=ncFileName)

    print('Generating TiFF File ... ')
    generateGeotiff(parameter,yearStart,yearEnd,folderName)

if __name__=='__main__':
    # main(parameter='tmax',yearStart=2011,yearEnd=2021)
    # main(parameter='tmin',yearStart=2011,yearEnd=2021)
    main(parameter='rr',yearStart=1981,yearEnd=2011)
