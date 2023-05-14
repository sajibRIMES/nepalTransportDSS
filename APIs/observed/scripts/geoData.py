import folium
import geemap.foliumap as geemap
import geopandas as gpd



def returnRoadGeoDataframes():
    
    bdGeoRoads=gpd.read_file('/Volumes/dssDevelopment/djangular/APIs/observed/bdGeoJSON/bdRoads.geojson')
    # bdRoadsDF=pd.DataFrame(bdRoads[['objectid','rd_nr','start','end','length','class']].copy(deep=True))

    nationalGeoRoads=bdGeoRoads[
        ['objectid','rd_nr','start','end','length','class','geometry']].where(bdGeoRoads['class']=='National Highway').dropna()
    
    regionalGeoRoads=bdGeoRoads[
        ['objectid','rd_nr','start','end','length','class','geometry']].where(bdGeoRoads['class']=='Regional Highway').dropna()
    
    zillaGeoRoads=bdGeoRoads[
        ['objectid','rd_nr','start','end','length','class','geometry']].where(bdGeoRoads['class']=='Zilla Road').dropna()
    
    otherGeoRoads=bdGeoRoads[
        ['objectid','rd_nr','start','end','length','class','geometry']].where(bdGeoRoads['class']=='Other Agency Road').dropna()


    return bdGeoRoads,nationalGeoRoads,regionalGeoRoads,zillaGeoRoads,otherGeoRoads


def mapInitialize():
    
    figure = folium.Figure()
    # Map = geemap.Map(plugin_Draw = True, Draw_export = True)
    Map=geemap.Map(location=[23.8103, 90.4125],tiles='CartoDB Positron',add_google_map = False,zoom=7)
    

    Map.add_to(figure)

    return Map


