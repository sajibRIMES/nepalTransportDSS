import numpy as np

from bokeh.plotting import figure
from bokeh.tile_providers import get_provider, Vendors


from bokeh.embed import json_item


def lon_to_web_mercator(lon,k = 6378137):return lon * (k * np.pi / 180.0)
def lat_to_web_mercator(lat,k = 6378137):return np.log(np.tan((90 + lat) * np.pi / 360.0)) * k

def initializeFigure():
    bdLinWSG84=[87.50,93.50,20.50,26.75]
    x_range, y_range = (
        (lon_to_web_mercator(bdLinWSG84[0]), lon_to_web_mercator(bdLinWSG84[1])),
        (lat_to_web_mercator(bdLinWSG84[2]), lat_to_web_mercator(bdLinWSG84[3])))

    tile_provider = get_provider(Vendors.OSM)
    p = figure(
        x_range=x_range, y_range=y_range,x_axis_type="mercator", 
        y_axis_type="mercator",active_scroll = "wheel_zoom",
        width=500,height=500)
    p.toolbar_location = None
    p.add_tile('CARTODBPOSITRON')

    chart_item=json_item(p)

    return chart_item

