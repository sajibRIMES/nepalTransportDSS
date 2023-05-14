import geopandas as gpd
import xarray as xr
import rioxarray as rxr
import pandas as pd

import regionmask
import pymysql
from sqlalchemy import create_engine


def returnFolder(parameter):
    if parameter == 'tmax': folderName='Daily_Tmax'
    elif parameter=='tmin':folderName='Daily_tmin'
    elif parameter=='rr':folderName='Daily_Rainfall'

    return folderName

    
def computeCountryMean(parameter,yearStart,yearEnd):

    # Return Country Shape
        
    bdShapePath = "../bdShapefile/bangladesh-whole.shp"
    bdGeo = gpd.read_file(bdShapePath)

    bdGeo=bdGeo[['OBJECTID','admin0Name','geometry']]


    # Retuen Grid NC Mean
    folderName= returnFolder(parameter)

    ncPath=f'../enacts/{folderName}/{yearStart}-{yearEnd}_{parameter}.nc'
    dataset=xr.open_dataset(ncPath)
    dataVariable=list(dataset.data_vars)[0]

    dataArray=dataset[dataVariable]


    ## Crop Country Grid Mean
    countryMask= regionmask.mask_3D_geopandas(
            bdGeo,
            dataArray.Lon,
            dataArray.Lat,
            drop=True,
            numbers='OBJECTID'
        )

    countryDS = dataArray.where(countryMask)

    countryMonthlyMeanDS = countryDS.groupby("time.month").mean(dim=['time','Lat','Lon'])
    countryMeanDF=countryMonthlyMeanDS.to_dataframe()

    # countryMeanDF = countryMeanDF.reset_index()
    # countryMeanDF = countryMeanDF.drop(columns=['region'])
    # countryMeanDF= countryMeanDF.set_index("month")
    # countryMeanDF.index.name = 'month'

    print(countryMeanDF)


def computeRegionMean(parameter,yearStart,yearEnd):

    ## Database 
    engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}".format(host='127.0.0.1', db='bdClimatology', user="root", pw=""))

    # Return Region Shape

    zilaShapePath="../bdShapefile/district-1bd.shp"
    zilaGeo = gpd.read_file(zilaShapePath)
    zilaGeo=zilaGeo[['OBJECTID','admin2Name','geometry']].reset_index(drop=True)
    print(zilaGeo)

    # zilaGeo.to_sql('admin2boundary', engine, if_exists='replace',index=True)
    
    ##Save Region Details to SQL
    # regionDetails=zilaGeo[['OBJECTID','admin2Name','admin1Name']].copy(deep=True)
    # regionDetails.to_sql('regions', engine, if_exists='replace',index=True)

       # Retuen Grid NC Mean
    folderName= returnFolder(parameter)

    ncPath=f'../enacts/{folderName}/{yearStart}-{yearEnd}_{parameter}.nc'
    dataset=xr.open_dataset(ncPath)
    dataVariable=list(dataset.data_vars)[0]

    dataArray=dataset[dataVariable]


    # for index in range(0,64):

    #     thisZilla=zilaGeo.loc[[index]].reset_index(drop=True)
    #     print(thisZilla)

    #     zila_mask = regionmask.mask_3D_geopandas(
    #             thisZilla,
    #             dataArray.Lon,
    #             dataArray.Lat,
    #             drop=True,
    #             numbers='OBJECTID'
    #         )

    #     region_ds = dataArray.where(zila_mask)


    #     ## Computing Region Mean
    #     grouped_ds = region_ds.groupby("time.month").mean(dim=['time','Lat','Lon'])
    #     df=grouped_ds.to_dataframe()

    #     df = df.reset_index()
    #     df= df.set_index("month")
    #     df.index.name = 'month'
    #     tbaleName=f'table_{yearStart}-{yearEnd}_{parameter}'
    #     df.to_sql(f'{tbaleName}', engine, if_exists='append',index=True)
    #     print('Saved to SQL ')
    #     print(df)



parameter,yearStart,yearEnd='tmin',1981,2021
# computeCountryMean(parameter,yearStart,yearEnd)
computeRegionMean(parameter,yearStart,yearEnd)
