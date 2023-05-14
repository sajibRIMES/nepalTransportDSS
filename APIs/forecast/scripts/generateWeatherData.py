
import datetime
import pandas as pd

url = "https://flood-phl.rimes.int/Test/get_daily"

#function to return any day as based on passed integer value on the parameter forecast day
def returnForecastDate(day=0):
    
    forecastDate=datetime.date.today()+datetime.timedelta(days=day)
    forecastDate=forecastDate.strftime('%Y-%m-%d')
    # st.write(forecastDate)
    return forecastDate

def returnDailyWeather(forecastDate):

    tenDaysWeather=pd.read_json(url)
    dailyWeather=tenDaysWeather.where(tenDaysWeather.dt==f'{forecastDate}').dropna()
    dailyWeather=dailyWeather.astype({'district_id':'int32'})
    
    return dailyWeather.to_dict(orient="records"),tenDaysWeather

def returnDailyMaxMin(forecastDate):

    tenDaysWeather=pd.read_json(url)
    dailyWeather=tenDaysWeather.where(tenDaysWeather.dt==f'{forecastDate}').dropna()
    dailyWeather=dailyWeather.astype({'district_id':'int32'})

    maxPrecip=max(dailyWeather.precip.values)
    minPrecip=min(dailyWeather.precip.values)
    maxMinPrecip=[maxPrecip,minPrecip]

    maxTmax=max(dailyWeather.tmax.values)
    minTmax=min(dailyWeather.tmax.values)
    maxMinTmax=[maxTmax,minTmax]

    maxTmin=max(dailyWeather.tmin.values)
    minTmin=min(dailyWeather.tmin.values)
    maxMinTmin=[maxTmin,minTmin]

    maxRh=max(dailyWeather.rh.values)
    minRh=min(dailyWeather.rh.values)
    maxMinRh=[maxRh,minRh]


    maxWs=max(dailyWeather.ws.values)
    minWs=min(dailyWeather.ws.values)
    maxMinRh=[maxWs,minWs]

    maxMinList=[maxMinPrecip,maxMinTmax,maxMinTmin,maxMinRh,maxMinRh,forecastDate]

    return maxMinList

