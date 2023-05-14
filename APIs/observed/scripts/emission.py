import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly
import plotly.figure_factory as ff
import numpy as np

import os.path
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

px.set_mapbox_access_token(open(f"{PROJECT_ROOT}/.mapbox_token").read())
np.random.seed(0)

# Generate Lan Cover Figure
def returnDistrictLanCover(thisDistrict):

    landcoverDF=pd.read_json(f'{PROJECT_ROOT}/bd_LandCover.json')

    filter = landcoverDF["Dist_name"]==thisDistrict
    thisDistrictLandcover=landcoverDF.where(filter).dropna()

    x=list(thisDistrictLandcover.columns)[1:]
    y=list(thisDistrictLandcover.iloc[0].values)[1:]

    fig = go.Figure(data=[go.Bar(
            x=x, y=y,
            text=y,
            textposition='auto',

        )])

    fig.update_layout(
    title={
        'text': f"Land Cover: {thisDistrict}",
        'y':0.99,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},

    autosize=True,
    width=600,
    height=590,
    margin=dict(
        l=60,
        r=0,
        b=0,
        t=5,
        pad=0
    ),
    font=dict(
        family="Courier New, monospace",
        size=12,
        color="RebeccaPurple"
    ),
    paper_bgcolor="LightSteelBlue",
    )

    jsonFig=plotly.io.to_json(fig, validate=True, pretty=False, remove_uids=True, engine=None)

    return jsonFig

# Generate yearly FMD Figure
def returnDistrictFMD(thisDistrict):

    landcoverDF=pd.read_json(f'{PROJECT_ROOT}/yearly_fmd.json')

    filter = landcoverDF["Dist_name"]==thisDistrict
    thisDistrictLandcover=landcoverDF.where(filter).dropna()

    x=list(thisDistrictLandcover.columns)[1:]
    y=list(thisDistrictLandcover.iloc[0].values)[1:]

    fig = go.Figure(data=[go.Bar(
            x=x, y=y,
            text=y,
            textposition='auto',

        )])

    fig.update_layout(
    title={
        'text': f"FMD Incidence: {thisDistrict}",
        'y':0.99,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},

    autosize=True,
    width=600,
    height=590,
    margin=dict(
        l=60,
        r=0,
        b=0,
        t=5,
        pad=0
    ),
    font=dict(
        family="Courier New, monospace",
        size=12,
        color="RebeccaPurple"
    ),
    paper_bgcolor="LightSteelBlue",
    )

    jsonFig=plotly.io.to_json(fig, validate=True, pretty=False, remove_uids=True, engine=None)

    return jsonFig

# Return Livestock Population
def returnLivestockPopulation(thisDistrict):

    populationDF=pd.read_json(f'{PROJECT_ROOT}/livestockPopulation.json')

    districtWisePopulation=populationDF[populationDF['district.1']==f'{thisDistrict}']

    districtWisePopulation.drop(columns=['district','upazila'],inplace=True)
    # districtWisePopulation=districtWisePopulation.where(districtWisePopulation.year==2020)
    districtWisePopulation.dropna(inplace=True)
    df=districtWisePopulation[['year','cattle','buffalo','goat','sheep','chicken','duck']]
    df.reset_index(drop=True)

    fig = px.bar(df, x="year", y=['cattle','buffalo','goat','sheep','chicken','duck'],barmode="group")

    fig.update_layout(
    title={
        'text': f"Livestock Population: {thisDistrict}",
        'y':0.99,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},

    autosize=True,
    width=600,
    height=590,
    margin=dict(
        l=60,
        r=0,
        b=0,
        t=5,
        pad=0
    ),
    font=dict(
        family="Courier New, monospace",
        size=12,
        color="RebeccaPurple"
    ),
    paper_bgcolor="LightSteelBlue",
    )

    jsonFig=plotly.io.to_json(fig, validate=True, pretty=False, remove_uids=True, engine=None)

    return jsonFig

# Return CWD Risk Indices
def returnDistrictCWD(thisDistrict):

    df=pd.read_json(f'{PROJECT_ROOT}/districts_cwd.json')

    df.reset_index(inplace=True)
    df.rename(columns={'index':'Districts'},inplace=True)

    df=df[df['Districts']==f'{thisDistrict}']

    x=df.columns.to_list()[1:]
    y=list(df.iloc[0][1:].values)

    fig = px.line(x=x,y=y,markers=True)

    fig.update_layout(
    title={
        'text': f"Semi-Decadal CWD: {thisDistrict}",
        'y':0.99,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},

    autosize=True,
    width=600,
    height=590,
    margin=dict(
        l=60,
        r=0,
        b=0,
        t=5,
        pad=0
    ),
    font=dict(
        family="Courier New, monospace",
        size=12,
        color="RebeccaPurple"
    ),
    paper_bgcolor="LightSteelBlue",
    )

    jsonFig=plotly.io.to_json(fig, validate=True, pretty=False, remove_uids=True, engine=None)

    return jsonFig

def returnCorrelationDF(thisParameter):

    columns=[]
    print(type(thisParameter))

    if (thisParameter=='landcover'):

        landcoverDF=pd.read_json(f'{PROJECT_ROOT}/bd_LandCover.json')
        columns=landcoverDF.columns.to_list()

    return columns

def returnEmissionJson(thisEmission):
    
    
    # print(PROJECT_ROOT)

    emissionDF=pd.read_csv(f'{PROJECT_ROOT}/BD_Emission_Gleam_All.csv')
    emissionDF=emissionDF[['Dist_name','bfl_meat_em', 'bfl_milk_em','_buffelo_em', 'n_cattle_em', '_chicken_em', '_ckn_egg_em',
        'ckn_meat_em', 'ctl_meat_em', 'ctl_milk_em', 'ion_goat_em','on_sheep_em', 'on_total_em']]
    
    emissionTreeFig=px.treemap(emissionDF,color=f'{thisEmission}',path=['Dist_name'],height=500)
    emissionTreeFig.update_layout(
        margin=dict(l=0, r=0, t=0, b=0),
        )
    emissionJson=plotly.io.to_json(emissionTreeFig, validate=True, pretty=False, remove_uids=True, engine=None)

    return emissionJson

def returnDistrictEmission(thisDistrict):

    emissionDF=pd.read_csv(f'{PROJECT_ROOT}/BD_Emission_Gleam_All.csv')
    emissionDF=emissionDF[['Dist_name','bfl_meat_em', 'bfl_milk_em','_buffelo_em', 'n_cattle_em', '_chicken_em', '_ckn_egg_em',
        'ckn_meat_em', 'ctl_meat_em', 'ctl_milk_em', 'ion_goat_em','on_sheep_em', 'on_total_em']]

    filter = emissionDF["Dist_name"]==thisDistrict

    thisDistrictEmission=emissionDF.where(filter).dropna()

    x=list(thisDistrictEmission.columns)[1:]
    y=list(thisDistrictEmission.iloc[0].values)[1:]

    fig = go.Figure(data=[go.Bar(
            x=x, y=y,
            text=y,
            textposition='auto',
            
        )])

    fig.update_layout(
    title={
        'text': f"District Name: {thisDistrict}",
        'y':0.9,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
        
    autosize=True,
    width=1100,
    height=700,
    margin=dict(
        l=200,
        r=10,
        b=200,
        t=50,
        pad=50
    ),
    font=dict(
        family="Courier New, monospace",
        size=18,
        color="RebeccaPurple"
    ),
    paper_bgcolor="LightSteelBlue",
)
    
    jsonFig=plotly.io.to_json(fig, validate=True, pretty=False, remove_uids=True, engine=None)

    return jsonFig

def returnPlotly():
    # df = px.data.gapminder().query("year==2007")
    # fig = px.scatter_geo(df, locations="iso_alpha", color="continent",
    #                     hover_name="country", size="pop",
    #                     projection="natural earth")


    N = 500
    n_frames = 12
    lat = np.concatenate([
        np.random.randn(N) * 0.5 + np.cos(i / n_frames * 2 * np.pi) + 10
        for i in range(n_frames)
    ])
    lon = np.concatenate([
        np.random.randn(N) * 0.5 + np.sin(i / n_frames * 2 * np.pi)
        for i in range(n_frames)
    ])
    frame = np.concatenate([
        np.ones(N, int) * i for i in range(n_frames)
    ])

    fig = ff.create_hexbin_mapbox(
        lat=lat, lon=lon, nx_hexagon=15, animation_frame=frame,
        color_continuous_scale="Cividis", labels={"color": "Point Count", "frame": "Period"},
        opacity=0.5, min_count=1,
        show_original_data=True, original_data_marker=dict(opacity=0.6, size=4, color="deeppink")
    )
    fig.update_layout(margin=dict(b=0, t=0, l=0, r=0))
    fig.layout.sliders[0].pad.t=20
    fig.layout.updatemenus[0].pad.t=40

    jsonFig=plotly.io.to_json(fig, validate=True, pretty=False, remove_uids=True, engine=None)

    return jsonFig


# emissionJson=returnEmissionJson(thisEmission)
# print(emissionJson)