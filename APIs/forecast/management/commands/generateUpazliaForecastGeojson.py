from django.core.management import BaseCommand, CommandError

from sqlalchemy import create_engine
import pymysql
import logging
import sshtunnel
from sshtunnel import SSHTunnelForwarder

from datetime import date, datetime, timedelta
import pandas as pd
import geopandas as gpd

ssh_host = '114.31.28.234'
# ssh_host = 
ssh_username = 'rimes'
ssh_password = 'inflamedwarrior666'
# database_name = 'bias_database'
database_name = 'weather_api'
localhost = '127.0.0.1'



class Command(BaseCommand):

    help='Update Daily Forecast data from Server-Site database to localhost SQL Table to update with recent'

    # def add_arguments(self, parser):
    # 		parser.add_argument('date', type=str, help='Enter Present Day')

    def handle(self, *args, **kwargs):

        updateDate=datetime.today()-timedelta(days=1)
        # updateDate=datetime.today()
        dateInput=datetime.strftime(updateDate,'%Y-%m-%d')
        
        print(dateInput)

        self.main(dateInput)
    

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

    def run_query(self,sql):
        return pd.read_sql_query(sql, connection)


    def mysql_disconnect(self):
        connection.close()

    def close_ssh_tunnel(self):
        tunnel.close

    def toSql(self,df,tableName):
        sqlEngine       = create_engine(f'mysql+pymysql://root:@localhost/{database_name}', pool_recycle=3600)
        dbConnection    = sqlEngine.connect()
        df.to_sql(con=dbConnection, name=tableName, if_exists='append', index=False)
    
    def remoteEngine(self):
        sqlEngine = create_engine(
            f'mysql+pymysql://rimes:inflamedwarrior666@114.31.28.234/{database_name}', pool_recycle=3600)
        dbConnection    = sqlEngine.connect()
        print(dbConnection)
        return sqlEngine
    
    def main(self,dateInput):
        
        self.open_ssh_tunnel()
        self.mysql_connect()

        table='apis_upazila_forecast_daily'
        parameterList=[1,2,3,6]
        df = self.run_query(f"SELECT * FROM `{table}` WHERE `forecast_date`='{dateInput}' AND `step_start`='{dateInput}' AND `parameter_id`='{parameterList[1]}';")

        forecastDF=df[['upazila_id','val_max']]
        forecastDF.rename(columns={'upazila_id':'OBJECTID'},inplace=True)
        forecastDF.to_json('upazila_forecast_daily.json')

        # print(df[['upazila_id','val_max']])

        # upazilaGeo=gpd.read_file('forecast/management/commands/upazila.geojson')
        # print(upazilaGeo)

        # tables=['apis_upazila_forecast_daily','apis_upazila_forecast_steps']
        # # table='apis_upazila_forecast_daily'
        # for table in tables:
        #     df = self.run_query(f"SELECT * FROM `{table}` WHERE `forecast_date`='{dateInput}';")
        #     self.toSql(df,f'{table}')
        

        self.mysql_disconnect()
        self.close_ssh_tunnel()


        # for table in tables:
        #     # print(table)
        #     df = self.run_query(f"SELECT * FROM `{table}`")
        #     self.toSql(df,f'{table}')
        # df = self.run_query(f"SELECT * FROM `{table}`;")

   