from django.core.management import BaseCommand, CommandError
from django.conf import settings

import sys,os
from numpy import datetime_as_string
import pandas as pd
from datetime import date, datetime, timedelta
from sqlalchemy import create_engine
import pymysql
import logging
import sshtunnel
from sshtunnel import SSHTunnelForwarder

ssh_host = '114.31.28.234'
ssh_username = 'rimes'
ssh_password = 'inflamedwarrior666'
# database_name = 'bias_database'
database_name = 'bmd_observe_data'
localhost = '127.0.0.1'


class stationObserved():

    def __init__(self):

        updateDate=datetime.today()-timedelta(days=1)
        dateInput=datetime.strftime(updateDate,'%Y-%m-%d')
        print(f'Updating Station Observed for the Date : {dateInput}')
        self.dateInput=dateInput

        # self.dateInput=sys.argv[1]


    # help='Update Station  Observed Regularly'

    # def add_arguments(self,parser):
    #     parser.add_argument('date',type=str, help='date for updating station observed')

    # def handle(self, *args, **kwargs):

    #     dateInput = kwargs['date']

        # updateDate=datetime.today()-timedelta(days=1)
        # dateInput=datetime.strftime(updateDate,'%Y-%m-%d')
        # print(dateInput)

        # self.main(dateInput)

    def open_ssh_tunnel(self,verbose=False):
    
        if verbose:
            sshtunnel.DEFAULT_LOGLEVEL = logging.DEBUG
    
        global tunnel
        tunnel = SSHTunnelForwarder(
            (ssh_host, 22),
            ssh_username = ssh_username,
            ssh_password = ssh_password,
            remote_bind_address = ('127.0.0.1', 3306)
        )
        
        tunnel.start()

    def mysql_connect(self):

        global connection
        
        connection = pymysql.connect(
            host='127.0.0.1',
            user="rimes",
            passwd="rimesr230@#$%",
            db=database_name,
            port=tunnel.local_bind_port
        )

        # connection = pymysql.connect(
        #     host='127.0.0.1',
        #     user="root",
        #     passwd="",
        #     db=database_name,
        #     port=3306
        # )

    def mysql_disconnect(self):
        connection.close()

    def close_ssh_tunnel(self):
        tunnel.close

    def openTunnel(self):
        
        self.open_ssh_tunnel()
        self.mysql_connect()
        cur= connection.cursor()
        
        return cur

    def closeTunnel(self):
        
        self.mysql_disconnect()
        self.close_ssh_tunnel()

    def returnStation(self):

        self.open_ssh_tunnel()
        self.mysql_connect()
        cur= connection.cursor() 

        selectStatement="SELECT * FROM `observe_data`"
        cur.execute(selectStatement)

        stations = cur.fetchall()
        stationList=[(station[0],station[1]) for station in stations]

        return stationList

  
    def returnStationObserved(self,dateString):
        
        jsonDF=pd.read_json(
                f"https://api.all.bdservers.site/bmd_observed_data/observe_hourly.php?from_date={dateString}&to_date={dateString}"
            )
        
        observedDF=jsonDF[
            ['station_id','observation_time',
            'precipitation', 'temperature','relative_humidity','dewpoint','wind_speed','wind_direction',
            'visibility','total_cloud_cover',
            'station_level_pressure','sea_level_pressure'
            ]].copy(deep=True)
        
        return observedDF


    def returnSqlParameter(self,dateString,df,index):

        sqlValueList=[]

        
        stationID=df.iloc[index]['station_id']
        sqlValueList.append(stationID)

        forecastDate=datetime.strptime(dateString,'%Y-%m-%d')
        sqlValueList.append(f'{forecastDate}')

        # print(type(df.iloc[index]['observation_time']))
        obTime=df.iloc[index]['observation_time'][3:-4]
        
        startDate=dateString

        # print(obTime[:2])
        if (obTime[:2]=='34'
        ) | (obTime[:2]=='28') | (obTime[:2]=='24'
        ) | (obTime[:2]=='78') | (obTime[:2]=='71') | (obTime[:2]=='43'
        ) |(obTime[:2]=='32') |(obTime[:2]=='.0'
        ) | (obTime[:2]=='96') |(obTime[:2]=='64') |(obTime[:2]=='26') |(obTime[:2]=='44') |(obTime[:2]=='40'
        ) |(obTime[:2]=='.6') |(obTime[:2]=='OO') | (obTime[:2]=='90'
        ) | (obTime[:2]=='54') | (obTime[:2]=='60') | (obTime[:2]=='25') | (obTime[:2]=='98'

        ) | (obTime[:2]=='84') | (obTime[:2]=='70') | (obTime[:2]=='l8') | (obTime[:2]=='81'
        ) | (obTime[:2]=='2Q') : 
            
            print('Wrong Format..')

            print(obTime)
            obTime= obTime.replace(obTime,'21:00')
            print(obTime)

            startStep=startDate+' '+obTime
            startStep=datetime.strptime(startStep,'%Y-%m-%d %H:%M')
            sqlValueList.append(f'{startStep}')

            endStep = str((int(obTime[:2])+3)%24) + obTime[2:]
            endStep = startDate+' '+endStep
            endStep = datetime.strptime(endStep,'%Y-%m-%d %H:%M')
            sqlValueList.append(f'{endStep}')

        else:

            startStep=startDate+' '+obTime
            startStep=datetime.strptime(startStep,'%Y-%m-%d %H:%M')
            sqlValueList.append(f'{startStep}')

        # if (obTime[2:]=='34') | (obTime[2:]=='28') | (obTime[2:]=='.0') : 
        #     print('Wrong Format..')
        #     pass
        # else: 
            endStep = str((int(obTime[:2])+3)%24) + obTime[2:]
            endStep = startDate+' '+endStep
            endStep = datetime.strptime(endStep,'%Y-%m-%d %H:%M')
            sqlValueList.append(f'{endStep}')
        
        
        # Observed=df.iloc[index]['temperature']
        precipitation=df.iloc[index]['precipitation']
        sqlValueList.append(precipitation)

        temperature=df.iloc[index]['temperature']
        sqlValueList.append(temperature)

        relative_humidity=df.iloc[index]['relative_humidity']
        sqlValueList.append(relative_humidity)

        dewpoint=df.iloc[index]['dewpoint']
        sqlValueList.append(dewpoint)

        wind_speed=df.iloc[index]['wind_speed']
        sqlValueList.append(wind_speed)

        wind_direction=df.iloc[index]['wind_direction']
        sqlValueList.append(wind_direction)

        visibility=df.iloc[index]['visibility']
        sqlValueList.append(visibility)

        total_cloud_cover=df.iloc[index]['total_cloud_cover']
        sqlValueList.append(total_cloud_cover)

        station_level_pressure=df.iloc[index]['station_level_pressure']
        sqlValueList.append(station_level_pressure)

        sea_level_pressure=df.iloc[index]['sea_level_pressure']
        sqlValueList.append(sea_level_pressure)

        
        return sqlValueList 

    def insertObserved(self,dateString,tempDF):

        cur=self.openTunnel()

        for index in range(len(tempDF)):
            
            sqlValueList=self.returnSqlParameter(dateString,tempDF,index)

            

            insertValues=tuple(sqlValueList)
            print(f'{dateString} for - Station {insertValues[0]} Date: {insertValues[1]} Start Time: {insertValues[2]} End Time: {insertValues[3]} - - Inserting...')
            sqlStatement=f"INSERT INTO station_observed (stationID,forecastDate,startStep,endStep,precipitation,temperature, relative_humidity, dewpoint,wind_speed, wind_direction, visibility,total_cloud_cover, station_level_pressure, sea_level_pressure) VALUES {insertValues}"
            cur.execute(sqlStatement)
            connection.commit()

            # print(f'{dateString} for - {insertValues[0]} :inserted...')


    
def main():
    
    updateObject=stationObserved()
    # print(updateObject.dateInput)
    dateInput=updateObject.dateInput
    # print(dateInput)
    # year,month,day=[]
    # sdate = date(2021,1,19)   # start date
    # edate = date(2022,11,26)   # end date

    # dateRange=[sdate+timedelta(days=x) for x in range((edate-sdate).days)]
    # # print(dateRange[0])
    # dateStringRange=[datetime.strftime(dateString,'%Y-%m-%d') for dateString in dateRange]
    # # print(dateStringRange)


    # # print(dateRange)
    # # for dateInput in dateStringRange:

    observedDF=updateObject.returnStationObserved(dateInput)

    tempDF=observedDF.copy(deep=True)
    tempDF.dropna(inplace=True)

    updateObject.insertObserved(dateInput,tempDF)
    
    os._exit(0)

if __name__=='__main__':main()